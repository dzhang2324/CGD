"""Run from the repository root: python -m analysis.run."""

import argparse
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import tempfile

# Matplotlib's cache should never require write access outside this project.
os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "cgd-matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(Path(tempfile.gettempdir()) / "cgd-cache"))

import pandas as pd

from .audit import run_audit
from .data import load_costplus, load_medicaid
from .models import coefficient_records, fit_costplus, fit_medicaid
from .report import write_reports

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "analysis" / "output")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    data = ROOT / "data"
    raw, panel, filtered = load_medicaid(data / "raw")
    costplus = load_costplus(data / "raw")
    inputs = {
        "Medicaid_Spending_by_Drug_2021.csv": data / "raw" / "Medicaid_Spending_by_Drug_2021.csv",
        "med_panel.csv": data / "reference" / "med_panel.csv",
        "costplus.csv": data / "raw" / "costplus.csv",
    }
    audit = run_audit(
        raw, panel, filtered, costplus,
        legacy_panel=pd.read_csv(inputs["med_panel.csv"]),
    )
    audit["input_sha256"] = {
        name: hashlib.sha256(path.read_bytes()).hexdigest()
        for name, path in inputs.items()
    }
    audit["environment"] = {
        "python": platform.python_version(),
        "packages": {
            name: importlib.metadata.version(name)
            for name in ["numpy", "pandas", "scipy", "statsmodels", "matplotlib"]
        },
    }
    (output / "audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    if not audit["passed"] or not audit["reference_snapshot"]["matches"]:
        raise RuntimeError(f"Data audit failed; inspect {output / 'audit.json'}")
    medicaid = fit_medicaid(filtered)
    cp = fit_costplus(costplus)
    records = coefficient_records(medicaid + cp)
    records.to_csv(output / "estimates.csv", index=False, float_format="%.17g")
    # JSON nulls, rather than NaN, make the output usable outside Python.
    (output / "estimates.json").write_text(
        records.to_json(orient="records", indent=2, double_precision=15) + "\n"
    )
    filtered[["drug_group_id", "Brnd_Name", "Gnrc_Name"]].drop_duplicates().to_csv(
        output / "drug_groups.csv", index=False
    )
    write_reports(output, panel, filtered, costplus, medicaid, cp)
    focus = records.loc[records["term"].isin(["Tot_Mftr", "log_manuf_cost"])]
    print(focus[["model_id", "estimate", "std_error", "p_value", "percent_change"]].to_string(index=False))
    print(f"\nAudit passed. Results written to {output}")


if __name__ == "__main__":
    main()
