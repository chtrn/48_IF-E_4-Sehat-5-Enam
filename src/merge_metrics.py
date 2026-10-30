from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "outputs"
scenarios = ["early_all", "midperiod_all", "early_without_g3_zero"]
merged = {}
for name in scenarios:
    p = out / f"metrics_{name}.json"
    if not p.exists():
        raise FileNotFoundError(f"Belum ada {p.name}. Jalankan train.py --scenario {name}")
    merged[name] = json.loads(p.read_text(encoding="utf-8"))
(out / "metrics.json").write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
print(out / "metrics.json")
