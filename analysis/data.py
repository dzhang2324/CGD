"""Read immutable historical inputs and construct explicit analysis samples."""

from pathlib import Path

import numpy as np
import pandas as pd

YEARS = tuple(range(2017, 2022))
IDENTIFIERS = ["Brnd_Name", "Gnrc_Name", "Tot_Mftr", "Mftr_Name"]
METRICS = [
    "Tot_Spndng", "Tot_Dsg_Unts", "Tot_Clms",
    "Avg_Spnd_Per_Dsg_Unt_Wghtd", "Avg_Spnd_Per_Clm", "Outlier_Flag",
]
POSITIVE_COLUMNS = ["Tot_Mftr", *METRICS[:-1]]


def load_medicaid(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Preserve source missingness; apply the same positive sample to all models."""
    raw = pd.read_csv(data_dir / "Medicaid_Spending_by_Drug_2021.csv")
    required = IDENTIFIERS + [
        f"{metric}_{year}" for year in YEARS for metric in METRICS
    ]
    missing = set(required) - set(raw.columns)
    if missing:
        raise ValueError(f"Missing Medicaid source columns: {sorted(missing)}")
    if raw[IDENTIFIERS].isna().any().any():
        raise ValueError("Medicaid identifiers must not be missing.")
    if raw.duplicated(["Brnd_Name", "Gnrc_Name", "Mftr_Name"]).any():
        raise ValueError("Duplicate Medicaid source drug/manufacturer identifiers.")
    pieces = []
    for year in YEARS:
        names = {f"{metric}_{year}": metric for metric in METRICS}
        piece = raw[IDENTIFIERS + list(names)].rename(columns=names).copy()
        piece["Year"] = year
        piece["_source_row"] = np.arange(len(raw))
        pieces.append(piece)
    panel = (
        pd.concat(pieces, ignore_index=True)
        .sort_values(["_source_row", "Year"])
        .drop(columns="_source_row")
        .loc[:, IDENTIFIERS + ["Year"] + METRICS]
        .reset_index(drop=True)
    )
    values = panel[POSITIVE_COLUMNS].to_numpy(dtype=float)
    positive = np.isfinite(values).all(axis=1) & (values > 0).all(axis=1)
    eligible = (
        panel["Mftr_Name"].eq("Overall")
        & panel["Outlier_Flag"].eq(0)
        & positive
    )
    filtered = panel.loc[eligible].copy().reset_index(drop=True)
    if filtered.empty:
        raise ValueError("No Medicaid observations meet the sample rules.")
    keys = ["Brnd_Name", "Gnrc_Name"]
    if filtered.duplicated(keys + ["Year"]).any():
        raise ValueError("Duplicate Medicaid drug-group/year observations.")
    if filtered.groupby(keys)["Tot_Mftr"].nunique().gt(1).any():
        raise ValueError("Unexpected time variation in source manufacturer counts.")
    filtered["drug_group_id"] = pd.factorize(
        pd.MultiIndex.from_frame(filtered[keys]), sort=True
    )[0]
    for destination, source in [
        ("log_unit_spend", "Avg_Spnd_Per_Dsg_Unt_Wghtd"),
        ("log_claim_spend", "Avg_Spnd_Per_Clm"),
        ("log_claims", "Tot_Clms"),
    ]:
        filtered[destination] = np.log(filtered[source])
    return raw, panel, filtered


def load_costplus(data_dir: Path) -> pd.DataFrame:
    """Reproduce the original snapshot's constructed costs and markups."""
    frame = pd.read_csv(data_dir / "costplus.csv")
    frame["manuf_cost"] = (frame["CP_price"] - 3) / 1.15
    frame["markup"] = ((frame["retail_price"] - 3) / frame["manuf_cost"] - 1) * 100
    sources = ["manuf_cost", "retail_price", "markup"]
    values = frame[sources].to_numpy(dtype=float)
    if not (np.isfinite(values).all() and (values > 0).all()):
        raise ValueError("Cost Plus contains nonpositive or nonfinite log inputs.")
    for destination, source in zip(
        ["log_manuf_cost", "log_retail_price", "log_markup"], sources
    ):
        frame[destination] = np.log(frame[source])
    return frame
