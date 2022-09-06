---
title: Prices
subtitle: Prices, Price Indices, Price Adjustment, and Chain-Weighting
parent: Aggregate Measurement
grand_parent: Notes
layout: post
nav_order: 2
last_modified_date: 2022-09-04
---


## Price Indices

To measure aggregates, our unit is dollars.

**Problem:** Dollars themselves change in value.  
**Solution:** We need to adjust for this by using price indices. (Singular: price index)

A price index is some way of averaging out prices.


- Implicit GDP Price Deflator
    - GDP price index (differs from deflator how?)
- Gross Domestic Purchases Price Index
- Personal Consumption Expenditures Price Index
- Core PCE
- CPI
- CPI Core



Examples:
- CPI - Consumer Price Index - Build a basket of goods that reflects the “average” consumption patterns of a
household, and measure how the price of that basket changes.
- PPI - Producer Price Index - reflect the prices that producers face
- Industry specific price indexes
- Implicit GDP Deflator - Derived from cross-time GDP comparisons, and implicitly averages out all the goods produced.


## Real GDP

Conceptually:

$$\text{Nominal GDP} \approx \text{Quantity} \times \text{Price}$$

$$\text{Real GDP} \approx \text{Quantity}$$

We want to cancel out the prices so we are left just looking at quantities.

Simplest way to do this:

- Choose a base year.
    – Only use prices from this specific year
- Use those prices for every other year.
    – (Current Quantity) x (Base Year Price) = “real GDP”

$$\text{Price} = \frac{\text{Quantity} \times \text{Price}}{\text{Quantity}} \approx \frac{\text{Nominal GDP}}{\text{Real GDP}}$$

Multiply by 100 to put in % terms, and you get the implicit GDP deflator


This is not the only way to do things.


## Deflation

Basic formula:

$$\text{Real}=\frac{\text{Nominal}}{\text{Deflator}}=\frac{p_{t}q_{t}}{(\frac{p_{t}}{p_{0}})}=p_{0}q_{t}$$

Likewise,

$$\text{Deflator}=\frac{\text{Nominal}}{\text{Real}}$$




## Chain Weighting

This is how Real GDP is calculated in most data nowadays.

Most "Real" aggregate data *chain-weights* the measures of price and quantity.

**Problem**: Price ratios change, which means the choice of base year matters.  
**Solution**:  Use all the base years!

The Fisher index used for calculating chain-weighted real GDP is

$$Q_{t}^{F}=\sqrt{\frac{\sum p_{t-1}q_{t}}{\sum p_{t-1}q_{t-1}}\times\frac{\sum p_{t}q_{t}}{\sum p_{t}q_{t-1}}}$$

(Our textbook labels this $g_{c}$, while the BEA NIPA handbook labels this $Q_{t}^{F}$)
The recipe for for chain weighting:
1. Calculate gross real gdp growth in each year using two different base years
2. We average those gross growth rates to get our chain-weighted gross growth, called the “Fisher index”
3. Starting with the base year, we multiply or divide by our chain-weighted growth rates to get the real gdp for
other years.






<hr class="pagebreak">

## Links

- [Article from 1995 explaining the introduction of chain-weighting](https://www.newyorkfed.org/medialibrary/media/research/current_issues/ci1-9.pdf). This article is a short, easy read, and is the best explanation of the how and why of chain-weighting that I have found.
- [BLS Handbook on CPI](https://www.bls.gov/opub/hom/pdf/cpihom.pdf), and [BLS FAQ about CPI](https://www.bls.gov/cpi/questions-and-answers.htm)
- BEA Tables and Graphs
    - [Price Indexes for Gross Domestic Product](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=4&series=q&first_year=2000&last_year=2022&scale=-99&categories=survey&thetable=)
    - [Price Indexes for Personal Consumption Expenditures by Type of Product](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=69&series=q&first_year=2000&last_year=2020&scale=-99&categories=survey&thetable=)
    - [Price Indexes for Personal Consumption Expenditures by Function](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=73&series=q&first_year=2000&last_year=2020&scale=-99&thetable=)
- BLS Tables and Graphs
    - [12-month percentage change, Consumer Price Index, selected categories](https://www.bls.gov/charts/consumer-price-index/consumer-price-index-by-category-line-chart.htm)
    

<div>
<iframe height="400px" width="100%" src="./highcharts/data_CCPIU.html"></iframe>
</div>
<a href="./highcharts/data_CCPIU.html">Standalone link.</a>


<!--
- Graphs of US data from FRED
    - [TODO: broken graph. depicts rgdp vs cpi?](https://fred.stlouisfed.org/graph/?g=8aK#0)
    - [CPI and core CPI](https://fred.stlouisfed.org/graph/?g=8dGq)
    - [CPI GDP Deflator](https://fred.stlouisfed.org/graph/?g=TpUi)
    - [same](https://fred.stlouisfed.org/graph/?g=LcqN)
-->


<!--
https://www.bls.gov/news.release/pdf/ecopro.pdf
https://www.bls.gov/cpi/home.htm
https://www.bls.gov/opub/hom/cpi/
https://www.bea.gov/data/prices-inflation
https://www.bls.gov/mxp/
https://www.bls.gov/pPI/
https://apps.bea.gov/scb/account_articles/national/0597od/maintext.htm
https://observablehq.com/@observablehq/plot
https://github.com/observablehq/plot
https://jsfiddle.net/gh/get/library/pure/highcharts/highcharts/tree/master/samples/highcharts/demo/spline-irregular-time
https://fred.stlouisfed.org/series/WPU1173
https://fred.stlouisfed.org/graph/?id=CPIFABSL,CPIHOSSL,CPIAPPSL,CPITRNSL,CPIMEDSL,CPIRECSL,CPIEDUSL,CPIOGSSL,

https://apps.bea.gov/scb/2022/08-august/0822-gdp-economy.htm

https://research.stlouisfed.org/publications/page1-econ/2015/10/01/whats-in-your-market-basket-why-your-inflation-rate-might-differ-from-the-average/?

https://quant.stackexchange.com/questions/141/what-data-sources-are-available-online?rq=1

-->



<!--
TODO: Graphs it would be nice to have.
Multiple price indices with adjustable base year.
Price indices for specific goods.
-->

<!--
TODO: write a script to update data by pulling from BLS api
https://www.bls.gov/bls/api_features.htm
https://apps.bea.gov/API/signup/index.cfms  
-->