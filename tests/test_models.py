"""Check clustered uncertainty against an independently computed sandwich."""

import numpy as np
import pandas as pd
from scipy import stats

from analysis.models import fit_costplus, fit_medicaid, medicaid_design, percent_change


def synthetic_medicaid():
    rows = []
    for group in range(12):
        for year in range(2017, 2022):
            claims = 3 + 0.17 * group + 0.04 * (year - 2017) ** 2
            residual = 0.3 * np.sin(group + 2 * year)
            outcome = 1.8 - 0.12 * (group % 7 + 1) + 0.2 * claims + residual
            rows.append({
                "drug_group_id": group, "Year": year,
                "Tot_Mftr": group % 7 + 1, "log_claims": claims,
                "log_unit_spend": outcome, "log_claim_spend": outcome + claims / 3,
            })
    return pd.DataFrame(rows)


def test_clustered_covariance_matches_hand_calculation():
    frame = synthetic_medicaid()
    model = fit_medicaid(frame)[1]
    x = medicaid_design(frame, True).to_numpy()
    y = frame["log_unit_spend"].to_numpy()
    beta = np.linalg.lstsq(x, y, rcond=None)[0]
    residuals = y - x @ beta
    bread = np.linalg.inv(x.T @ x)
    meat = np.zeros((x.shape[1], x.shape[1]))
    for group in frame["drug_group_id"].unique():
        mask = frame["drug_group_id"].eq(group).to_numpy()
        score = x[mask].T @ residuals[mask]
        meat += np.outer(score, score)
    n, k = x.shape
    g = frame["drug_group_id"].nunique()
    expected = bread @ meat @ bread * g / (g - 1) * (n - 1) / (n - k)
    np.testing.assert_allclose(model.result.params, beta, rtol=1e-10, atol=1e-10)
    np.testing.assert_allclose(model.result.cov_params(), expected, rtol=1e-9, atol=1e-10)
    expected_p = 2 * stats.t.sf(np.abs(beta / np.sqrt(expected.diagonal())), df=g - 1)
    np.testing.assert_allclose(model.result.pvalues, expected_p, rtol=1e-9, atol=1e-10)
    np.testing.assert_allclose(
        model.result.conf_int().iloc[:, 0],
        beta - stats.t.ppf(0.975, g - 1) * np.sqrt(expected.diagonal()),
    )


def test_exact_percentage_conversion_and_interval_monotonicity():
    assert np.isclose(percent_change(-0.124), -11.662015915)
    assert percent_change(0) == 0
    assert percent_change(-0.2) < percent_change(-0.124) < percent_change(-0.05)


def test_costplus_hc3_matches_hand_calculation():
    x = np.linspace(-1, 3, 35)
    y = 2 + 0.7 * x + np.sin(x * 2) * (x + 2) / 10
    frame = pd.DataFrame({"log_manuf_cost": x, "log_retail_price": y, "log_markup": y - x})
    model = fit_costplus(frame)[0]
    design = np.column_stack([np.ones(len(x)), x])
    bread = np.linalg.inv(design.T @ design)
    beta = bread @ design.T @ y
    residuals = y - design @ beta
    leverage = np.sum((design @ bread) * design, axis=1)
    expected = bread @ (
        design.T @ np.diag((residuals / (1 - leverage)) ** 2) @ design
    ) @ bread
    np.testing.assert_allclose(model.result.cov_params(), expected, rtol=1e-10)
    assert model.result.use_t is False
