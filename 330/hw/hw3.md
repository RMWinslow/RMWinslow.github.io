---
title: Econ 330 HW3
# subtitle: Monetary Policy
# parent: M&B HW
# grand_parent: Money and Banking
# great_grand_parent: Notes
layout: post
has_children: false
has_toc: false
toc: true
date: 2025-09-29
modified: 2025-09-29
nav_exclude: true
---

<!-- This assignment is adapted in-part from material by Terry J. Fitzgerald. -->

This assignment is under construction.


## Instructions

Each problem in this assignment asks you to work with data and/or answer one or more reflection questions about the data.
Each chart you produce *must* be clearly labeled, self-contained, and easy to read. 
Your answers to the reflection questions should be succint and insightful. 
When writing your answers, imagine that you are preparing a report for your very busy, non-economist, manager.

You must submit one report (preferable in PDF format) to D2L, 
which contains all of your charts and your answers to the questions.
Once again, your analysis and charts must be self-contained and clearly labeled. 

You are allowed to work with others on this assignment, but:
- Be sure to include attribution at the top of your submission. If someone helped you create a document, their name should be somewhere on the document.
- Submitted work should be your own. *(Charts will naturally look similar. That’s fine.)*


## Problem 1: Velocity of Money

1. Plot the velocity of money. (Nominal GDP divided by the M2 money supply.) 1960-2025
2. Now plot the quarterly change in the velocity. (Change the units to underneath the Formula in FRED)
<!-- 3. Prior to  1990, does the velocity of money look relatively stable? [Max: 10 words.] -->
3. What happens to the velocity of money in 2020? [Max: 10 words.]
4. What does this imply for a simple quantity theory of money? [Max: 20 words.]

<!-- https://fred.stlouisfed.org/graph/?g=1MHyG -->

<!-- 
Possible future variant: redo with divisia m2 money aggregate.
https://www.centerforfinancialstability.org/amfm.php
https://www.economicforces.xyz/p/most-inflation-stories-dont-add-up
> Long-time readers will recall that I argued that inflation was entirely predictable using a simple forecasting model that included only two variables: inflation and the growth rate of the money supply (as measured by Divisia M2). This forecasting model suggested that, using only data available as of the end of 2020 that we should expect rising rates of inflation throughout 2021. In addition, the model predicted, using only data through 2021 that the U.S. would experience persistently high rates of inflation throughout 2022. That model’s predictions turned out to be quite accurate, despite its simplicity.

Another nice quote.
> who is responsible for the increase in the price. The answer is clearly the consumers whose demand has risen. They are the ones who set in motion the process by which prices increased. Yet, if we were to ask meat packer-suppliers why prices have gone up, they will blame the cost of cattle. If we ask the butcher why prices have gone up, he will blame the rising prices of the meat packer-suppliers.

That substack article also has a paper I want to read about the link between fiscal policy and inflation: https://www.nber.org/papers/w31838

It links to the following article I want to read, but I can't access it without downloading the app.
https://www.economicforces.xyz/p/the-inflation-mystery-that-wasnt


https://www.economicforces.xyz/p/what-is-inflation?utm_source=publication-search
justification of viewing inflation as decline in purchasing power,
explanation of "medium of account" term,
+ argument that the monetary base actually is the important thing here
> This helps us to understand, for example, why we didn’t experience the high rates of inflation that were predicted following the Fed’s large expansion of its balance sheet in the aftermath of the financial crisis. The Federal Reserve expanded its balance sheet while also paying interest on reserves. This payment of interest on reserves increased the demand for reserves at precisely the same time that it was creating reserves. Supply increases. Demand increases. Those two effects offset one another.
+ defense of money multiplier ( see comments ) 
( excess demand for base money -> declining money multiplier -> decline in M2? )


Here's another great article:
https://www.economicforces.xyz/p/central-banks-and-fiscal-policy?utm_source=publication-search
"Some people might talk about central banking in terms of the interest rate or the money supply or the inflation rate, but fundamentally, it is about the supply and demand for liquidity."

https://www.economicforces.xyz/p/no-doge-checks-wouldnt-cause-inflation?utm_source=publication-search
>With that as a backdrop, we can get a sense of why people might think that a DOGE dividend would be inflationary. For example, consider the typical environment in which the government gives out checks. Ordinarily this is done during recessions or in anticipation of a coming recession. In that environment, monetary policy tends to shift towards a more expansionary stance. The mechanics of sending out checks is as follows. The U.S. Treasury department issues bonds. The proceeds of those bonds are used to give out checks to the American taxpayer. The Federal Reserve, in its expansionary stance, is purchasing U.S. Treasury securities on the open market. As a result, what is effectively happening is that these checks are financed by an increase in base money.
> An excess supply of money manifests in higher levels of nominal spending. An excess demand for money results in lower levels of nominal spending. Thus, the central bank can adjust the money supply to meet money demand by targeting a stable path for nominal spending. The central bank could have a target of constant nominal spending or it could have a target of constant growth in nominal spending. For example, during the period known as the Great Moderation, nominal spending growth was remarkably constant at around 5 percent per year.



https://www.economicforces.xyz/p/what-theory-does-and-does-not-say?utm_source=publication-search
> If the growth rate of the money supply was entirely random, then firms would see an increase in the demand for their product. Unsure of whether this increase in demand was caused by an increase in the demand for their particular product or due to an increase in the money supply, firms would increase both output and prices. This would generate a negative relationship between inflation and unemployment. However, if the change in the money supply was anticipated, the policy would not be effective at reducing unemployment at all. In fact, the higher expected rate of inflation would be counterproductive.
> This point was especially important given the evidence. The early, robust negative empirical relationship between inflation and unemployment was based on sample periods in which the monetary regime was the gold standard.
 -->

## Problem 2: Monetary Policy Cycles

Download data on the Fed Funds rate and unemployment rate from 2000 onwards.
Looking at the Fed Funds rate, 
you will need to manually determine when each "easing cycle" and "tightening" cycle begins. 

1. Create a plot comparing the tightening cycles that have taken place since 2000.
    - On one axis, you should have the time since the start of tightening.
    - On the other axis, you should have the increase in fedfunds rate since the tightening began.
2. Create a similar plot for the easing cycles since 2000.
3. Compare the most recent tightening cycle to the ones that came before it. [Max: 15 words.]
3. Compare the most easing cycle to the ones that came before it. [Max: 15 words.]


## Problem 3: Interest Rates



1. Plot the Federal Funds rate, the interest rate on 2-year treasury securities (DGS2), and 10-year treasury securities (DGS10). 2000-2025
2. Plot the "real interest rate" by combining date on inflation expectations (EXPINF2YR) and nominal interest rates (DGS2). 2000-2025


<!-- 
Real interest rate
https://fredblog.stlouisfed.org/2022/05/constructing-ex-ante-real-interest-rates-on-fred/
Fedfunds vs treasury bonds
https://fred.stlouisfed.org/graph/?g=1MHKz
inflatoin expectations:
https://fred.stlouisfed.org/release?rid=500
interest rate spreads
https://fred.stlouisfed.org/categories/33446
https://fred.stlouisfed.org/searchresults/?st=breakeven%20rate


Could do ex post inflation, but that would be complicated.
 -->



<!-- 
Something related to rates.
Ideas from Terry:
- Plot 10 yr rate minus 2 year rate for treasury constant maturity - relate spread to recessions
    - (short term reflects expected path of FFR, long term reflects long-run equilibrium)
- yield curve (125,135 in Mishkin, (ch6))
    - Relate to QE? (337, 358, 569 in Mishkin (ch14,15,22))
- bond spreads against treasuries?
- inflation expectations: breakeven inflation rates (compare nominal vs real, have students compare calculation to published rate?) (Not sure if Mishkin discusses.)

output gap vs unemployment rate (Okun's law)

Real interst rate vs durable consumption, etc.

Tightening Cycles (See Mishkin ch 25 problems for examples, or Terry's suggestion:)
- Plot cycle comparison: manually set dates for tightening cycle starts and plot increase from baseline.
    - Overlay time series with different start points (graph of increase from low point vs months since first rate hike)
- do likewise for easing cycles
- plot unemployment rate during easing cycles
    - (good observation from Terry: we'll see FFR falling when UR is high because former is response to latter)


How tight is monetary policy (Terry's suggestions):
- "Many analysts look at the median long-run federal funds rate projection from the SEP as a measure of a neutral policy stance."
- [HLW model estimates from fed](https://www.newyorkfed.org/research/policy/rstar) - compare to SEP rates.
- (My idea: redo Taylor rule with these rates?... ehh)

Tobins' Q? -->

<!-- 
This comes up when I google robins q fred
https://fred.stlouisfed.org/graph/?g=xtC

Not quite what I'm looking for though...
 -->
