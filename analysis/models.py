"""Pooled OLS with explicit, documented uncertainty calculations."""

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm


@dataclass
class ModelResult:
    model_id: str
    outcome: str
    with_claims: bool
    n_groups: int | None
    result: object


def percent_change(coefficient: float) -> float:
    """Exact percentage change for a one-unit increase in a log-level model."""
    return float(100 * np.expm1(coefficient))


def medicaid_design(frame: pd.DataFrame, with_claims: bool) -> pd.DataFrame:
    design = pd.DataFrame({"const": 1.0, "Tot_Mftr": frame["Tot_Mftr"]})
    for year in range(2018, 2022):
        design[f"year_{year}"] = frame["Year"].eq(year).astype(float)
    if with_claims:
        design["log_claims"] = frame["log_claims"]
    return design.astype(float)


def fit_medicaid(frame: pd.DataFrame) -> list[ModelResult]:
    """Unweighted pooled OLS; CR1 covariance and t(G-1) inference."""
    groups = frame["drug_group_id"]
    count = int(groups.nunique())
    if count < 2:
        raise ValueError("Clustered inference requires at least two drug groups.")
    models = []
    for outcome, stem in [
        ("log_unit_spend", "unit"), ("log_claim_spend", "claim"),
    ]:
        for with_claims in [False, True]:
            design = medicaid_design(frame, with_claims)
            if np.linalg.matrix_rank(design) != design.shape[1]:
                raise ValueError("The Medicaid model matrix is rank deficient.")
            result = sm.OLS(frame[outcome], design, missing="raise").fit(
                cov_type="cluster",
                cov_kwds={
                    "groups": groups,
                    "use_correction": True,
                    "df_correction": True,
                },
                use_t=True,
            )
            models.append(ModelResult(
                f"medicaid_{stem}_{'claims' if with_claims else 'year'}",
                outcome, with_claims, count, result,
            ))
    return models


def fit_costplus(frame: pd.DataFrame) -> list[ModelResult]:
    """Preserve the original notebook's HC3/normal-inference convention."""
    design = sm.add_constant(frame[["log_manuf_cost"]])
    models = []
    for outcome, stem in [
        ("log_retail_price", "retail"), ("log_markup", "markup"),
    ]:
        result = sm.OLS(frame[outcome], design, missing="raise").fit(
            cov_type="HC3", use_t=False
        )
        models.append(ModelResult(
            f"costplus_{stem}", outcome, False, None, result,
        ))
    return models


def coefficient_records(models: list[ModelResult]) -> pd.DataFrame:
    records = []
    for model in models:
        result = model.result
        intervals = result.conf_int(alpha=0.05)
        for term in result.params.index:
            estimate = float(result.params[term])
            lower, upper = map(float, intervals.loc[term])
            records.append({
                "model_id": model.model_id,
                "outcome": model.outcome,
                "with_log_claims": model.with_claims,
                "term": term,
                "estimate": estimate,
                "std_error": float(result.bse[term]),
                "p_value": float(result.pvalues[term]),
                "ci_lower": lower,
                "ci_upper": upper,
                "observations": int(result.nobs),
                "drug_groups": model.n_groups,
                "r_squared": float(result.rsquared),
                "adjusted_r_squared": float(result.rsquared_adj),
                "covariance": result.cov_type,
                "inference": "t(G-1)" if model.n_groups else "normal",
                "percent_change": percent_change(estimate) if term == "Tot_Mftr" else None,
                "percent_ci_lower": percent_change(lower) if term == "Tot_Mftr" else None,
                "percent_ci_upper": percent_change(upper) if term == "Tot_Mftr" else None,
            })
    return pd.DataFrame.from_records(records)
