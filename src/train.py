from __future__ import annotations
import argparse
import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, precision_score, recall_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from common import load_config, load_and_validate_data, resolve

SCENARIOS = {
    "early_all": (False, False),
    "midperiod_all": (True, False),
    "early_without_g3_zero": (False, True),
}


def make_xy(df: pd.DataFrame, cfg: dict, include_absences: bool = False, drop_g3_zero: bool = False):
    target = cfg["target"]["column"]
    work = df.copy()
    if drop_g3_zero:
        work = work.loc[work[target] != 0].copy()
    exclude = list(cfg["features"]["always_exclude"])
    if not include_absences:
        exclude += list(cfg["features"]["early_prediction_exclude"])
    X = work.drop(columns=[target] + exclude)
    y = work[target].astype(float)
    risk = (y < cfg["target"]["actual_risk_threshold"]).astype(int)
    g3_zero = (y == 0).astype(int)
    strata = (risk * 2 + g3_zero).astype(str)
    return X, y, strata


def make_preprocessor(X: pd.DataFrame):
    categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric = [c for c in X.columns if c not in categorical]
    return ColumnTransformer([
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), categorical),
        ("num", StandardScaler(), numeric),
    ], remainder="drop", verbose_feature_names_out=False)


def model_defs(cfg: dict):
    seed = cfg["project"]["random_seed"]
    rf_cfg = cfg["models"]["random_forest"]
    return {
        "Baseline mean": DummyRegressor(strategy="mean"),
        "Ridge Regression": Ridge(alpha=cfg["models"]["ridge"]["alpha"]),
        "Random Forest": RandomForestRegressor(
            n_estimators=rf_cfg["n_estimators"],
            min_samples_leaf=rf_cfg["min_samples_leaf"],
            max_features=rf_cfg["max_features"],
            random_state=seed,
            n_jobs=rf_cfg["n_jobs"],
        ),
    }


def evaluate(X, y, strata, cfg):
    cv_cfg = cfg["validation"]
    cv = RepeatedStratifiedKFold(
        n_splits=cv_cfg["n_splits"],
        n_repeats=cv_cfg["n_repeats"],
        random_state=cfg["project"]["random_seed"],
    )
    rows = []
    warning_t = cfg["target"]["predicted_warning_threshold"]
    actual_t = cfg["target"]["actual_risk_threshold"]

    for model_name, estimator in model_defs(cfg).items():
        for fold, (tr, te) in enumerate(cv.split(X, strata), start=1):
            pipe = Pipeline([
                ("prep", make_preprocessor(X.iloc[tr])),
                ("model", clone(estimator)),
            ])
            pipe.fit(X.iloc[tr], y.iloc[tr])
            pred = pipe.predict(X.iloc[te])
            actual_risk = (y.iloc[te].to_numpy() < actual_t).astype(int)
            pred_risk = (pred < warning_t).astype(int)
            rows.append({
                "model": model_name,
                "fold": fold,
                "rmse": float(mean_squared_error(y.iloc[te], pred) ** 0.5),
                "mae": float(mean_absolute_error(y.iloc[te], pred)),
                "r2": float(r2_score(y.iloc[te], pred)),
                "recall_risk": float(recall_score(actual_risk, pred_risk, zero_division=0)),
                "precision_risk": float(precision_score(actual_risk, pred_risk, zero_division=0)),
            })

    folds = pd.DataFrame(rows)
    summary = folds.groupby("model", as_index=False).agg(
        rmse_mean=("rmse", "mean"),
        rmse_std=("rmse", "std"),
        mae_mean=("mae", "mean"),
        r2_mean=("r2", "mean"),
        recall_mean=("recall_risk", "mean"),
        precision_mean=("precision_risk", "mean"),
    )
    return summary


def run_one_scenario(cfg_path: Path, scenario: str, output_path: Path):
    cfg = load_config(cfg_path)
    base = cfg_path.parent
    df = load_and_validate_data(cfg, base)
    include_absences, drop_zero = SCENARIOS[scenario]
    X, y, strata = make_xy(df, cfg, include_absences, drop_zero)
    summary = evaluate(X, y, strata, cfg)
    payload = {
        "n": int(len(y)),
        "include_absences": include_absences,
        "drop_g3_zero": drop_zero,
        "summary": summary.to_dict(orient="records"),
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def aggregate_rf_importance(final_pipe: Pipeline, X: pd.DataFrame) -> pd.DataFrame:
    prep = final_pipe.named_steps["prep"]
    rf = final_pipe.named_steps["model"]
    transformed = list(prep.get_feature_names_out())
    categorical = X.select_dtypes(include=["object", "category"]).columns.tolist()
    numeric = [c for c in X.columns if c not in categorical]
    agg = {c: 0.0 for c in X.columns}
    for name, imp in zip(transformed, rf.feature_importances_):
        if name in numeric:
            source = name
        else:
            matches = [c for c in categorical if name.startswith(c + "_")]
            source = max(matches, key=len) if matches else name
        agg[source] = agg.get(source, 0.0) + float(imp)
    return pd.DataFrame({"feature": list(agg), "importance": list(agg.values())}).sort_values(
        "importance", ascending=False
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config.yaml")
    parser.add_argument("--scenario", choices=SCENARIOS.keys(), default="early_all")
    parser.add_argument("--scenario-output", default=None)
    args = parser.parse_args()

    cfg_path = Path(args.config).resolve()
    cfg = load_config(cfg_path)
    base = cfg_path.parent
    df = load_and_validate_data(cfg, base)
    outdir = resolve(base, cfg["outputs"]["directory"])
    outdir.mkdir(parents=True, exist_ok=True)

    include_absences, drop_zero = SCENARIOS[args.scenario]
    X, y, strata = make_xy(df, cfg, include_absences, drop_zero)
    summary = evaluate(X, y, strata, cfg)
    payload = {
        "n": int(len(y)),
        "include_absences": include_absences,
        "drop_g3_zero": drop_zero,
        "summary": summary.to_dict(orient="records"),
    }
    scenario_out = Path(args.scenario_output).resolve() if args.scenario_output else outdir / f"metrics_{args.scenario}.json"
    scenario_out.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    if args.scenario == "early_all":
        final_pipe = Pipeline([
            ("prep", make_preprocessor(X)),
            ("model", model_defs(cfg)["Random Forest"]),
        ])
        final_pipe.fit(X, y)
        joblib.dump(
            {"pipeline": final_pipe, "feature_columns": X.columns.tolist()},
            outdir / cfg["outputs"]["model_file"],
        )
        aggregate_rf_importance(final_pipe, X).to_csv(
            outdir / cfg["outputs"]["feature_importance_file"], index=False
        )

    print(f"Selesai: {args.scenario}")
    print(summary.round(3).to_string(index=False))
    print(f"\nMetrik tersimpan di: {scenario_out}")


if __name__ == "__main__":
    main()
