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

<table>
<thead >
  <tr>
    <th></th>
    <th colspan="3"style="text-align: center;">Trillions USD</th>
    <th colspan="3" style="text-align: center;">Percent</th>
  </tr>
  <tr>
    <th></th>
    <th>2019</th>
    <th>2020</th>
    <th>2021</th>
    <th>2019</th>
    <th>2020</th>
    <th>2021</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Gross domestic product</td>
    <td>21.4</td>
    <td>20.9</td>
    <td>23.0</td>
    <td>100%</td>
    <td>100%</td>
    <td>100%</td>
  </tr>
  <tr>
    <td>Personal consumption expenditures</td>
    <td>14.4</td>
    <td>14.0</td>
    <td>15.7</td>
    <td>67.5%</td>
    <td>67.2%</td>
    <td>68.5%</td>
  </tr>
  <tr>
    <td>&emsp;Goods</td>
    <td>4.5</td>
    <td>4.7</td>
    <td>5.5</td>
    <td>21.0%</td>
    <td>22.3%</td>
    <td>23.8%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Durable goods</td>
    <td>1.5</td>
    <td>1.6</td>
    <td>2.0</td>
    <td>7.1%</td>
    <td>7.7%</td>
    <td>8.8%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Nondurable goods</td>
    <td>3.0</td>
    <td>3.0</td>
    <td>3.5</td>
    <td>13.9%</td>
    <td>14.5%</td>
    <td>15.0%</td>
  </tr>
  <tr>
    <td>&emsp;Services</td>
    <td>9.9</td>
    <td>9.4</td>
    <td>10.3</td>
    <td>46.6%</td>
    <td>45.0%</td>
    <td>44.6%</td>
  </tr>
  <tr>
    <td>Gross private domestic investment</td>
    <td>3.8</td>
    <td>3.6</td>
    <td>4.1</td>
    <td>17.9%</td>
    <td>17.4%</td>
    <td>17.9%</td>
  </tr>
  <tr>
    <td>&emsp;Fixed investment</td>
    <td>3.8</td>
    <td>3.7</td>
    <td>4.1</td>
    <td>17.6%</td>
    <td>17.7%</td>
    <td>18.0%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Nonresidential</td>
    <td>2.9</td>
    <td>2.8</td>
    <td>3.1</td>
    <td>13.7%</td>
    <td>13.4%</td>
    <td>13.3%</td>
  </tr>
  <tr>
    <td>  &emsp;&emsp;Structures</td>
    <td>0.7</td>
    <td>0.6</td>
    <td>0.6</td>
    <td>3.1%</td>
    <td>2.9%</td>
    <td>2.5%</td>
  </tr>
  <tr>
    <td>  &emsp;&emsp;Equipment</td>
    <td>1.2</td>
    <td>1.1</td>
    <td>1.3</td>
    <td>5.8%</td>
    <td>5.4%</td>
    <td>5.5%</td>
  </tr>
  <tr>
    <td>  &emsp;&emsp;Intellectual property products</td>
    <td>1.0</td>
    <td>1.1</td>
    <td>1.2</td>
    <td>4.8%</td>
    <td>5.2%</td>
    <td>5.2%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Residential</td>
    <td>0.8</td>
    <td>0.9</td>
    <td>1.1</td>
    <td>3.8%</td>
    <td>4.3%</td>
    <td>4.7%</td>
  </tr>
  <tr>
    <td>&emsp;Change in private inventories</td>
    <td>0.1</td>
    <td>-0.1</td>
    <td>0.0</td>
    <td>0.3%</td>
    <td>-0.3%</td>
    <td>-0.1%</td>
  </tr>
  <tr>
    <td>Net exports of goods and services</td>
    <td>-0.6</td>
    <td>-0.7</td>
    <td>-0.9</td>
    <td>-2.8%</td>
    <td>-3.1%</td>
    <td>-4.0%</td>
  </tr>
  <tr>
    <td>&emsp;Exports</td>
    <td>2.5</td>
    <td>2.1</td>
    <td>2.5</td>
    <td>11.8%</td>
    <td>10.2%</td>
    <td>10.8%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Goods</td>
    <td>1.6</td>
    <td>1.4</td>
    <td>1.7</td>
    <td>7.7%</td>
    <td>6.8%</td>
    <td>7.6%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Services</td>
    <td>0.9</td>
    <td>0.7</td>
    <td>0.7</td>
    <td>4.1%</td>
    <td>3.4%</td>
    <td>3.2%</td>
  </tr>
  <tr>
    <td>&emsp;Imports</td>
    <td>3.1</td>
    <td>2.8</td>
    <td>3.4</td>
    <td>14.6%</td>
    <td>13.3%</td>
    <td>14.8%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Goods</td>
    <td>2.5</td>
    <td>2.3</td>
    <td>2.8</td>
    <td>11.8%</td>
    <td>11.1%</td>
    <td>12.4%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Services</td>
    <td>0.6</td>
    <td>0.5</td>
    <td>0.5</td>
    <td>2.8%</td>
    <td>2.2%</td>
    <td>2.4%</td>
  </tr>
  <tr>
    <td>Government consumption expenditures and gross investment</td>
    <td>3.7</td>
    <td>3.9</td>
    <td>4.1</td>
    <td>17.4%</td>
    <td>18.5%</td>
    <td>17.6%</td>
  </tr>
  <tr>
    <td>&emsp;Federal</td>
    <td>1.4</td>
    <td>1.5</td>
    <td>1.6</td>
    <td>6.6%</td>
    <td>7.2%</td>
    <td>6.8%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;National defense</td>
    <td>0.8</td>
    <td>0.9</td>
    <td>0.9</td>
    <td>4.0%</td>
    <td>4.2%</td>
    <td>3.9%</td>
  </tr>
  <tr>
    <td>&emsp;&emsp;Nondefense</td>
    <td>0.6</td>
    <td>0.6</td>
    <td>0.7</td>
    <td>2.7%</td>
    <td>3.0%</td>
    <td>2.9%</td>
  </tr>
  <tr>
    <td>&emsp;State and local</td>
    <td>2.3</td>
    <td>2.4</td>
    <td>2.5</td>
    <td>10.8%</td>
    <td>11.3%</td>
    <td>10.8%</td>
  </tr>
</tbody>
</table>





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

