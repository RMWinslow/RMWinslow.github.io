---
title: Adding Money to the Model
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 506
last_modified_date: 2022-12-30
---

<!--

Defining characteristics of money:

- Medium of exchange

- Store of value

- Unit of account

Definitions of money supply

- M0 (Monetary Base) - Currency in circulation and in reserve.

- M1 - Liquid money: Currency in circulation, transactions accounts like debit, checking

- M2 - Less liquid money: All of M1, plus less liquid accounts like savings accounts.

How does the government actually change the money supply?

- Helicopter money: Increase the money money supply by decreasing taxes or equivalently increasing transfers.

- Seignorage: Government prints money to buy stuff.

- Open market operations: Increase money supply by decreasing government debt.

-->

Putting money in our model:

- Money Demand: $M_{d}=P\cdot L(Y,R)$
    - L: Liquidity demand, amount of stuff people want to buy with money
    - L goes up when $Y$ (which is equal to GDP and income) goes up.
    - L goes down when $R$ goes up. A higher nominal interest rate is associated with a higher opportunity cost for holding money.
    - L is generally chaotic, fluctuating based on time of day, day of week, new apps, whatever.
- Money supply: By fiat.
    - The government decides how much money there is.
- If liquidity demand increases, dollars become more valuable, and prices fall.
- If liquidity demand decreases, dollars become less valuable, and prices rise.
- In the basic version of the model, shocks which change $Y$ or $r$ will change the liquidity demand and thus the equilibrium price level, but the change in price level has no effect on the markets for labor and goods, which are priced in real terms.
    - Money is "neutral" in this model.
    - "Classic dichotomy": real economy affects the nominal economy, but not vice versa.
- Note that in our model, hyperinflation doesn't cause any problems. But in the real world, we know it does.
    - Hyperinflation increases the transaction costs associated with using money
    - Inflation is also functionally a tax on people holding currency
    - Also causes problems for investment:
        - Fisher equation: $R\approx r+i$
        - But nominal interest is determined via contract, while real is the after-the-fact result.
        - So unexpectedly high inflation will lead to real returns being lower than expected (low inflation means real returns higher than expected)
    - Keep this in mind for future lectures.


