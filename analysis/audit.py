"""Independent checks of the source data, panel construction, and model samples."""

from __future__ import annotations

import numpy as np
import pandas as pd


YEARS = tuple(range(2017, 2022))
IDENTIFIERS = ("Brnd_Name", "Gnrc_Name", "Tot_Mftr", "Mftr_Name")
METRICS = (
    "Tot_Spndng",
    "Tot_Dsg_Unts",
    "Tot_Clms",
    "Avg_Spnd_Per_Dsg_Unt_Wghtd",
    "Avg_Spnd_Per_Clm",
    "Outlier_Flag",
)
PANEL_COLUMNS = (*IDENTIFIERS, "Year", *METRICS)
ROW_KEY = ("Brnd_Name", "Gnrc_Name", "Mftr_Name", "Year")
DRUG_KEY = ("Brnd_Name", "Gnrc_Name")
POSITIVE_COLUMNS = (
    "Tot_Mftr",
    "Tot_Spndng",
    "Tot_Dsg_Unts",
    "Tot_Clms",
    "Avg_Spnd_Per_Dsg_Unt_Wghtd",
    "Avg_Spnd_Per_Clm",
)


def _compare_panels(left: pd.DataFrame, right: pd.DataFrame) -> dict:
    """Compare by a unique semantic key, independently of row order."""
    missing_columns = sorted(set(PANEL_COLUMNS) - set(left) | (set(PANEL_COLUMNS) - set(right)))
    if missing_columns:
        return {"matches": False, "missing_columns": missing_columns}
    duplicate_left = int(left.duplicated(list(ROW_KEY)).sum())
    duplicate_right = int(right.duplicated(list(ROW_KEY)).sum())
    if len(left) != len(right) or duplicate_left or duplicate_right:
        return {
            "matches": False,
            "left_rows": int(len(left)),
            "right_rows": int(len(right)),
            "left_duplicate_keys": duplicate_left,
            "right_duplicate_keys": duplicate_right,
        }
    lhs = left.loc[:, PANEL_COLUMNS].sort_values(list(ROW_KEY)).reset_index(drop=True)
    rhs = right.loc[:, PANEL_COLUMNS].sort_values(list(ROW_KEY)).reset_index(drop=True)
    mismatches = {}
    for name in PANEL_COLUMNS:
        if name in (*METRICS, "Tot_Mftr", "Year"):
            # Source and saved panel are CSVs. Permit only float round-trip error.
            equal = np.isclose(
                lhs[name].to_numpy(dtype=float),
                rhs[name].to_numpy(dtype=float),
                rtol=1e-12,
                atol=1e-12,
                equal_nan=True,
            )
        else:
            equal = (
                lhs[name].eq(rhs[name]) | (lhs[name].isna() & rhs[name].isna())
            ).to_numpy()
        mismatches[name] = int((~equal).sum())
    return {
        "matches": not any(mismatches.values()),
        "rows_compared": int(len(lhs)),
        "mismatched_cells_by_column": mismatches,
        "numeric_relative_tolerance": 1e-12,
        "numeric_absolute_tolerance": 1e-12,
    }


def _positive_finite(frame: pd.DataFrame, columns: tuple[str, ...]) -> pd.Series:
    values = frame.loc[:, columns].to_numpy(dtype=float)
    return pd.Series(
        (np.isfinite(values) & (values > 0)).all(axis=1), index=frame.index
    )


def _distribution(series: pd.Series) -> dict[str, int]:
    return {str(key): int(value) for key, value in series.sort_index().items()}


def run_audit(
    raw: pd.DataFrame,
    panel: pd.DataFrame,
    filtered: pd.DataFrame,
    costplus: pd.DataFrame,
    *,
    legacy_panel: pd.DataFrame | None = None,
) -> dict:
    """Return JSON-safe diagnostics without modifying any supplied DataFrame.

    The source/panel comparison is reconstructed separately for each year.
    Production callers also provide the historical panel to check the old
    missing-to-zero transformation. Reference counts describe this saved
    historical snapshot; they are separate from the structural checks so that
    small synthetic datasets can exercise the same audit.
    """
    source_year_checks = {}
    for year in YEARS:
        names = [f"{metric}_{year}" for metric in METRICS]
        expected = raw.loc[:, [*IDENTIFIERS, *names]].rename(
            columns=dict(zip(names, METRICS))
        )
        expected["Year"] = year
        source_year_checks[str(year)] = _compare_panels(
            expected, panel.loc[panel["Year"].eq(year)]
        )

    legacy_comparison = None
    if legacy_panel is not None:
        legacy_expected = panel.loc[:, PANEL_COLUMNS].copy()
        legacy_expected.loc[:, METRICS] = legacy_expected.loc[:, METRICS].fillna(0)
        legacy_comparison = _compare_panels(legacy_expected, legacy_panel)

    historical_filter = (
        panel["Mftr_Name"].eq("Overall")
        & panel["Outlier_Flag"].eq(0)
        & panel["Tot_Spndng"].gt(0)
    )
    positive = _positive_finite(panel, POSITIVE_COLUMNS)
    expected_sample = panel.loc[historical_filter & positive]
    sample_comparison = _compare_panels(expected_sample, filtered)
    drug_groups = filtered.groupby(list(DRUG_KEY), dropna=False, sort=True)
    group_year_counts = drug_groups["Year"].nunique()
    grouped_brand_year = filtered.groupby(["Brnd_Name", "Year"], dropna=False).size()
    group_count_variation = drug_groups["Tot_Mftr"].nunique()
    brand_count_variation = filtered.groupby("Brnd_Name", dropna=False)["Tot_Mftr"].nunique()
    group_id_consistent = (
        "drug_group_id" in filtered
        and int(filtered["drug_group_id"].nunique()) == int(len(drug_groups))
        and bool(drug_groups["drug_group_id"].nunique().eq(1).all())
    )
    required_logs = {
        "log_unit_spend": "Avg_Spnd_Per_Dsg_Unt_Wghtd",
        "log_claim_spend": "Avg_Spnd_Per_Clm",
        "log_claims": "Tot_Clms",
    }
    log_checks = {}
    for log_column, source_column in required_logs.items():
        log_checks[log_column] = bool(
            log_column in filtered
            and np.allclose(
                filtered[log_column],
                np.log(filtered[source_column]),
                rtol=1e-12,
                atol=1e-12,
            )
        )
    claim_identity_error = (
        filtered["Avg_Spnd_Per_Clm"]
        - filtered["Tot_Spndng"] / filtered["Tot_Clms"]
    ).abs()

    expected_cost = (costplus["CP_price"] - 3) / 1.15
    expected_markup = ((costplus["retail_price"] - 3) / expected_cost - 1) * 100
    cost_columns = (
        "manuf_cost", "retail_price", "markup",
        "log_manuf_cost", "log_retail_price", "log_markup",
    )
    cp_finite = bool(
        set(cost_columns).issubset(costplus.columns)
        and np.isfinite(costplus.loc[:, cost_columns].to_numpy(dtype=float)).all()
    )
    cost_checks = {
        "manufacturing_cost_formula": bool(
            np.allclose(costplus["manuf_cost"], expected_cost, rtol=1e-12, atol=1e-12)
        ),
        "markup_formula": bool(
            np.allclose(costplus["markup"], expected_markup, rtol=1e-12, atol=1e-12)
        ),
        "positive_log_inputs": bool(
            _positive_finite(costplus, ("manuf_cost", "retail_price", "markup")).all()
        ),
        "finite_values_and_logs": cp_finite,
    }
    for log_column, source_column in (
        ("log_manuf_cost", "manuf_cost"),
        ("log_retail_price", "retail_price"),
        ("log_markup", "markup"),
    ):
        cost_checks[log_column] = bool(
            np.allclose(
                costplus[log_column], np.log(costplus[source_column]),
                rtol=1e-12, atol=1e-12,
            )
        )

    checks = {
        "source_identifiers_unique": not bool(raw.duplicated(list(IDENTIFIERS)).any()),
        "panel_rows_equal_source_rows_times_years": len(panel) == len(raw) * len(YEARS),
        "panel_years_expected": set(panel["Year"].unique()) == set(YEARS),
        "all_years_match_source": all(item["matches"] for item in source_year_checks.values()),
        "sample_matches_documented_filters": sample_comparison["matches"],
        "drug_group_year_keys_unique": not bool(
            filtered.duplicated([*DRUG_KEY, "Year"]).any()
        ),
        "drug_group_identifiers_consistent": group_id_consistent,
        "manufacturer_count_constant_within_drug_group": bool(group_count_variation.le(1).all()),
        "all_medicaid_log_columns_correct": all(log_checks.values()),
        "costplus_calculations_valid": all(cost_checks.values()),
    }
    if legacy_comparison is not None:
        checks["legacy_panel_matches_missing_to_zero_transformation"] = legacy_comparison["matches"]

    return {
        "passed": all(checks.values()),
        "checks": checks,
        "reference_snapshot": {
            "expected_medicaid_observations": 12740,
            "expected_medicaid_drug_groups": 3244,
            "expected_costplus_observations": 442,
            "matches": (
                len(filtered) == 12740
                and len(drug_groups) == 3244
                and len(costplus) == 442
            ),
        },
        "source": {
            "rows": int(len(raw)),
            "years": list(YEARS),
            "source_year_checks": source_year_checks,
        },
        "panel": {
            "rows": int(len(panel)),
            "missing_values_by_metric": {
                metric: int(panel[metric].isna().sum()) for metric in METRICS
            },
            "legacy_comparison": legacy_comparison,
            "legacy_missing_value_policy": "Missing yearly metrics were replaced with zero.",
            "current_missing_value_policy": "Source missing values are preserved.",
        },
        "medicaid": {
            "observations": int(len(filtered)),
            "drug_groups": int(len(drug_groups)),
            "brand_names": int(filtered["Brnd_Name"].nunique()),
            "observations_by_year": _distribution(filtered["Year"].value_counts()),
            "years_observed_per_drug_group": _distribution(group_year_counts.value_counts()),
            "historical_filter_observations": int(historical_filter.sum()),
            "additional_nonpositive_or_nonfinite_exclusions": int((historical_filter & ~positive).sum()),
            "sample_comparison": sample_comparison,
            "duplicate_drug_group_year_excess_rows": int(filtered.duplicated([*DRUG_KEY, "Year"]).sum()),
            "duplicate_brand_year_keys": int(grouped_brand_year.gt(1).sum()),
            "duplicate_brand_year_excess_rows": int((grouped_brand_year - 1).clip(lower=0).sum()),
            "brand_names_with_multiple_manufacturer_counts": int(brand_count_variation.gt(1).sum()),
            "drug_groups_with_multiple_manufacturer_counts": int(group_count_variation.gt(1).sum()),
            "log_checks": log_checks,
            "spending_per_claim_identity_max_absolute_error": float(claim_identity_error.max()),
            "manufacturer_count_interpretation": (
                "One source column is repeated across years. Apparent within-brand variation "
                "comes from grouping different brand/generic pairs, not annual manufacturer entry."
            ),
        },
        "costplus": {
            "observations": int(len(costplus)),
            "calculations": cost_checks,
            "duplicate_medication_excess_rows": int(costplus.duplicated(["medication"]).sum()),
            "duplicate_medication_form_excess_rows": int(costplus.duplicated(["medication", "form"]).sum()),
        },
    }
