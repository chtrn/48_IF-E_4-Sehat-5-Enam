from __future__ import annotations
import argparse
from pathlib import Path
import joblib
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Prediksi G3 untuk data siswa baru (prototipe).")
    parser.add_argument("--model", default="outputs/model.joblib")
    parser.add_argument("--input", required=True, help="CSV input dengan kolom fitur yang sama.")
    parser.add_argument("--output", default="outputs/predictions.csv")
    parser.add_argument("--sep", default=";")
    parser.add_argument("--warning-threshold", type=float, default=11.0)
    args = parser.parse_args()

    artifact = joblib.load(args.model)
    df = pd.read_csv(args.input, sep=args.sep)
    cols = artifact["feature_columns"]
    missing = [c for c in cols if c not in df.columns]
    if missing:
        raise ValueError(f"Kolom input kurang: {missing}")
    pred = artifact["pipeline"].predict(df[cols])
    out = df.copy()
    out["predicted_G3"] = pred.round(2)
    out["warning_flag"] = out["predicted_G3"] < args.warning_threshold
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"Prediksi tersimpan: {args.output}")

if __name__ == "__main__":
    main()
