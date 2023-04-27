---
title: Prices
subtitle: Price Adjustment, Price Indices, and Chain-Weighting
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 102
last_modified_date: 2022-09-06
---



## Real GDP

To measure aggregates, our unit is dollars.

**Problem:** Dollars themselves change in value. 
**Solution:** We need to adjust for this by using a **price index**.

Conceptually:

$$\text{Nominal GDP} = \text{The Actual Data} \approx \text{Quantities} \cdot \text{Prices}$$

$$\text{Real GDP} \approx \text{Quantities}$$

We want to find some way to cancel out the prices so we are left with just the quantities.

### The Simple Method

The simplest way to do this:

1. Choose a base year. Only use prices from this specific year
2. Use those prices for every other year. (Current Quantity) x (Base Year Price) = “Real GDP”

This method is simple, and easy to understand. 
But it can lead to problems when making comparisons over long time periods.

Most "Real" aggregate data nowadays uses *chain-weighting* (as opposed to the simpler "fixed-weighting" described above).


<hr class="pagebreak">



### The Chain Weighting Method

**Problem**: Price ratios change, which means the choice of base year matters.  
**Solution**:  Use all the base years!

This is how Real GDP is calculated in most data nowadays.

The recipe for chain weighting:
1. For each pair of years, calculate gross real gdp growth using two different 'base years'.
2. Average those growth rates to get our chain-weighted growth rate between the two years, called the “Fisher index”.
3. Choose some actual base year. Multiply or divide by our chain-weighted growth rates to get the real gdp for other years.

The Fisher index formula used for calculating chain-weighted GDP growth is

$$Q_{t}^{F}=\color{#a00}\sqrt{ 
\textcolor{#080}{
    \frac{\sum p_{t-1}q_{t}}{\sum p_{t-1}q_{t-1}}
    }
\times
\textcolor{#00d}{
    \frac{\sum p_{t}q_{t}}{\sum p_{t}q_{t-1}}}
    }$$

(Our textbook labels this $g_{c}$, while the BEA NIPA handbook labels this $Q_{t}^{F}$)

This formula says that to find the growth in real GDP between years $t-1$ and $t$, 
take the <span style="color: #a00">geometric mean</span>
of <span style="color: #080">real GDP growth calculated with year $t-1$ prices</span>
and <span style="color: #00d">real GDP growth calculated with year $t$ prices</span>.

One minor downside of chain-weighting: components don't add up to the whole. 
So if you want to calculate, eg, consumption as a percentage of GDP, 
then you need to use nominal data or data deflated with some fixed base year.



## Implicit GDP Deflator 

Once we have a time series for "Real" quantities, we can extract prices as well.

The basic idea looks like this:

$$\text{Prices} \approx \frac{\text{Quantities} \cdot \text{Prices}}{\text{Quantity}} \approx \frac{\text{Nominal GDP}}{\text{Real GDP}}$$

Multiply by 100 to put in % terms, 
and you get the price index called the implicit GDP deflator.

$$\text{Deflator}=\frac{\text{Nominal}}{\text{Real}} \times 100$$

Then to use a deflator to adjust nominal data into real data, we just rearrange the formula:

$$\text{Real}=\frac{\text{Nominal}}{\text{Deflator}} \times 100$$

This is not the only way to get aggregate prices.

<!--$$\frac{p_{t}q_{t}}{(\frac{p_{t}}{p_{0}})}=p_{0}q_{t}$$-->




<hr class="pagebreak">


## Price Indexes

In reality, there isn't one single price in the economy.
There are many thousands of different prices which are changing at different rates.


To talk about prices in the aggregate, we need some way of averaging out many different prices.
We need a "Price Index".
Because there are many different ways to average prices, there are many different price indexes in use.

- The **Implicit GDP Deflator** or **GDP Price Index** is implicitly the price index we get by averaging prices over all goods produced in the country.
- The **Personal Consumption Expenditures Price Index** averages prices only over Household purchases. <!--It can likewise be calculated as the deflator for real consumption-->
- The **Gross Domestic *Purchases* Price Index** likewise averages prices over C, I, and G, but ignores the prices of exported goods.
- The **Consumer Price Index** is a survey-based price index compiled by the BLS. Goods are weighted based on a basket of goods that reflects the consumption patterns of a "typical" household. <!--The BLS also has started compiling a chain-weighted price index since 2002-->
- The **Producer Price Index** is another BLS price index, reflecting the prices that producers face when they sell things.
- "Core" price indexes (Core PCE, Core CPI) are calculated by excluding the prices of food and energy. 
    - This is done to try to get a grasp on longer term patterns in price changes because those two types of goods have relatively volatile prices (energy especially).


### The Price Level and Inflation

When a price index represents all or most of the goods in the economy, we might call it the "Price Level".

The "Inflation Rate" is the percentage change in the price level. 
In other words, positive inflation represents an average increase in prices across the economy,
or equivalently a decrease in the average amount of goods or services that a dollar can buy.

(Change in the CPI is the measure of inflation most commonly seen in headlines.)

<!--When we talk about the "Price Level", we are talking about some average of the prices in the economy, 
based on some index of prices.-->

### Other Price Indices

While the above price indices are useful for thinking about aggregate macroeconomic phenomena,
there are also many smaller price indices that are in use.
Price indices for specific industries, specific commodities, locations, etc.

At the extreme, every household has their own consumption patterns, 
and so experiences price changes in different ways.
Measures of the overall price level in the economy won't be a perfect reflection of any individual households experiences.
But this is simply the nature of aggregate statistics.





<hr class="pagebreak">


<div>
<iframe height="420px" width="100%" src="./highcharts/data_CCPIU.html" style="border-style:hidden;"></iframe>
</div>
<a href="./highcharts/data_CCPIU.html" hidden>Standalone link.</a>



## Links

- [Article from 1995 explaining the introduction of chain-weighting](https://www.newyorkfed.org/medialibrary/media/research/current_issues/ci1-9.pdf). This article is a short, easy read, and is the best explanation of the how and why of chain-weighting that I have found.
- [Overview of CPI](https://www.bls.gov/cpi/overview.htm), [BLS Handbook on CPI](https://www.bls.gov/opub/hom/pdf/cpihom.pdf), and [BLS FAQ about CPI](https://www.bls.gov/cpi/questions-and-answers.htm)
- FRED graphs 
    - [Major price indices, base year 2012](https://fred.stlouisfed.org/graph/?g=TqIl)
    - [Major price indices, base year 1970](https://fred.stlouisfed.org/graph/?g=TqIv)
- BEA Tables and Graphs
    - [Price Indexes for Gross Domestic Product](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=4&series=q&first_year=2000&last_year=2022&scale=-99&categories=survey&thetable=)
    - [Price Indexes for Personal Consumption Expenditures by Type of Product](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=69&series=q&first_year=2000&last_year=2020&scale=-99&categories=survey&thetable=)
    - [Price Indexes for Personal Consumption Expenditures by Function](https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&select_all_years=0&nipa_table_list=73&series=q&first_year=2000&last_year=2020&scale=-99&thetable=)
- BLS Tables and Graphs
    - [12-month percentage change, Consumer Price Index, selected categories](https://www.bls.gov/charts/consumer-price-index/consumer-price-index-by-category-line-chart.htm)
    






<!--
- Graphs of US data from FRED
    - [TODO: broken graph. depicts rgdp vs cpi?](https://fred.stlouisfed.org/graph/?g=8aK#0)
    - [CPI and core CPI](https://fred.stlouisfed.org/graph/?g=8dGq)
    - [CPI GDP Deflator](https://fred.stlouisfed.org/graph/?g=TpUi)
    - [same](https://fred.stlouisfed.org/graph/?g=LcqN)

Purchasing Power of US dollar
https://fred.stlouisfed.org/series/CUUR0000SA0R#0

PCE price index inflation 
https://fred.stlouisfed.org/graph/?g=NDby

https://www.federalreservehistory.org/essays/monetary-policy

Federal Funds rates and targets
https://fred.stlouisfed.org/graph/?g=vvkN
https://www.stlouisfed.org/in-plain-english/the-fomc-conducts-monetary-policy
https://research.stlouisfed.org/publications/economic-synopses/2022/08/23/liquidity-dries-up


https://files.stlouisfed.org/files/htdocs/publications/page1-econ/2021/12/01/a-dollars-worth-inflation-is-real_TE.pdf
https://www.econlowdown.org/resource-gallery
-->


<!--
https://www.bls.gov/PPI/
https://www.bls.gov/ppi/overview.htm

water price index
https://www.nasdaq.com/solutions/nasdaq-veles-water-index

https://www.bea.gov/resources/learning-center/what-to-know-prices-inflation

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

https://www.bls.gov/cpi/additional-resources/chained-cpi-covid19-impact.htm

https://fredblog.stlouisfed.org/2023/03/the-sticky-price-consumer-price-index/
https://fredblog.stlouisfed.org/2023/03/the-differences-among-price-indexes/
https://fredblog.stlouisfed.org/2023/03/when-comparing-wages-and-worker-productivity-the-price-measure-matters/

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