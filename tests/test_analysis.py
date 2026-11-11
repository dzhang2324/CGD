"""Small independent examples for panel construction and audit safeguards."""

import json

import numpy as np
import pandas as pd
import pytest

from analysis.audit import METRICS, YEARS, run_audit
from analysis.data import load_costplus, load_medicaid


@pytest.fixture
def example_data(tmp_path):
    """Create 25 potential drug-year rows, of which exactly 11 are eligible."""
    rows = []
    identifiers = [
        ("Shared", "First compound", 2, "Overall"),
        ("Shared", "Second compound", 5, "Overall"),
        ("Excluded", "Third compound", 1, "Overall"),
        ("Shared", "First compound", 2, "Actual manufacturer"),
        ("One-year drug", "Fourth compound", 1, "Overall"),
    ]
    expected_panel = []
    for row_number, (brand, generic, count, manufacturer) in enumerate(identifiers):
        row = {
            "Brnd_Name": brand,
            "Gnrc_Name": generic,
            "Tot_Mftr": count,
            "Mftr_Name": manufacturer,
        }
        for year in YEARS:
            values = {
                "Tot_Spndng": 100.0,
                "Tot_Dsg_Unts": 50.0,
                "Tot_Clms": 10.0,
                "Avg_Spnd_Per_Dsg_Unt_Wghtd": 2.0,
                "Avg_Spnd_Per_Clm": 10.0,
                "Outlier_Flag": 0.0,
            }
            if (row_number == 2 and year == 2017) or (row_number == 4 and year > 2017):
                values = {metric: np.nan for metric in METRICS}
            elif row_number == 2:
                field = {
                    2018: "Outlier_Flag",
                    2019: "Tot_Clms",
                    2020: "Avg_Spnd_Per_Dsg_Unt_Wghtd",
                    2021: "Tot_Spndng",
                }[year]
                values[field] = 1.0 if field == "Outlier_Flag" else 0.0
            row.update({f"{metric}_{year}": values[metric] for metric in METRICS})
            expected_panel.append(
                {
                    "Brnd_Name": brand,
                    "Gnrc_Name": generic,
                    "Tot_Mftr": count,
                    "Mftr_Name": manufacturer,
                    "Year": year,
                    **values,
                }
            )
        rows.append(row)
    raw = pd.DataFrame(rows)
    raw.to_csv(tmp_path / "Medicaid_Spending_by_Drug_2021.csv", index=False)
    costplus = pd.DataFrame(
        {
            "medication": ["First generic", "Second generic"],
            "brand_name": ["First brand", "Second brand"],
            "form": ["Tablet", "Capsule"],
            "retail_price": [53.0, 123.0],
            "CP_price": [14.5, 26.0],
        }
    )
    costplus.to_csv(tmp_path / "costplus.csv", index=False)
    return tmp_path, pd.DataFrame(expected_panel)


def test_panel_preserves_missingness_and_uses_pair_identifiers(example_data):
    directory, expected_panel = example_data
    _, panel, sample = load_medicaid(directory)
    pd.testing.assert_frame_equal(
        panel.loc[:, expected_panel.columns].reset_index(drop=True),
        expected_panel,
        check_dtype=False,
    )
    assert len(panel) == 25
    assert int(panel["Tot_Spndng"].isna().sum()) == 5
    assert len(sample) == 11
    assert sample["drug_group_id"].nunique() == 3
    assert sample.loc[sample["Brnd_Name"].eq("Shared"), "drug_group_id"].nunique() == 2
    assert sample["Mftr_Name"].eq("Overall").all()
    assert not sample.duplicated(["Brnd_Name", "Gnrc_Name", "Year"]).any()
    assert set(sample["Brnd_Name"]) == {"Shared", "One-year drug"}
    np.testing.assert_allclose(sample["log_claims"], np.log(10))
    np.testing.assert_allclose(sample["log_unit_spend"], np.log(2))
    np.testing.assert_allclose(sample["log_claim_spend"], np.log(10))


def test_costplus_construction_matches_hand_calculations(example_data):
    directory, _ = example_data
    costplus = load_costplus(directory)
    np.testing.assert_allclose(costplus["manuf_cost"], [10, 20])
    np.testing.assert_allclose(costplus["markup"], [400, 500])
    np.testing.assert_allclose(costplus["log_manuf_cost"], np.log([10, 20]))
    np.testing.assert_allclose(costplus["log_markup"], np.log([400, 500]))
    np.testing.assert_allclose(costplus["log_retail_price"], np.log([53, 123]))


def test_audit_distinguishes_missing_data_and_false_brand_variation(example_data):
    directory, expected_panel = example_data
    raw, panel, sample = load_medicaid(directory)
    costplus = load_costplus(directory)
    legacy = expected_panel.copy()
    legacy.loc[:, METRICS] = legacy.loc[:, METRICS].fillna(0)
    audit = run_audit(raw, panel, sample, costplus, legacy_panel=legacy)
    assert audit["passed"], audit["checks"]
    assert audit["medicaid"]["observations"] == 11
    assert audit["medicaid"]["drug_groups"] == 3
    assert audit["medicaid"]["duplicate_brand_year_keys"] == 5
    assert audit["medicaid"]["duplicate_brand_year_excess_rows"] == 5
    assert audit["medicaid"]["duplicate_drug_group_year_excess_rows"] == 0
    assert audit["medicaid"]["brand_names_with_multiple_manufacturer_counts"] == 1
    assert audit["medicaid"]["drug_groups_with_multiple_manufacturer_counts"] == 0
    assert audit["medicaid"]["additional_nonpositive_or_nonfinite_exclusions"] == 2
    assert audit["panel"]["missing_values_by_metric"]["Tot_Spndng"] == 5
    assert audit["panel"]["legacy_comparison"]["matches"]
    # JSON artifacts must not contain NumPy scalars or nonstandard NaN literals.
    json.dumps(audit, allow_nan=False)


def test_audit_detects_an_altered_legacy_value(example_data):
    directory, expected_panel = example_data
    raw, panel, sample = load_medicaid(directory)
    costplus = load_costplus(directory)
    legacy = expected_panel.copy()
    legacy.loc[:, METRICS] = legacy.loc[:, METRICS].fillna(0)
    legacy.loc[0, "Tot_Spndng"] += 1
    audit = run_audit(raw, panel, sample, costplus, legacy_panel=legacy)
    assert not audit["passed"]
    assert not audit["checks"]["legacy_panel_matches_missing_to_zero_transformation"]
    assert audit["panel"]["legacy_comparison"]["mismatched_cells_by_column"]["Tot_Spndng"] == 1


def test_audit_detects_an_omitted_eligible_observation(example_data):
    directory, _ = example_data
    raw, panel, sample = load_medicaid(directory)
    costplus = load_costplus(directory)
    audit = run_audit(raw, panel, sample.iloc[1:].copy(), costplus)
    assert not audit["passed"]
    assert not audit["checks"]["sample_matches_documented_filters"]


def test_audit_detects_an_incorrect_generated_log(example_data):
    directory, _ = example_data
    raw, panel, sample = load_medicaid(directory)
    sample.loc[sample.index[0], "log_unit_spend"] += 0.1
    audit = run_audit(raw, panel, sample, load_costplus(directory))
    assert not audit["passed"]
    assert not audit["checks"]["all_medicaid_log_columns_correct"]
