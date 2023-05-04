---
title: Business Cycles
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: false
nav_order: 105
last_modified_date: 2023-01-31
---

<!--TODO: add section on seasonal adjustment and annualization of rates-->


The Assumption is that the data can be decomposed like so:

$$\text{data} = \text{trend} + \text{seasonal} + \text{cyclical}$$

- **Trend** = smoothed out so we only see long-term patterns
- **Seasonal** component = predictable fluctations that happen on a yearly cycle
    - Examples:
        - Farming: weather affects output of crops (harvest) and determines when you want to hire labor to work on those fields
        - Holidays: People consume more at Christmas time, they consume more travel services if everyone is visiting their family at the same time, etc.
    - For annual data, seasonal adjustment doesn’t do anything.
- **Cyclical** component = The part of the data which can’t be explained by long-term patterns and which doesn’t follow some consistent predictable pattern.

## The Boom and Bust Cycle

Peak
: Economic activity reaches a high point and begins to decline.

Trough
: Economic activity reaches a low point and begins to increase again.

Recession
: Going from a Peak to a Trough. A significant drop in economic activity that affects the entire economy.

Boom/Expansion
: Going from a trough to a peak. Happens whenever there isn’t a recession.



## Additional Terms

Procyclical
: If the cyclical component of a variable is positively correlated with the cyclical component of GDP, then we say that this variable is Procyclical

Countercyclical
: If the cyclical component of a variable is negatively correlated with the cyclical component of GDP, then we say that this variable is Countercyclical

Acyclical
: If no correlation between cyclical component of a variable and the cyclical component of GDP, then the variable is Acyclical

Lagging
: Deviations from trend move with GDP but the peaks and troughs happen slightly after the peaks and troughs in GDP

Leading
: Deviations from trend move with GDP but the peaks and troughs happen slightly before the peaks and troughs in GDP

Coincident
: Deviations from trend move with GDP, but are neither leading nor lagging.



## Summary of Business Cycle Facts

|  | Cyclicality | Lead/Lag | Variation |
|:-:|:-:|:-:|:-:|
| Consumption | Procyclical | Coincident | Smaller than GDP's |
| Investment | Procyclical | Coincident | Larger than GDP's |
| Employment | Procyclical | Lagging | Smaller than GDP's |
| Real Wage | Procyclical | ? | ? |
| Average Labor Productivity | Procyclical | Coincident | Smaller than GDP's |



## Links

- [NBER Business Cycle Dating](https://www.nber.org/research/business-cycle-dating)
    - [table of dates](https://www.nber.org/research/data/us-business-cycle-expansions-and-contractions)
    - [Direct link to their graph of unemployment](https://datawrapper.dwcdn.net/7lRs9/22/).
- FRED Dashboard: [Data Considered for the NBER Turning Points](https://fredaccount.stlouisfed.org/public/dashboard/84408)
- Recession Heuristics (graph from FRED):
    - [Sahm Rule](https://fred.stlouisfed.org/series/SAHMREALTIME)
    - [Real GDP Growth](https://fred.stlouisfed.org/graph/?g=T4L8)
- Some examples of data series with clear seasonality:
    - [GDP](https://fred.stlouisfed.org/graph/?g=TU8i)
    - [Unemployment Rate](https://fred.stlouisfed.org/graph/?id=UNRATE,UNRATENSA,)
    - [CPI Prices for Apparel](https://fred.stlouisfed.org/graph/?id=CPIAPPSL,CPIAPPNS,)
    - [PPI Television Advertising Prices](https://fred.stlouisfed.org/series/WPU362)
    - [Initial Claims for Unemployment Insurance](https://fred.stlouisfed.org/graph/?id=ICSA,ICNSA,)






<!--
https://fred.stlouisfed.org/graph/?id=GDI,GDP,

http://econbrowser.com/recession-index
https://fred.stlouisfed.org/series/JHGDPBRINDX

- [Dallas Fed article on seasonal adjustment](https://www.dallasfed.org/research/basics/seasonally)
-->


<!--
FRED Recession Dashboard
https://fredblog.stlouisfed.org/2022/08/the-data-and-determinations-behind-dating-business-cycle-peaks-and-troughs/
https://fredblog.stlouisfed.org/2021/08/discrepancies-in-dating-recessions/

https://news.research.stlouisfed.org/2022/09/teaching-the-economics-of-recessions-bring-fred-into-the-classroom-september-2022/
https://en.wikipedia.org/wiki/Sahm_Rule


-->
