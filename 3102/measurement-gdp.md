---
title: Gross Domestic Product
subtitle: GDP and Related Measurements in the National Accounts
parent: 3102 Notes
grand_parent: Teaching
layout: post
toc: true
last_modified_date: 2022-08-23
---


<!--
https://www.bea.gov/system/files/2020-04/GDP-Education-by-BEA.pdf
https://www.cia.gov/the-world-factbook/field/real-gdp-purchasing-power-parity/country-comparison
https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&nipa_table_list=289&categories=survey
-->


## What is GDP?

**Concept:** How much stuff is being made?

**Definition:** The dollar value of all final goods and services produced during a given period of time within a region’s borders.

- Dollar value: The only way we can compare and add up many thousands of different types of goods is using using the value for which they sell
    - For most goods and services, it's their market value which is counted towards the National Accounts. 
    - The BEA and other agencies have some notable exceptions, such as including the "market value" of in-kind payments. When workers are paid with a portion of the output (as is common in agriculture), these in-kind payments are never sold, but are counted towards GDP *as if* they had been sold at the same price that similar goods sell for.
    - Inventories are counted as final goods in the form of investment, and are likewise counted towards gdp at the average price at which they could sell.
- **Final** goods and services
    - We don’t include intermediate goods. (ex: We don’t count a tomato if its used in a can of tomato sauce). This avoids double counting.
- Produced within a region: GDP defines a country or region by its geographical borders. Any production that occurs physically within a country counts towards GDP.
    - By contrast, GNP (Gross National Product) defines a country or region by its people. GNP is the same as GDP except GNP that looks at goods produced by the *residents* of a region.
- within a time period


<!--
But the dollar value of some goods must be *imputed*.
A full list of imputations here
https://apps.bea.gov/iTable/iTable.cfm?reqid=19&step=3&isuri=1&nipa_table_list=289&categories=survey
he largest NIPA imputation is that made to approximate the value of the services
provided by owner-occupied housing. This imputation is made so that the treatment of
owner-occupied housing in the accounts is comparable to that for tenant-occupied
housing (which is valued by rent paid), thereby keeping GDP invariant as to whether a
house is owned or rented. In the NIPAs, the purchase of a new house (excluding the value
of the unimproved land) is treated as an investment, the ownership of the home is treated
as a productive enterprise, and a service is assumed to flow, over its economic life, from
the house to the occupant. For the homeowner, the value of this service is measured as
the income the homeowner could have received if the house had been rented to a tenant.-->

<!--https://www.cia.gov/the-world-factbook/field/real-gdp-purchasing-power-parity/country-comparison-->


## Approaches to Measuring GDP

There are three ways to measure GDP.
In theory, all three approaches should yield the same total value.

<figure markdown="block">
![An image using a bar chart to depict the equivalence of the three approaches to measuring GDP](img-gdp-three-ways.png)
<figcaption>Three ways to measure GDP. Recreation of figure 2.1 from the BEA's NIPA Handbook. GDP components not to scale.</figcaption>
</figure>



### Expenditure Approach:

Measures output by looking at where that output goes.

$$C + I + G + NX$$

- Consumption
- Investment
    - Includes inventory changes
- Government Expenditures
- Net Exports (Exports - Imports)

<!--Government investment is always counted, but where it goes in the formula varies. BEA lumps Gov consumption and invesetment together. OECD seems to seperate them. Need to double check on that before uncommenting this part.-->

#### Components of US Expenditure Approach GDP 

The following table shows the components of expenditure approach GDP for the United States in 2019
| Component| 2019 | percent | trillions |
|------------------------------------------------------------|------------|--------|------|
|     Gross domestic product                                 | 21,372,582 | 100.0% | 21.4 |
| Personal consumption expenditures                          | 14,428,676 | 67.5%  | 14.4 |
| &emsp; Goods                                                  | 4,478,918  | 21.0%  | 4.5  |
| &emsp;&emsp;      Durable goods                                        | 1,513,285  | 7.1%   | 1.5  |
| &emsp;&emsp;      Nondurable goods                                     | 2,965,633  | 13.9%  | 3.0  |
|  &emsp;   Services                                               | 9,949,758  | 46.6%  | 9.9  |
| Gross private domestic investment                          | 3,826,258  | 17.9%  | 3.8  |
|     Fixed investment                                       | 3,752,632  | 17.6%  | 3.8  |
|       Nonresidential                                       | 2,938,716  | 13.7%  | 2.9  |
|         Structures                                         | 672,634    | 3.1%   | 0.7  |
|         Equipment                                          | 1,231,319  | 5.8%   | 1.2  |
|         Intellectual property products                     | 1,034,763  | 4.8%   | 1.0  |
|       Residential                                          | 813,916    | 3.8%   | 0.8  |
|     Change in private inventories                          | 73,626     | 0.3%   | 0.1  |
| Net exports of goods and services                          | -596,263   | -2.8%  | -0.6 |
|     Exports                                                | 2,519,727  | 11.8%  | 2.5  |
|       Goods                                                | 1,641,729  | 7.7%   | 1.6  |
|       Services                                             | 877,998    | 4.1%   | 0.9  |
|     Imports                                                | 3,115,990  | 14.6%  | 3.1  |
|       Goods                                                | 2,517,913  | 11.8%  | 2.5  |
|       Services                                             | 598,077    | 2.8%   | 0.6  |
| Government consumption expenditures and   gross investment | 3,713,912  | 17.4%  | 3.7  |
|     Federal                                                | 1,414,931  | 6.6%   | 1.4  |
|       National defense                                     | 847,538    | 4.0%   | 0.8  |
|       Nondefense                                           | 567,393    | 2.7%   | 0.6  |
|     State and local                                        | 2,298,981  | 10.8%  | 2.3  |





### Value-added (or Output or Product) Approach:

Measures output by looking at where goods are coming from.

Problem: Firms know their outputs and inputs, but don’t know which outputs are final vs which are intermediate.

Solution: Inputs to a firm are always intermediate, so we can add up all the output from all firms and subtract out all
the intermediate inputs. So intermediate goods cancel out, while final goods remain uncancelled.

A firm’s value added: (That firm’s revenue, including inventory) - (That firm’s input costs of goods and services)

You can also calculate this approach simply by adding up each firm’s value-added.


### Income Approach:

Also called Gross Domestic Income

Income-expenditure identity says that aggregate income will be equal to aggregate output.

Income approach measures output by adding up all the income that happens as a result of production.

- Compensation
- Profits
- Net Taxes on production and imports
    - sales tax, VAT, for example are included
    - Personal income tax is not included because that money was already measured as part of compensation.
- Depreciation (payments to replace broken down capital)
- Net interest
    – Specifically on debt owed by firms.
- Rental income, etc

