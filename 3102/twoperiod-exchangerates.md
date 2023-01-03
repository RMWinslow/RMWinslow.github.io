---
title: Exchange Rates
subtitle: Monetary Policy in an International Context
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 509
last_modified_date: 2022-01-01
---


## Exchange Rate Definitions

Nominal Exchange Rate
: The price of a unit of currency, measured in terms of another currency.

When you buy a loaf of bread, the price of the bread is, for example, $2\frac{dollars}{loaf}$.

The store is at the same time buying dollar bills using bread, at a price of $\frac{1}{2}\frac{loafs}{dollar}$

Let's suppose that you can exchange 1 US Dollar (USD) for 7 Chinese Yuan (CNY).
This means you can buy CNY using USD at a price of $\frac{1}{7}\frac{dollars}{yuan}$, then that's the nominal exchange rate.
Likewise, when you exchange CNY for USD, you are buying dollars at a price of $7\frac{yuan}{dollar}$.

<aside>As seen here, any exchange rate can be represented by two different numbers. 
These are the same exchange from opposite sides of the transaction.
When it doubt about which way to write the number, include the units and just make sure they make sense.</aside>



Real Exchange Rate
: Exchange rate adjusted for local price differences.

If $e$ is the nominal exchange rate and $RER$ is the real exchange rate, then $RER=e\frac{P^{*}}{P}$

<!--Example - Big Mac Index: -->

Purchasing Power Parity
: PPP is the condition that the RER happens to be 1, meaning an amount of each currency that can buy the same goods is equivalent in value.

$$1=RER=e\frac{P^{*}}{P}\\P=eP^{*}$$

<aside>Confusingly, "Purchasing Power Parity" is also sometimes use to refer to the price ratio $P/P^\star$, 
which can be thought of as what the exchange rate would need to be for the condition of PPP to hold.</aside>

<!--
https://files.stlouisfed.org/files/htdocs/publications/review/03/11/pakko.pdf
https://www.economist.com/big-mac-index
https://data.oecd.org/conversion/purchasing-power-parities-ppp.htm#indicator-chart
-->



### Example 1: The Big Mac Index

Prices indices can be rather abstract. To make things concrete, let’s use the Economist's [Big Mac index](https://www.economist.com/big-mac-index). 
It’s a  (rather silly) price index where the bundle of goods is simply a single Big Mac sandwich from McDonald's.

According to the page linked above, in June 2022:

- A Big Mac in the United States cost 5.15 USD
- A near-identical sandwich in China cost 24.00 CNY
- The nominal exchange rate was 6.75 CNY per USD (or equivalently $\frac{1}{6.75}\approx 0.15$ USD per CNY)

Plugging these numbers in, we get

$$RER=e\cdot\frac{P^{*}}{P} = e\cdot\frac{24.00\ CNY}{5.15\ USD}$$

Note that it would be a mistake to plug in 6.75 for our nominal exchange rate if we’re using the US price as our
domestic price index. Take note of the units on the second fraction. We want the units to cancel out, which means
we need CNY in the denominator of the exchange rate.


$$\begin{aligned}
RER &= e\cdot\frac{P^{*}}{P} = \frac{1\ USD}{6.75\ CNY}\cdot\frac{24.00\ CNY}{5.15\ USD} \\
&= \frac{1\ USD}{6.75\ CNY}\cdot\frac{24.00\ CNY}{5.15\ USD}\\
&= \frac{1}{6.75}\cdot\frac{24.00}{5.15} \approx 0.69\\
\end{aligned}$$


So that means that Big Macs in China are in some sense only 69 percent as expensive as Big Macs in the US.

So here's a brilliant business idea: 
Travel to China, trade 1000 USD for 6750 CNY, 
use that to buy 281 Big Macs, 
bring them back to the US, sell them for 5 USD each.
Voila! You've made 1405 USD. That's 400 dollars of profit!

Genius, right? Well, no, not really.

You can probably think of several reasons why this scheme wouldn't actually work.
Some people genuinely do make money from arbitrage, but there are costs in transporting goods from one place to another that prevent prices from completely equalizing, even after accounting for exchange rates.

<aside>
Incidentally, a man named Charles Ponzi once came up with a similar idea when he noticed that stamps were cheaper in Europe. He quickly realized that his arbitrage plan wasn't logistically feasible, <a href="http://users.econ.umn.edu/~tkehoe/classes/Ponzi.pdf">and decided to just scam his investors instead</a>.
</aside>


## Example 2: More realistic numbers

Using [data from the OECD](https://data.oecd.org/conversion/purchasing-power-parities-ppp.htm#indicator-chart), we know that in 2021, 

$$\frac{P^\star}{P} = 4.187 \frac{CNY}{USD}$$

On the same page, there’s a tab for (Nominal) Exchange Rates. The number given is $6.449 \frac{CNY}{USD}$,
but remember,
we need the units to cancel, so we flip it to get

$$e = \frac{1}{6.449} \frac{CNY}{USD}$$

The the Real Exchange Rate is

$$RER = e\cdot\frac{P^{*}}{P} = \frac{1\ USD}{6.449\ CNY}\cdot\frac{4.187\ CNY}{1\ USD} = 0.649$$



## Exchange Rate Regimes

In our model, if PPP holds, $M_{d}=PL=eP^{\star}L$

- Floating/Flexible Exchange Rate: Don't worry about it. Let the exchange rate move up and down in response to market forces.
    - Use monetary policy to adjust the $M_{s}$ to keep $P$ stable (and to counteract business cycle shocks).
        - If a shock increase $P$, (by decrease liquidity demand), decrease the money supply
        - If a shock decreases $P$, (by increasing liquidity demand), increase the money supply
    - Don't use monetary policy to influence the exchange rate:
        - If a shock increases $P^{\star}$, then don't respond. Keep $P$ stable, which means (assuming PPP holds, so $P=eP^{\star}$), the exchange rate must fall.
        - If a shock decreases $P^{\star}$, then don't respond. Keep $P$ stable, which means (assuming PPP holds, so $P=eP^{\star}$), the exchange rate must rise.
- Fixed Exchange Rate: 
    - Use monetary policy to keep the nominal exchange rate e stable
        - If $P$ changes but $P^{\star}$ does not, we can't stabilize $P$ because that would change $e$.
    - But this means that your domestic price level is now exposed to shocks to the foreign price level.
        - If a shock increases $P^{\star}$, then (assuming PPP holds, so $P=eP^{\star}$), the domestic price level $P$ must also increase.
        - If a shock decreases $P^{\star}$, then (assuming PPP holds, so $P=eP^{\star}$), the domestic price level $P$ must also decrease.
- Dollarization: Use another country's currency.