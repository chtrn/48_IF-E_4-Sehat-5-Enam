"""Utilitas untuk memuat dataset Student Performance dari root proyek."""
from pathlib import Path
import pandas as pd

def project_root(start: str | Path | None = None) -> Path:
    """Temukan root proyek dari direktori kerja atau direktori induknya."""
    current = Path(start or Path.cwd()).resolve()
    for candidate in (current, *current.parents):
        if (candidate / "data" / "raw").exists() or (candidate / "README.md").exists() and (candidate / "notebooks").exists():
            return candidate
    return current

def load_student_math(path: str | Path | None = None) -> pd.DataFrame:
    """Membaca student-mat.csv dengan pemisah titik koma."""
    csv_path = Path(path) if path is not None else project_root() / "data" / "raw" / "student-mat.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"Dataset tidak ditemukan: {csv_path}. Letakkan student-mat.csv di data/raw/.")
    return pd.read_csv(csv_path, sep=";")
