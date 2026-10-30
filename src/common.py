from __future__ import annotations
import hashlib
from pathlib import Path
import yaml
import pandas as pd


def load_config(path: str | Path = "config.yaml") -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve(base: Path, rel: str) -> Path:
    p = Path(rel)
    return p if p.is_absolute() else base / p


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_and_validate_data(config: dict, base: Path) -> pd.DataFrame:
    data_cfg = config["data"]
    path = resolve(base, data_cfg["path"])
    actual_hash = sha256_file(path)
    if actual_hash != data_cfg["sha256"]:
        raise ValueError(f"Checksum tidak cocok: {actual_hash}")
    df = pd.read_csv(path, sep=data_cfg.get("separator", ";"))
    expected = (data_cfg["expected_rows"], data_cfg["expected_columns"])
    if df.shape != expected:
        raise ValueError(f"Dimensi data {df.shape}, seharusnya {expected}")
    return df
