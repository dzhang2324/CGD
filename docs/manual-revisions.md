# Manual manuscript revisions

These edits are prepared for David to apply manually. **This document does not change prose or interpretation in Paper/main.tex.** Numerical tables, figures, and reference labels may already have changed separately. Search for the complete Find passage; line numbers can shift. Deletions are explicit.

Apply edits 1–14 and 24 first to reconcile the main paper with the verified analysis. The remaining edits address theory, literature, and supplementary analyses. Numbers come from `analysis/output/estimates.csv`; the headline effects use the specifications with claims.

## 1. Abstract: replace the two Medicaid sentences

**Find:**

```text
I then use Medicaid data from 2017--2021 to examine associations between manufacturer counts and drug spending, controlling for year and drug-name fixed effects and prescription claim volume. I find that an increase in one manufacturer for a drug is associated with a decrease of 8.7\% on total spending for a Medicaid drug.
```

**Replace with:**

```text
I then use Medicaid data from 2017--2021 to examine associations between manufacturer counts and drug spending across drug groups, controlling for year effects and prescription claim volume. One additional manufacturer is associated with 12.2\% lower spending per dosage unit and 8.7\% lower spending per claim, conditional on these controls.
```

**Why:** The new models compare drug groups rather than changes within a drug. The outcomes are now spending per dosage unit and spending per claim. These figures use 100(exp(beta)-1), from the specifications with prescription claims. This is a wording change, not an automatic replacement of the old total-spending number.

## 2. Medicaid source: distinguish rows from drugs

**Find:**

```text
The first data source that I will discuss is Medicaid - Spending by Drug. This data contains Medicaid spending by drug from 2017 to 2021, along with other covariates. It represents national-level drug spending for Medicaid covered outpatient drugs, which are paid for by state Medicaid agencies. Over-the-counter drugs in the Medicaid State Drug Utilization data are not included, and drugs with fewer than 11 claims in the most recent year are also not included. This includes 16,146 observations across 5 time periods, each of which is a particular drug/compound, with some duplicates in the case of drugs with different dosage forms, strengths, and methods of administration. For each drug, there is an entry which calculates the same features (when applicable) for all of the manufactures of that drug. In total, there are 80,730 observations when accounting for time.
```

**Replace with:**

```text
The main data source is the CMS Medicaid Spending by Drug dataset, which reports national spending on covered outpatient drugs paid for by state Medicaid agencies. The source file contains 16,146 rows, including manufacturer-specific observations and observations aggregated across all manufacturers. Reshaping its six annual measures for 2017--2021 yields 80,730 records. The empirical analysis uses the observations aggregated across manufacturers.
```

**Why:** Distinguishes source rows from drugs and from the regression sample.

## 3. Medicaid sample: explain the corrected groups and static counts

**Find:**

```text
In addition to the 16,146 total observations, each observation has a total of 36 features.
Four of the features are the brand name of the drug, the generic equivalent of that drug, the number of manufacturers for the drug, and the name of the manufacturer of the drug: these features are time-invariant during this period. 30 of the features can be divided into 6 distinct spending/financial/counting features for each year in 2017-2021, inclusive. After transforming the data, the data consists of 10 features. For the analyses in this paper, the data is filtered to consider only the entries where the statistics are calculated by aggregating all of the manufacturers for a particular drug, the outlier flag is 0, and all the other statistics are greater than 0. The 10 distinct features are described in \autoref{table:table6}; summary statistics are given in \autoref{summary:medicaid-all}, and \autoref{summary:medicaid-filtered} for the filtered data.
```

**Replace with:**

```text
I define a drug group by the combination of its reported brand name and generic name. Manufacturer count is reported once for each source row and is repeated across the five years; it is not an annual measure of entry or exit. Using brand name alone would combine some distinct generic-name groups and create artificial within-drug variation in manufacturer counts. The analysis retains aggregate observations with a zero outlier flag and positive, nonmissing manufacturer count, spending, dosage units, prescription claims, and spending per dosage unit and per claim. The resulting sample contains 12,740 observations across 3,244 drug groups. The source variables and summary statistics are reported in the data appendix.
```

**Why:** Explains the central identification correction and matches the common estimation sample. Missing source entries are not treated as observed zero spending.

## 4. Outlier flag: describe the filter actually used

**Find:**

```text
Outlier\_Flag is an indicator variable which represents if the drug is an outlier or not. A drug is labeled an outlier by the standard definition using the IQR, in addition to if it meets two other conditions. First, if there are fewer than 30 records associated with the drug from the initial data source, then it is flagged as an outlier. Second, average spending per dosage unit is calculated with and without outlier records. If these calculated amounts differ by 10 percent and \$1, then it is flagged as an outlier. The data used in this paper only includes observations for which Outlier\_Flag is 0 i.e. the observations are not outliers.
```

**Replace with:**

```text
Outlier\_Flag is a quality indicator supplied with the CMS data. I retain only observations for which this flag equals zero; I do not construct an additional outlier threshold.
```

**Why:** The old paragraph equates the flag with a generic IQR rule without demonstrating that rule. The replacement describes the implemented filter.

## 5. Empirical opening: state the comparison and the role of claims

**Find:**

```text
We now see if these theoretical conclusions hold in an empirical setting through looking at the filtered Medicaid data. To do this, we can look at the effect of the total number of manufacturers on various cost metrics within the data through two forms of linear regression: first through a naive regression with just the single feature of manufacturers and then controlling for time and entity effects, as well as demand through accounting for total claims.
```

**Replace with:**

```text
I examine whether the negative relationship between competition and prices suggested by economic theory is also present in the Medicaid spending data. The regressions compare spending across drug groups with different reported manufacturer counts, controlling for year effects. I estimate specifications both with and without log prescription claims to show how the association changes after adjusting for prescription volume. Claims measure realized utilization and do not provide an exogenous measure of demand.
```

**Why:** Removes causal language and the incorrect drug-fixed-effects description. Claims need not fully control demand.

## 6. Descriptive figure: remove the competitive-threshold claim

**Find:**

```text
The plot shows an exponentially decreasing mean average spending per dosage unit as the number of manufacturers increases. Two manufacturers have a drastic decrease in cost. The increase from 2 to 3 manufacturers results in another significant decrease, and the decrease resulting from an increase in the number of manufacturers is at best marginal for greater than 3 manufacturers. This observation could likely be explained by many other factors not related to the number of manufacturers, but is worthy to note. At face value, it illustrates a fast convergence to competitive prices with respect to the number of manufacturers: this plot suggests only more than 3 manufacturers are needed.
```

**Replace with:**

```text
The plot summarizes mean spending per dosage unit for each manufacturer count. It describes differences across drug groups, which may also differ in their ingredients, formulations, and patient populations. It therefore provides descriptive context for the regressions, rather than evidence that a particular number of manufacturers is sufficient to produce competitive prices.
```

**Why:** An unadjusted plot cannot identify a threshold of three manufacturers or establish an exponential pricing rule.

## 7. Outcomes and equation: replace the obsolete fixed-effects specification

**Status:** Applied by the author and verified November 12, 2026, including the paragraph consolidation. The Find passage below records the earlier text.

**Find:**

```text
For the regression analyses, the cost metrics we will investigate are Avg\_Spnd\_Per\_Dsg\_Unt\_Wghtd, Avg\_Spnd\_Per\_Clm, and Tot\_Spndng (average spending per dosage unit, average spending per claim, and total spending, respectively). For all of these analyses, I work with the natural logarithm of each of these variables. The total manufacturers for the drug is referred to as Tot\_Mftr. 

In general for the fixed effects regressions, I estimate the equation 

$$ Y_{it} = \beta X_{it} + \lambda_t + u_{it}$$

where $\lambda_t$ represents the time fixed effects. This is equivalent to the within estimator, which is used for the computations.
```

**Replace with:**

```text
For our regression specification, the outcomes are average spending per dosage unit and average spending per claim. For each outcome, I estimate

\[
Y_{it}=\alpha+\beta M_i+\gamma\log C_{it}+\lambda_t+u_{it},
\]
where $i$ denotes a drug group defined by brand name and generic name, $t$ denotes year, $Y_{it}$ is the natural logarithm of the spending outcome, $M_i$ is the reported manufacturer count, and $C_{it}$ is the number of prescription claims. Drugs with larger markets based on the number of prescription claims may attract more manufacturers and have different spending patterns. I include log prescription claims to adjust for differences in utilization across drug groups.

I estimate each model by unweighted pooled ordinary least squares, with and without the log-claims term. Year fixed effects $\lambda_t$ account for changes common to all drug groups, with 2017 as the reference year. Standard errors are clustered by drug group. The reported manufacturer count does not vary over time within a drug group in these data. Drug-group fixed effects would therefore absorb the manufacturer-count variable, preventing separate estimation of $\beta$. The manufacturer-count coefficient is estimated from differences across drug groups, conditional on the included controls.
```

**Why:** Specifies the four actual models, their controls, and their uncertainty estimates. The outcome is defined as log spending, and the common intercept is distinct from a drug fixed effect. A static manufacturer-count variable cannot be separately estimated alongside a full set of drug-group fixed effects.

## 8. Explain why total spending was dropped

**Find:**

```text
One possible explanation of the result in the naive regression for total spending is that drugs with a higher number of manufacturers may also have a higher number of people using that drug (higher demand), which would also increase total spending. I account for this by including the natural logarithm of the total number of claims in the regression. In general, it seems plausible that demand causes omitted variable bias in the other regressions as well, so I include it in all of the regressions.
```

**Replace with:**

```text
Total spending equals spending per claim multiplied by the number of claims. In logarithms, a total-spending regression that controls for log claims therefore repeats the manufacturer-count association in a spending-per-claim regression, apart from rounding. I report spending per claim directly and omit the redundant total-spending regression.
```

**Why:** Removes discussion of a dropped regression and explains the accounting identity verified against the data.

## 9. Results transition: do not claim bias was corrected

**Find:**

```text
As seen in the regression tables, the inclusion of fixed effects and the natural logarithm of total claims significantly changes the coefficients and $R^2$ of the regressions.
```

**Replace with:**

```text
Both spending outcomes are negatively associated with manufacturer counts. Adding prescription claims reduces the magnitude of the manufacturer-count coefficient, showing that the estimated association depends on whether prescription volume is held constant.
```

**Why:** A change in coefficients does not, by itself, establish omitted-variable bias or show that the revised estimate is causal.

## 10. Main result: spending per dosage unit

**Find:**

```text
In regression (2) for average spend per dosage unit (\autoref{table:table1}), the $R^2$ decreases to 0.127, and the adjusted $R^2$ is $0.127$. This suggests a poor fit, and that adding log(Tot\_Clms) does not add any predictive power. Regression (2) seems to indicate that when clustering standard errors to account for heteroscedasticity and autocorrelation, the number of manufacturers may not have much effect on the average spend per dosage unit. Additionally, the coefficent on Tot\_Mftr decreased in magnitude, indicating that we were able to account for some omitted variable bias from time-fixed effects and total claims. The coefficient on Tot\_Mftr indicates that the average spend per dosage unit decreases by 12.2\% on average for an increase in 1 manufacturer, holding other variables constant, although it is not significant. In general, after controlling for fixed effects, the regressions suggest that there is little to no relationship between the number of manufacturers and the average spend per dosage unit when also controlling for demand. Additionally, the coefficient on log(Tot\_Clms) shows that a 1\% increase in total claims results in a 0.03 decrease in average spend per dosage unit on average holding all else constant, which suggests that the average cost per unit of Medicaid medicines is not strongly influenced by demand.
```

**Replace with:**

```text
For spending per dosage unit (\autoref{table:table1}), the manufacturer-count coefficient is -0.186 with year controls alone and -0.130 after adding log prescription claims. In column (2), one additional manufacturer is associated with 12.2\% lower spending per dosage unit, conditional on the included controls (95\% confidence interval: 10.3\% to 14.1\% lower). The coefficient is statistically significant at the 1\% level using standard errors clustered by drug group. The negative association is consistent with the competitive mechanism discussed earlier, but it does not identify the causal effect of manufacturer entry.
```

**Why:** Replaces the old nonsignificant within-model estimate with the new cross-group result. The percentage interval is transformed from the coefficient interval.

## 11. Delete the obsolete total-spending paragraph

**Find:**

```text
In regression (3) for total spending (\autoref{table:table2}), the $R^2$ increases to 0.444, and the adjusted $R^2$ is 0.444. The coefficient on manufacturer count changes from positive in the unadjusted regression to negative in the specification with fixed effects and prescription claims, suggesting omitted-variable bias. This sign change shows that the estimated association depends on the regression specification. In the reported specification, manufacturer count has a negative coefficient of -0.091, statistically significant at the 1\% level. Conditional on prescription claim volume and the included fixed effects, more manufacturers are associated with lower total spending. This is consistent with the earlier theoretical discussion and literature which suggests that greater competition is associated with lower drug prices. However, this association does not establish a causal effect of manufacturer entry. Another thing to notice is that the coefficient on log(Tot\_Clms) suggests that when holding all else constant, the total spending can be interpreted almost entirely as a function of the total claims, since the coefficient suggests that a 1\% increase in total claims results in a 0.755\% increase in total spending on average, which is very close to a "$y = x$" line.
```

**Replace with:**

Delete this paragraph; insert no replacement text.

**Why:** The corresponding table has been removed. Do not transfer this interpretation to a different outcome. Edit 8 supplies the relevant accounting explanation.

## 12. Secondary result: spending per claim

**Find:**

```text
Looking at regression (2) for average cost per claim (\autoref{table:table3}), we can see that controlling for fixed effects lowered the $R^2$ to 0.203, and the adjusted $R^2$ is 0.202, indicating a poor fit similar to the results in \autoref{table:table1}. We may think that this regression should provide similar results to the regression for total spending with regards to fit, since the average spend per claim is simply an averaged version of total spending. However, this regression indicates that after we average the total spending by the total claims, the manufacturers and total claims provide little predictive power, indicating that there may be more relevant variables to consider. Also, we can notice that while the coefficient on Tot\_Mftr is the same as in \autoref{table:table2}, the coefficient on log(Tot\_Clms) is very small. Specifically, it indicates that a 1\% increase in total claims results in a 0.02 decrease in the average spend per claim on average, holding all else constant. This suggests that the average cost per claim of Medicaid medicines are actually quite stable, and are not strongly influenced by demand. This is a similar result to \autoref{table:table1}.
```

**Replace with:**

```text
For spending per claim (\autoref{table:table3}), the manufacturer-count coefficient is -0.170 with year controls alone and -0.091 after adding log prescription claims. In column (2), one additional manufacturer is associated with 8.7\% lower spending per claim, conditional on the included controls (95\% confidence interval: 7.3\% to 10.2\% lower). The coefficient is statistically significant at the 1\% level. The log-claims coefficients are -0.173 in the dosage-unit model and -0.245 in the per-claim model. These coefficients describe conditional associations with utilization; they do not estimate demand elasticities.
```

**Why:** Updates the secondary result and the log-log coefficients. The old discussion of fit did not establish stable prices or weak demand effects.

## 13. Medicaid limitations

**Find:**

```text
In summary, the regressions seem to confirm what we know from economic theory and the claims of several scientists from the literature. One thing to note is that the degree of generalizability of the results of the regression are likely not high. This is because the Medicaid data is not a good representation of general medicine usage patterns and costs since Medicaid serves a particular demographic of people, specifically low-income individuals, the elderly, and disabled. In other words, the Medicaid data may not be representative of the population at large, and so the conclusions from the regressions may vary with more general data. However, I do believe that these results are very applicable to Medicaid specifically.
```

**Replace with:**

```text
The negative associations are consistent with the view that competition can reduce drug prices. However, manufacturer entry may respond to market size and expected profitability, and drug groups may differ in ways that affect both entry and spending. Year controls and prescription claims do not eliminate these sources of confounding. Moreover, the reported manufacturer count is not an annual measure, so the models cannot trace price changes following entry. The results describe the Medicaid sample and may not generalize to other payers or patient populations.
```

**Why:** Explains why controls and clustering do not resolve endogenous entry or establish causal identification.

## 14. Medicaid conclusion

**Find:**

```text
The regressions from the Medicaid data do confirm Rajkumar and Kesselheim et al (2016). The number of manufacturers for a particular drug seem to have a strong relationship with the cost of the drug on average, as measured through three cost metrics in the data. These relationships stand even when controlling for fixed effects and demand for that drug, which indicates that the relationship is quite robust, and suggests a strong relationship. This helps to further confirm intuitions founded on microeconomic theory. The $R^2$ values for the regressions are not very high, which may suggest that Rajkumar and Kesselheim et al (2016) overstate the relationship between monopoly power and high drug prices. Although the generalizability outside of Medicaid is questionable, I argue that the relationship is strong and very relevant for Medicaid.
```

**Replace with:**

```text
In the Medicaid sample, drug groups with more reported manufacturers have lower spending per dosage unit and per claim, conditional on year effects and prescription volume. These patterns are consistent with competition lowering prices, but they do not establish a causal effect of manufacturer entry. The static manufacturer counts and the possibility of unobserved differences across drug groups limit that interpretation. Annual manufacturer counts and a design that separates entry from changes in market conditions would be needed to investigate the mechanism more directly.
```

**Why:** Does not use R-squared to assess causal credibility or claim to confirm review articles.

## 15. Qualify the theory prediction

**Find:**

```text
Thus, this implies that as the number of firms increases, the market price charged for a good decreases.
```

**Replace with:**

```text
This comparison motivates the expectation that greater competition can lower prices. Applying that prediction across different drugs requires caution: products, costs, and demand conditions differ, and the number of manufacturers may itself respond to market profitability.
```

**Why:** The monopoly-versus-perfect-competition benchmark does not establish a universal monotonic relationship across heterogeneous drug markets.

## 16. Correct the FDA source and percentages

**Find:**

```text
Additionally, the FDA find that drug prices decline to approximately 55\% of brand-name drug prices with 2 generic manufacturers making the product, 33\% with 5 manufacturers, and 13\% with 15 manufacturers, according to a paper released in August 2022 which attempts to quantify the savings due to the release of generic drugs.
```

**Replace with:**

```text
Using drugs with initial generic entry during 2015--2017, Conrad and Lutter (2019) report median generic average manufacturer prices approximately 54\% below the pre-entry brand price with two generic competitors and 79\% below it with four competitors. These measures describe manufacturer prices rather than prices paid directly by patients.
```

**Why:** Directly checked against the December 2019 FDA report, pages 1–2. The old sentence mixes different percentages with a 2022 date.

## 17. Add the foundational generic-entry reference

**Find:**

```text
An established literature examines generic entry and pharmaceutical pricing. Reiffen and Ward (2005) analyze the relationship between the number of generic competitors and generic drug prices. Grabowski and Vernon (1992) examine pricing strategies for branded and generic drugs following generic entry, including the role of brand loyalty.
```

**Replace with:**

```text
An established literature examines generic entry and pharmaceutical pricing. Caves, Whinston, and Hurwitz (1991) study competition surrounding patent expiration and generic entry. Reiffen and Ward (2005) examine generic-industry entry and pricing, while Grabowski and Vernon (1992) study brand loyalty and price competition after the 1984 Drug Act. Together, this literature motivates examining the relationship between manufacturer counts and spending, while recognizing that branded and generic products need not respond identically to entry.
```

**Why:** Adds the requested foundational study and distinguishes brand loyalty from the homogeneous-product benchmark. See the source notes for verification status.

## 18. Explain the mechanical Cost Plus markup relationship

**Find:**

```text
Interestingly, the coefficient on log(manuf\_cost) is negative. In particular, this indicates that for a 1\% change in manuf\_cost, markup decreases by .275\%, on average. Similarly to the first regression, the markup is quite inelastic to changes in manufacturing cost, to an even higher degree compared to the retail price. On first glance, the sign on the coefficient doesn't make sense, since we would expect that an increase in manufacturing cost should increase the markup, since the manufacturer would want to recoup more of the manufacturing cost. 

However, the first regression suggests that as the manufacturing cost increases, the retail price increases as well, although not as much as the manufacturing cost. Therefore, the manufacturing cost increases faster than the retail price on average, and so an increase in the manufacturing costs results in a decrease the markup. However, the $R^2$ is quite low for the second regression, which indicates that manufacturing costs explain little of the variance in the markup.
```

**Replace with:**

```text
The coefficient on log estimated manufacturing cost is -0.275 in the markup regression. Thus, a 1\% higher estimated cost is associated with approximately 0.275\% lower percentage markup in this sample. This relationship requires particular caution because estimated cost appears in the denominator of the constructed markup. A negative association can arise partly from that construction and should not be interpreted as an independently identified effect of production costs on pricing decisions.
```

**Why:** The markup outcome shares its construction with the explanatory variable; the old causal story overlooked this mechanical relationship.

## 19. Limit the Cost Plus appendix conclusion

**Find:**

```text
Overall, these results suggest that manufacturing costs have a small effect on the high retail prices. In particular, manufacturing costs explain very little of the variance in the markup. For the markup and retail prices, they are both relatively unresponsive to changes in the manufacturing cost. One weakness of this approach is that it does not account for the costs incurred to discover the chemical formula for the drug, which are a real part of the manufacturing costs, especially for the companies which discover and charge the retail prices. One way to interpret the markup is the extra price charged for the intellectual property rights in discovering the drug, and this is not captured solely by the costs to produce the medicine, which are significantly lower once the drug has been discovered. This is far more likely to explain the markup, but this data is unavailable.
```

**Replace with:**

```text
These regressions summarize relationships among reported prices and quantities constructed from the historical Cost Plus snapshot. The cost measure is inferred from an assumed pricing formula rather than observed in manufacturers' accounts, and the reported retail comparison may refer to a different product or price basis. The analysis therefore does not identify production costs, intellectual-property rents, or the causal contribution of either to retail prices.
```

**Why:** The snapshot does not identify R&D costs, brand rents, or actual production costs.

## 20. Cost Plus in the main conclusion

**Find:**

```text
From the analysis of the Cost Plus Drugs data, it suggests that manufacturing costs are a factor when it comes to understanding the retail (brand-name) prices. However, they explain little about the markup from the manufacturing price of the drug. Additionally, the regressions indicate that the retail price and the markup are inelastic to changes in the manufacturing cost i.e. the retail price and markup do not change much when the manufacturing cost changes. Unfortunately, there may be better indicators of what determines the retail price, but this data is not available. Also, the lack of controls for the regressions and the ambiguity of the calculation of the retail price do not make for robust results.
```

**Replace with:**

```text
The Cost Plus appendix provides a descriptive comparison of reported retail prices and estimated manufacturing costs. Its interpretation is limited by the constructed cost measure, the mechanical relationship between cost and markup, and uncertainty about the comparability of the reported prices.
```

**Why:** Aligns the main conclusion with the appendix limitations.

## 21. Shorten the full NADAC results section

**Find:**

```text
\section{Brand to Generic}
This final section will investigate differences between the NADAC of brand name drugs and their generic counterparts through a more qualitative approach. I first separate the NADAC data into drugs with no generic counterpart, and the drugs where the rate is classified as generic in the NADAC. I then plot a density histogram of the natural logarithm of the NADAC Per Unit for both groups:

\begin{figure}
    \centering
    \includegraphics[width=13cm]{Screenshot (90).png}
    \caption{Histograms of log(NADAC Per Unit) of strictly brand name and generic drugs.}
    \label{fig:nadac-distributions}
\end{figure}
\FloatBarrier

Note that the brand name drugs distribution lies farther to the right along the x-axis, which indicates that brand name drugs are priced significantly higher on average compared to generics. The brand name density is also concentrated higher at a significantly higher NADAC per unit for brand name drugs: this tells us that brand name drugs are very consistently priced at a specific high “price range”. Additionally, we can also see that where most of the generic NADAC per unit values are, the brand name drugs are sparse in that same area. The lines drawn over the histograms are kernel density estimations (KDEs) of the respective distributions. Also note the fat tails of the brand name distribution, which indicates significantly high variance compared to the relatively symmetric and approximately normal distribution of the generic NADAC.

Now we consider brand name drugs which have had a corresponding generic introduced at some point. In total, there are 1286 of these drugs after accounting for duplicates. 

\begin{table}[!htbp] \centering 
  \caption{Summary Statistics - Brand Name with Generic} 
  \label{summary:nadac-paired} 
\begin{singlespace}
\small
\begin{tabular}{@{\extracolsep{5pt}}lccccc} 
\\[-1.8ex]\hline 
\hline \\[-1.8ex] 
Statistic & \multicolumn{1}{c}{N} & \multicolumn{1}{c}{Mean} & \multicolumn{1}{c}{St. Dev.} & \multicolumn{1}{c}{Min} & \multicolumn{1}{c}{Max} \\ 
\hline \\[-1.8ex]  
NADAC per unit & 1,286 & 16.173 & 41.481 & 0.005 & 471.559 \\ 
Corresponding generic NADAC per unit & 1,286 & 4.514 & 19.310 & 0.003 & 330.858 \\ 
nadac\_diff & 1,286 & $-$11.659 & 28.786 & $-$324.811 & 2.277 \\ 
nadac\_percent\_change & 1,286 & $-$0.696 & 0.292 & $-$0.999 & 1.679 \\ 
\hline \\[-1.8ex] 
\end{tabular}
\end{singlespace} 
\end{table} 
\FloatBarrier

The nadac\_diff is calculated by taking the difference between the corresponding generic NADAC per unit and the regular NADAC per unit. nadac\_percent\_change is calculated by taking nadac\_diff and dividing it by the corresponding NADAC per unit. One thing we can immediately notice is that the NADAC per unit for most drugs significantly decreases when a generic is introduced. However, we can also see that there are some drugs which happen to experience an increase in price when the generic is introduced: in particular, one drug increases by 67\%! After filtering, there are 16 drugs which increase in price when the generic is introduced, with no obvious reason why. We can look at the summary statistics of these drugs:

\begin{table}[!htbp] \centering 
  \caption{Summary Statistics - Generic is More Expensive} 
  \label{summary:nadac-positive} 
\begin{singlespace}
\small
\begin{tabular}{@{\extracolsep{5pt}}lccccc} 
\\[-1.8ex]\hline 
\hline \\[-1.8ex] 
Statistic & \multicolumn{1}{c}{N} & \multicolumn{1}{c}{Mean} & \multicolumn{1}{c}{St. Dev.} & \multicolumn{1}{c}{Min} & \multicolumn{1}{c}{Max} \\ 
\hline \\[-1.8ex]  
NADAC per unit & 16 & 2.018 & 2.150 & 0.081 & 7.245 \\ 
Corresponding generic NADAC per unit & 16 & 2.493 & 2.257 & 0.116 & 7.686 \\ 
nadac\_diff & 16 & 0.474 & 0.656 & $-$0.027 & 2.277 \\ 
nadac\_percent\_change & 16 & 0.457 & 0.452 & 0.057 & 1.679 \\ 
\hline \\[-1.8ex] 
\end{tabular}
\end{singlespace} 
\end{table}
\FloatBarrier

For the drugs where the generic ends up more expensive, it is on average 45\% more expensive. However, since there are only 16 drugs, an increase in price in the generic is the exception rather than the rule. 

In any case, we can take a look at the distribution of the percent change:

\begin{figure}[H]
    \centering
    \includegraphics[width=13cm]{Screenshot (88).png}
    \caption{Density histogram of the percent change in NADAC}
    \label{fig:nadac-gap}
\end{figure}

We can see that a significant proportion of drugs experience an approximately 90\% decrease in NADAC per unit, comparing the brand name NADAC to the generic counterpart. This is a drastic decrease, and indicates that there is a high degree of “unnecessary” pricing when it comes to certain brand name drugs, in that the brand name drug pricing is significantly higher than what is needed to make non-zero profit. These are telltale signs of monopoly pricing, as discussed in the theoretical background section. 

In summary, the NADAC per unit of generic drugs tend to be significantly lower than those which are strictly brand name drugs. Additionally, the NADAC per unit for strictly brand name drugs has very high variance, while the NADAC per unit for generic drugs has much more normal variance. For the drugs which have a generic counterpart introduced at some point, a significant proportion of the drugs experience at least an 80\% decrease in the NADAC per unit and the vast majority of the drugs experience a decrease in the NADAC in general. A select few end up experiencing an increase in the NADAC per unit when the generic is introduced, but this is a very small proportion and may be a result of confounding factors which have to do with the specific circumstances of those drugs. Most importantly, these results line up with many of the claims in the literature, that the introduction of generic drugs results in a significant decrease in the cost that consumers face. Unfortunately, this analysis is only for the year of 2019, and so a much more robust way of confirming this pattern of decreasing prices is to analyze this same type of data over time. Due to poor data formatting and lack of computational power, it is extraordinarily difficult to merge all of the data provided of the NADAC and analyze this over time, and so it must be taken with a grain of salt. However, there is no immediately obvious reason to believe that this relationship would not generally hold over time.
```

**Replace with:**

```text
\section{Brand and Generic Acquisition Costs}
The saved 2019 NADAC summaries show lower acquisition costs for generic drugs than for their brand-name counterparts in the recorded comparisons. These are descriptive comparisons rather than estimates of changes caused by generic entry. The reported acquisition costs do not directly measure patients' out-of-pocket payments, and price differences alone do not identify profit margins or monopoly power.
```

**Why:** Drops unsupported before/after-entry and monopoly-pricing claims. The saved notebook and paper disagree about the small higher-priced-generic subset; omit its disputed statistics while raw-data recovery is deferred. This replacement also removes the NADAC results figures and tables; their original versions remain in Git.

## 22. NADAC conclusion

**Find:**

```text
Based on a qualitative analysis of the NADAC data, we can see that brand name drugs tend to cost significantly more on average compared to strictly generic drugs. When looking at brand name drugs which have had a generic counterpart released at some point, the cost significantly decreases for the vast majority of these drugs. However, more work is needed to verify that these results hold over time.
```

**Replace with:**

```text
The saved NADAC comparisons provide descriptive context: generic acquisition costs are generally lower than their recorded brand-name counterparts. They do not establish how prices changed after entry or what patients paid.
```

**Why:** Aligns the conclusion with the shortened descriptive account.

## 23. Correct the price-determinants literature review

**Find:**

```text
On the question of what goes into pharmaceutical pricing, there is also a decent amount of literature which examines the question, but the literature mainly focuses on the value of intellectual property, risks associated with drug development, and research and development costs, such as from Kesselheim et al (2016). Interestingly, Keyhani et al (2006) also argue that there is little correlation between research and development costs and increasing pharmaceutical prices, based on analyses regarding pharmaceutical development times. Even generic alternatives to brand-names in some cases cannot serve as a baseline price: Kesselheim et al. (2016) note several instances where generic drug manufacturers raised prices suddenly and significantly. As a result, it is very hard for policymakers and purchasers to have a good understanding of what is a “fair” price for medications. Daalen et al. (2021) attempts to centralize information on determinants of drug pricing through conducting a massive literature review in order to look for papers which investigate various factors that could affect drug pricing. To paraphrase, they find a lack of quality insight into the things which could factor into drug pricing, and the lack of quality evidence around price discrepancies for drugs does not enable one to make accurate conclusions about price discrepancies. They also find that retail drug prices internationally and nationally (United States) have a particularly high variance which cannot be entirely explained by the factors examined in the papers examined. However, Daalen et al. (2016) do find that determinants which are associated with lower drug prices include higher market share of generics, government purchasing, and pricing regulation. Determinants associated with higher drug prices include higher “originators” market share, which indicates original developers of a particular drug, and markets where drug markups are more common. In short, many of the problems lie with the fact that a lot of data related to determinants of drug pricing is either hard to obtain, or the data is insufficiently clear to draw conclusions about pharmaceutical pricing.
```

**Replace with:**

```text
Pharmaceutical prices reflect several institutions and incentives beyond production costs. Kesselheim et al. (2016) review the roles of market exclusivity, competition, and the organization of purchasing in the United States. Keyhani et al. (2006) find that clinical-trial durations did not increase, and regulatory review durations decreased, among the drugs they studied; this addresses one proposed explanation for rising prices rather than establishing a general relationship between R\&D expenditure and prices. In a systematic review, Janssen Daalen et al. (2021) find associations between lower retail prices and factors including generic market share, centralized purchasing, and price regulation. They also emphasize the scarcity of evidence on net prices, which limits comparisons based on publicly reported prices.
```

**Why:** Corrects the 2016/2021 inconsistency and the first author's surname, narrows the Keyhani claim to the actual study, and distinguishes retail from net prices.

## 24. Replace the obsolete naive-regression overview

**Find:**

```text
The first two naive regressions have a negative sign on the coefficient, which is what we expect based on economic theory. In particular, an increase in one manufacturer results in an 16.9\% decrease in the average spend per dosage unit, on average; and a 15.6\% decrease in the average spend per claim. Interestingly, an increase in one manufacturer seems to result in a 16.2\% increase in total spending for a drug, as seen in the third naive regression, which seems to conflict with microeconomic theory. However, this is likely due to omitted variable bias.
```

**Replace with:**

```text
In the specifications with year controls alone, one additional manufacturer is associated with 16.9\% lower spending per dosage unit and 15.6\% lower spending per claim. Both associations are statistically significant at the 1\% level. These estimates compare different drug groups rather than measuring spending changes after a manufacturer enters a particular market.
```

**Why:** Removes the old total-spending estimate and the incorrect linear percentage conversions. The new baseline specifications include year effects.

## 25. Correct the Cost Plus observation and variable description

**Find:**

```text
This data has 442 observations, with two duplicate rows for two medications that each have two different dosage forms. This data has seven features: the medication name, brand name, dosage form, retail price, the Cost Plus price, the manufacturing cost, and the markup. Cost Plus sells only generic medication, so the medication name is the name for the generic. The retail price is the brand name price as reported by Cost Plus Drugs. According the website, this is calculated as "an average of retail prices across other pharmacies that is sourced from third-party data. This information is published at the time we add the medication so may not reflect current market prices." Therefore, some of the interpretation of this retail price must be taken with a grain of salt, but I choose to give the benefit of the doubt in this paper.
```

**Replace with:**

```text
The saved Cost Plus snapshot contains 442 observations, with distinct medication names and no duplicate medication--form pairs. The recorded variables are medication name, brand name, dosage form, reported retail comparison price, and Cost Plus price. Estimated manufacturing cost and percentage markup are derived from these prices using the formulas below. The reported retail comparison is not independently observed here, and its timing and comparability limit the interpretation of the results.
```

**Why:** The data audit finds no duplicates. Distinguishes five recorded variables from two constructed quantities and avoids treating the reported comparison as a verified transaction price.

## 26. Replace the first Cost Plus results paragraph

**Find:**

```text
With an R-squared value of .483 and highly significant coefficients, it appears that manufacturing costs explain a significant proportion of the variance of retail prices of the drugs in Cost Plus. However, one thing to note is that if medicine was priced with a lot of the costs in mind, then we should expect a coefficient that is greater than or equal to 1. However, this is not the case, and the 95\% confidence interval is far from it as well. Since the coefficient is less than 1, we can characterize this relationship as quite inelastic. In other words, the retail price doesn't change much with a change in manufacturing cost. Also, while the manufacturing costs account for almost half of the variance of the retail price, there are other highly relevant factors other than manufacturing-related costs which account for the final retail price.
```

**Replace with:**

```text
In the log--log regression, a 1\% higher estimated manufacturing cost is associated with approximately 0.721\% higher reported retail price (95\% confidence interval for the coefficient: 0.654 to 0.788). This is a descriptive elasticity across the products in the snapshot. Its magnitude need not equal one: markups, product characteristics, and the comparability of the reported prices can differ across products.
```

**Why:** Removes the unsupported restriction that the coefficient should be at least one and keeps a directly interpretable estimate rather than using R-squared as causal evidence.

## 27. Replace the long development-cost paragraph

**Find:**

```text
Lipsky and Sharp (2001) briefly outline the FDA approval process for prescription drugs, starting from preclinical testing to phases 1-4 of the FDA approval process, which takes on average around 8 to 12 years. Moore et al (2018) provide statistics for the costs of this process by looking 59 novel therapeutic drugs approved by the FDA during 2015-2016: these costs range from \$5 million to \$346.8 million, depending on the circumstances of the clinical trials and the particular drug being tested. J.A. Dimasi et al (2016) also provide estimates of total R\&D costs, pre-tax, for drugs during pre-approval, including the costs of drugs that are abandoned during testing, although these estimates have been criticized for lack of transparency and replicability. For the pre-human period, defined as discovery research and pre-clinical development, is estimated at around \$1098 million capitalized (2013 dollars, \$430 million out-of-pocket), and they estimate total costs as the costs of everything up until marketing and selling the drug, which they estimate as \$2558 million capitalized (2013 dollars, \$1395 million out of pocket). Mulcahy and Kareddy (2022) also provide a brief outline of a general supply chain model for brand-name drugs at retail pharmacies:
```

**Replace with:**

```text
Moore et al. (2018) estimate the costs of 138 pivotal efficacy trials supporting 59 novel therapeutic agents approved by the FDA in 2015--2016. The median estimated trial cost was \$19 million. These are trial costs rather than total drug-development costs. DiMasi et al. (2016) estimate average pre-approval development costs per approved compound of \$1,395 million in cash outlays and \$2,558 million after capitalizing those costs, in 2013 dollars. Their calculation also allocates costs from unsuccessful compounds. These measures of development expenditure are distinct from the unit production costs considered in the Cost Plus appendix. Mulcahy and Kareddy (2022) describe how manufacturers, distributors, pharmacies, and payers interact in the prescription drug supply chain:
```

**Why:** Corrects the unit of observation and cost concepts, removes the unverified approval-duration and pre-human-cost details, and preserves the introduction to the following supply-chain figure.

## 28. Reframe the opening of the Medicaid section

**Find:**

```text
As alluded to in the literature review, several scientists have suggested that monopoly power is a primary cause of high pharmaceutical costs. In this section, I outline the results of empirically investigating these claims from looking at the Medicaid - Spending by Drug data.
```

**Replace with:**

```text
This section examines the association between reported manufacturer counts and spending in the Medicaid data. Economic theory and evidence on generic entry motivate an expected negative association, while the observational design limits conclusions about the causal role of competition.
```

**Why:** Avoids claiming that the design directly tests whether monopoly power causes high drug prices.

## 29. Describe the historical Cost Plus data professionally

**Find:**

```text
The second data source that I will discuss is the data from Mark Cuban’s Cost Plus Drugs. To obtain the data, I web scraped the website page (legally) containing a list of all medications, using Selenium and BeautifulSoup packages in Python. The features are summarized by the following tables:
```

**Replace with:**

```text
The supplementary analysis uses a historical snapshot of medication listings from Mark Cuban's Cost Plus Drugs, collected using Selenium and BeautifulSoup in Python. The variables are described in the data appendix.
```

**Why:** Removes the informal parenthetical and distinguishes the saved snapshot from a current scrape.

## Remaining manual checks

- Add the bibliography entries in `docs/literature-notes.md` and reconcile any remaining historical citations.
- After edit 21, keep the NADAC dictionary and legacy summary only if useful to the shorter account; the raw source is unavailable for verification.
- Edit 26 removes the unsupported unit-elasticity restriction from the Cost Plus discussion.
- Edit 27 replaces the R&D paragraph with verified, correctly distinguished cost concepts. See the source notes.
- Complete the result-dependent prose revisions before treating the compiled PDF as final. The table-update PDF alone is a review draft.
