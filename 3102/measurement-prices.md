---
title: Prices
subtitle: Prices, Price Indices, and Chain-Weighting
parent: Aggregate Measurement
grand_parent: Notes
layout: post
nav_order: 2
last_modified_date: 2022-08-23
---


## Price Indices

Our unit is dollars.

Problem: Dollars themselves change in value.

Solution: We need to adjust for this by using price indices. (Singular: price index)

A price index is some way of averaging out prices.

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