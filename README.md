# Competition and Generic Drugs

The active manuscript is `Paper/main.tex`. The annotated Git tag
`baseline-before-rewrite` preserves the manuscript and PDF before the analysis
revision. The original ZIP, notebooks, R script, CSV inputs, and historical PDFs
are retained unchanged.

## Reproduce the analysis

Use Python 3.13 and the pinned environment:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m analysis.run
python -m pytest -q
```

Run commands from the repository root. The pipeline reads the three existing
CSV files under `CGPP Data/`; it does not download data or modify those inputs.
It writes `analysis/output/`, including:

- `audit.json`: source/panel comparisons, missingness, filters, identifiers,
  sample counts, dependency versions, and input SHA-256 hashes.
- `estimates.csv` and `estimates.json`: full-precision coefficients, robust
  standard errors, p-values, 95% intervals, sample sizes, and exact percentage
  changes for manufacturer-count coefficients.
- `tables/`: generated LaTeX regression and descriptive tables.
- `figures/`: reproducible plots, with their plotted means in a separate CSV.
- `drug_groups.csv`: the mapping from numeric group IDs to source names.

`python -m analysis.run --output-dir /private/tmp/cgd-reproduction` writes a
separate reproduction for comparison. Generated numerical files should be
identical under the pinned environment; PDF metadata excludes creation dates.

## Specifications and data decisions

Medicaid observations are national drug-group/year records, not patients,
manufacturers, states, or claims. A drug group is the source pair
`(Brnd_Name, Gnrc_Name)`, which is not a precise product-strength identifier.
The source has one manufacturer-count column repeated across 2017–2021.
Accordingly, the models estimate descriptive associations across drug groups;
they do not estimate within-drug manufacturer entry.

Both Medicaid log outcomes (weighted spending per dosage unit and spending per
prescription claim) use the same sample: `Mftr_Name == "Overall"`,
`Outlier_Flag == 0`, and finite, positive manufacturer counts, spending,
dosage units, prescription claims, and both spending averages. Missing values
are preserved when reshaping. The old panel is checked separately against the
historical missing-to-zero transformation. The saved sample has 12,740
observations and 3,244 drug groups.

Each outcome is regressed on manufacturer count and year indicators, first
without and then with log prescription claims. OLS is unweighted. There are no
drug fixed effects. Covariances are clustered by the brand/generic pair, with
the CR1 factor `G/(G-1) * (N-1)/(N-K)`; tests and intervals use `t(G-1)`.
The omitted year is 2017. The percentage association for one additional
manufacturer is `100 * expm1(beta)`, with confidence limits transformed in the
same way. Manufacturer entry, product mix, and prescription volume are not
exogenous, so causal interpretations are not warranted.

Cost Plus reproduces the two historical log-log regressions with HC3 standard
errors and normal-reference inference, as in the original notebook. Estimated
cost is `(CP_price - 3) / 1.15`; markup is
`100 * ((retail_price - 3) / estimated_cost - 1)`. Cost is inferred from a
pricing rule rather than independently observed, and its appearance in the
markup denominator creates a mechanical relationship. The saved 442-row
snapshot is used without re-scraping current prices.

The missing `nadac_2019.csv` was used for descriptive comparisons, not these
regressions. No NADAC statistics are newly estimated by this pipeline.
Historical source: https://data.medicaid.gov/dataset/76a1984a-6d69-5e4d-86c8-65eb31f0506d

## Build and revise the paper

LaTeX Workshop uses the existing Tectonic recipe on save. From a terminal:

```sh
cd Paper
/opt/homebrew/bin/tectonic --synctex --keep-logs main.tex
```

Tables are included from `analysis/output/tables/`; edit their generator rather
than the generated files. The current working PDF is ignored by Git; named PDF
checkpoints under `Paper/checkpoints/` are tracked.

Numerical tables and unambiguously matching numbers may be updated
automatically. Changes to prose wording or interpretation are proposed in
`docs/manual-revisions.md` for the author's manual review. Do not call an
analysis-updated PDF final while those revisions remain outstanding.
