---
title: Econ 330 HW2
subtitle: Monetary Policy
# parent: M&B HW
# grand_parent: Money and Banking
# great_grand_parent: Notes
layout: post
has_children: false
has_toc: false
toc: true
date: 2025-08-20
modified: 2025-08-26
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



## Data Sources:

<!-- 

https://www.federalreserve.gov/paymentsystems/master-account-and-services-database-existing-access.htm 



https://www.federalreserve.gov/paymentsystems/fednow_faq.htm
https://www.plancorp.com/blog/fednow
> At its onset, only 35 institutions were participating in the FedNow service. By the start of 2024, that number has grown to 400. Participating institutions include a range of credit unions and banks across 90% of states. 
https://www.frbservices.org/financial-services/fednow/organizations
As of 20250914, 1465 banks are signed up.


https://www.federalreserve.gov/supervisionreg/state-member-banks-supervised-federal-reserve.htm
surpisingly few banks on this list... is "supervision" narrower than I thought?

Summary of economic projections:
https://fred.stlouisfed.org/release?rid=326

https://fredblog.stlouisfed.org/2024/04/rates-related-to-monetary-policy/

https://fredblog.stlouisfed.org/2025/03/breakeven-inflation/
https://fredblog.stlouisfed.org/2025/02/how-unexpected-inflation-affects-household-wealth/

Graphs of gdp per capita over time, deflated using different price indices:
https://fred.stlouisfed.org/graph/fredgraph.png?g=1MrJE&height=490
https://fred.stlouisfed.org/graph/fredgraph.png?g=1MrJX&height=490
https://fred.stlouisfed.org/graph/?g=1MrJX
https://fred.stlouisfed.org/graph/fredgraph.png?g=1MrKt&height=490
https://fred.stlouisfed.org/graph/?g=1MrKt

-->

## Problem 1: A few real-world details.

1. Where do you keep most of your money? In a savings account? checking account? etc [Max 10 words]
2. Give an example of a non-monetary asset that you own. [Max 10 words]
3. Choose a bank that you use. [Check which Federal Reserve district this bank uses for Reserve Bank Financial Services](https://www.federalreserve.gov/paymentsystems/master-account-and-services-database-existing-access.htm). Include a screenshot of the spreadsheet row in your submission.
4. [Check whether that bank is signed up for the FedNow service](https://www.frbservices.org/financial-services/fednow/organizations). Again, include a screenshot of the spreadsheet row in your submission.



If you don't have any bank accounts, just choose a existing bank at random or ask the Professor to choose one for you.

<!-- ## Context for Problem 1 -->


## Problem 2: Fed Interest Rates

1. In FRED, plot  a chart with the following data series from 2010-2025:
    - Interest on Reserve Balances ([IORB](https://fred.stlouisfed.org/series/IORB))
    - Interest on Required Reserves ([IORR](https://fred.stlouisfed.org/series/IORR))
    - Federal Funds Rate ([FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS) for monthly or [DFF](https://fred.stlouisfed.org/series/DFF) for daily)
    - and the Primary Credit Rate (i.e. the Discount Rate) ([DPCREDIT](https://fred.stlouisfed.org/series/DPCREDIT))
 IORB, IORR, the Federal  and the Primary Credit Rate (i.e. the Discount Rate) from 2010-2025
2. Why are there two separate series for interest on reserves? [Max 15 words.]
<!-- - Why is the primary credit rate set above the federal funds rate? [Max 15 words.] -->
3. Why did the Fed lower the interest rate in 2020? [Max 15 words.]
4. Why did they start raising it in 2022? [Max 15 words.]


The graph for Problem 1.1 should look something like the following:

![FRED graph of four different interest rates](https://fred.stlouisfed.org/graph/fredgraph.png?g=1MzlL&height=490)


<!-- 
https://fred.stlouisfed.org/graph/?id=IORB,IORR,DFF,DPCREDIT
https://fred.stlouisfed.org/graph/?id=FEDFUNDS,IORB,IORR,DPCREDIT
https://fred.stlouisfed.org/graph/?g=1MzlL

 -->



## Problem 3: Taylor Rule

1. Plot the inflation gap (Inflation - 2%) and output gap (Real GDP - Potential GDP) from 1990-2025.. 
2. Plot the Taylor Rule alongside the Federal Funds Rate from from 1990-2025.



###  Additional Context:


The Inflation Gap can be calculated simply by taking the inflation rate (annual % change in the price level) and subtracting 2%.

The Output gap is the difference between real (inflation-adjusted) GDP and real "potential GDP". If we express this gap in percentage terms, we get:


$$
\text{Output Gap} = {\text{Real GDP}-\text{Real Potential GDP} \over \text{Real Potential GDP}} \times 100
$$


In FRED, we can find Real GDP under the mnemonic **GDPC1**,
and we can find an estimate of potential GDP from the Congressional Budget Office under **GDPPOT**.

If we plot the inflation gap and output gap together, we'll get a graph that looks something like this:

![FRED graph of inflation gap and output gap](https://fred.stlouisfed.org/graph/fredgraph.png?g=1MzcY&height=490)


<!-- 
https://fred.stlouisfed.org/graph/?g=1Mzew
 -->

The Taylor Rule says that the Fed Funds target rate should be set according to:

$$
\text{Taylor Rule Rate} = \text{Inflation Rate} + 2\% + \frac{1}{2}\text{Inflation Gap}+\frac{1}{2}\text{Output Gap}
$$

The "Inflation Rate + 2%" at the start is a stand-in for the equilibrium fed funds rate, that is the rate of interest that will naturally make credit markets function efficiently.
The Taylor Rule says that if inflation goes up, we should raise the rates (to fight inflation), and that if GDP goes down, we should lower them (to stimulate the economy).
If you compare this rule to the actual interest rates set by the Fed, then you'll get a graph that looks something like this one:

![graph of taylor rule vs fed funds rate, from FRED](https://fred.stlouisfed.org/graph/fredgraph.png?g=1MvQU&height=490)

Your styling will look a bit different. 
(Ideally, if you're willing to put in a bit of extra work, you'll download the data as a spreadsheet and create a graph with an actually readable y-axis label.)

<!-- 
https://www.atlantafed.org/cqer/research/taylor-rule
https://fredblog.stlouisfed.org/2014/04/the-taylor-rule/

Should be use chained GDP Price index instead of PCEPI? GDPPI

https://fred.stlouisfed.org/graph/fredgraph.png?g=1MvQx&height=490

-->



<!-- 
Other notes:






UK has only inflation targeting but still had inflation
https://fred.stlouisfed.org/series/GBRCPIALLMINMEI
https://www.bankofengland.co.uk/monetary-policy/the-interest-rate-bank-rate
started raising interest rates about 6 months too late.
https://www.bankofengland.co.uk/-/media/boe/files/letter/2021/march/2021-mpc-remit-letter.pdf
They stopped measuring M2 in 2016, but they have an M4 aggregate and iirc, that didn't spike up in 2022.
So mostly contagion based for UK from what US was doing?


IMF exchange arrangements 2023
https://www.imf.org/en/Publications/Annual-Report-on-Exchange-Arrangements-and-Exchange-Restrictions/Issues/2024/12/19/Annual-Report-on-Exchange-Arrangements-and-Exchange-Restrictions-2023-541890


Also, I improvised a point in class re: should we stick to a rule.
1. Post 2008, the deviation from the Taylor rule can be rationalized as caring more about the recession fighting component.
2. Post 2008, the deviation seemed to have been the right call.
3. Post 2020, it's hard to rationalize based on the rule (addendum: unrate was still high).
4. Post 2020, the deviation (based on fears that we would have another dip and belief that inflation was "transitory") was a mistake.
so would it be better or worse to have a more rules based approach? Unclear.

What would a NGDP rule look like?
Mechanically similar to Taylor Rule?
%ΔNGDP ~ %ΔRGDP + inflation

Here is an alternate ruling using an "unemployment gap" instead of an "output gap"
Basically the same as the Taylor rule but with with a slight lag. Checks out!
https://fred.stlouisfed.org/graph/?g=1MzHG
It also makes sense why the Taylor rules doesn't include that. 
The policy would be basically the same, but with a delay. Delays are not good in responding to a crisis.

Here are a list of alternate rules to compare to Taylor rule:
https://www.federalreserve.gov/monetarypolicy/policy-rules-and-how-policymakers-use-them.htm
Not much explanation here, but the list might be instructive:
https://www.clevelandfed.org/indicators-and-data/simple-monetary-policy-rules



 -->




