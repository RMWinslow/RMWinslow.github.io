---
title: Credit Market Imperfections
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 502
last_modified_date: 2023-03-13
---

The model we looked at in Chapter 9 predicts that it's increases in permanent income that increase consumption patterns, and a temporary increase in income will instead mostly just increase savings.

Looking at the transfer programs during the pandemic, this prediction seems to hold up in aggregate, but we know that this "Ricardian equivalence" doesn't actually *always* hold up in the real world.

In our model, we can make the timing of taxes matter by introducing credit market imperfections.


Examples of Credit market imperfections in the real world:

- The interest rate for borrowing is higher than the interest rate for lending.
- Limits on how much you can borrow, lower than what you could theoretically pay back.

And why might these kinds of imperfections exist?

- There are transactions costs in the credit market.
- Financial institutions have monopoly power which allows them to set the price of loans.
- There is asymmetric information between borrowers and lenders.




<div class="pagebreak"></div>


## Different Rates for Borrowing and Lending


<link href="https://kineticgraphs.org/css/kg.0.3.3.css" rel="stylesheet" type="text/css" />
<script src="https://kineticgraphs.org/js/kg3d.0.3.3.js"></script>
<div class="kg-container" src="./graphs/twoPeriodInterestRateSpread.yml" clearcolor="#fff0"></div>



Say that $r_{s}$ is the interest rate if you save money and $r_{b}$ is interest rate if you borrow. 

First period:

$$c+s=\left(y-T\right)$$

Second period:

$$c'=\begin{cases}
\left(y'-T'\right)+(1+r_{s})s & s\geq0\\
\left(y'-T'\right)+(1+r_{b})s & s\leq0
\end{cases}$$

Combine into intertemporal budget and the problem becomes:

$$\max_{c,c^{\prime}}u(c)+\beta u(c^{\prime})$$



$$\begin{aligned}
\text{s.t.}\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \  & c\geq0,\ \ \ c'\geq0\\
c+\frac{c^{\prime}}{(1+r_{s})}&=y+\frac{y^{\prime}}{(1+r_{s})} \text{ if }y-c\geq0 \\
c+\frac{c^{\prime}}{(1+r_{b})}&=y+\frac{y^{\prime}}{(1+r_{b})} \text{ if }y-c\leq0 \\
\end{aligned}$$

Assume that $r_{b}>r_{s}$. Then 

- If it is optimal to borrow, then the utility isoquant will be tangent to the borrowing budget constraint 
    $$MRS_{cc'}=(1+r_{b})$$

- If it is optimal to save, then the utility isoquant will be tangent to the savings budget constraint
    $$MRS_{cc'}=(1+r_{s})$$

- Third possibility is a corner case where $s=0$, both budget constraints hold, and there is no tangency condition.

Let's look at the effects of shocks to this person's income.

If you put in place a shock which doesn't change a person from borrower to lender, and this shock maintains the present value of their lifetime income (for the interest rate that they actually use), Ricardian equivalence still holds

If a shock does change a person from borrower to lender, then the analysis becomes trickier, and Ricardian equivalence will not hold.


**What happens when we decrease $T$ but hold $G$ and $G^{\prime}$ constant?**

Gov budget constraint

$$G+\frac{G^{\prime}}{1+r_{g}}=T+\frac{T^{\prime}}{1+r_{g}}$$

Assume that Gov, unlike consumers, can borrow and lend at the same rate.
For simplicity, assume that $r_{g}=r_{s}$.

$$G+\frac{G^{\prime}}{1+r_{s}}=T+\frac{T^{\prime}}{1+r_{s}}$$

Decrease taxes today by $\Delta$. To do this, we need to increase $T^{\prime}$ by $\Delta\cdot(1+r_s)$.

$$G+\frac{G^{\prime}}{1+r_{s}}=\left(T-\Delta\right)+\frac{T^{\prime}+(1+r_{s})\Delta}{1+r_{s}}$$

Consumer endowment starts $\left(y-T,y'-T'\right)$, and becomes $\left(y-T+\Delta,\ y'-T'-(1+r_{s})\Delta\right).$

- If the consumer is a saver, then nothing much changes.


$$\begin{aligned}
c+\frac{c^{\prime}}{(1+r_{s})}&=\left(y-T+\Delta\right)+\frac{\left(y^{\prime}-T^{\prime}-(1+r_{s})\Delta\right)}{(1+r_{s})}\\
&=\left(y-T\right)+\frac{\left(y^{\prime}-T^{\prime}\right)}{(1+r_{s})}
\end{aligned}$$
    

- If the consumer is a borrower, then this program increases the present value of lifetime income, and expands the set of options for the consumer
  
$$\begin{aligned}
c + \frac{c^{\prime}}{(1+r_{b})}& =\left(y-T+\Delta\right)+\frac{\left(y^{\prime}-T^{\prime}-(1+r_{s})\Delta\right)}{(1+r_{b})} \\
&=\left(y-T\right)+\frac{\left(y^{\prime}-T^{\prime}\right)}{(1+r_{b})}+\Delta-\frac{1+r_{s}}{1+r_{b}}\Delta \\
& > \left(y-T\right)+\frac{\left(y^{\prime}-T^{\prime}\right)}{(1+r_{b})} \\
\end{aligned}$$


Essentially whats happening is that the government doesn't face the same frictions as the consumer, and so can improve welfare by effectively 'borrowing for them'.





<div class="pagebreak"></div>

## Asymmetric Information

Why might borrowing and lending rates differ for consumers?

One explanation is that lending is risky. It's hard to tell who won't pay back their loans. Consider the following simple model:

- There is an equal population of savers and borrowers, and each person is saving or borrowing 1 dollar.
- There is a bank which takes deposits and issues loans over the course of two time periods
    - The bank lends at a rate $r_b$ to borrowers. So each borrower receives 1 unit from the bank in the first period and promises to pay back $(1+r_{b})$ in the second period
    - The bank takes deposits from savers and promises to pay out interest rate $r_{s}$. A saver pays 1 unit to the bank in period 1, and the bank promises to pay back $(1+r_{s})$ in the second period.
- But some of the borrowers won't pay back their loans.
    - Some fraction $\alpha$ of borrowers are good, and will actually pay back $(1+r_{b})$ in the second period.
    - The rest, a fraction $\left(1-\alpha\right)$ will pay back 0 in the next period.
    - The bank can't tell who is a good or bad borrower.
- Assume that the bank has no transaction costs and chooses interest rates so that the bank has $\pi=0$.

If the bank wants to break even, what should the relationship be between $r_{s}$ and $r_{b}$?

- First Period:
    - Revenue comes from savers. They each deposit 1 dollar.
    - Costs come borrowers. The bank gives them each 1 dollar.
    - First-period profits are $\pi_{1}=1-1=0$
- Second Period
    - Revenue now comes from the borrowers who pay back their loans. Each borrower who pays back their loans pays $(1+r_{b})$ but only $\alpha$ actually pay them back, so on average the bank gets $(1+r_{b})\alpha+0(1-\alpha)=(1+r_{b})\alpha$ per borrower
    - Costs from paying back the savers. Each saver gets paid back $1+r_{s}$
    - If bank breaks even, costs=revenue and so: 
        
        $$(1+r_{b})\alpha=(1+r_{s})\\r_{b}=\frac{(1+r_{s})}{\alpha}-1$$

The higher portion of borrowers who repay, the lower $r_{b}$ has to be compared to $r_{s}$ for the bank to break even.
If $\alpha$ is very low, meaning few borrowers repay their loans, then $r_b$ must be much higher.


<!--
- What happens if we change lenders and borrower population?

- N_{s} savers, and N_{b} borrowers. 

- First period:

- revenue: N_{s}

- costs: N_{b}

- The bank borrows to make up the difference. s_{b}=N_{s}-N_{b}

- Second period:

- Revenue: \alpha(1+r_{b})N_{b}

- Costs: (1+r_{s})\left(N_{s}-s_{b}\right)

- Break even(1+r_{b})=\frac{(1+r_{s})\left(N_{s}-s_{b}\right)}{\alpha N_{b}}

Conceptually similar in some ways to insurance markets. (Read about flood insurance if this interest you)

“Market for Lemons” - Very famous paper about bad cars driving good off the market.
-->



<div class="pagebreak"></div>

## Borrowing Limits - Collateral Constraints


<!-- <link href="https://kineticgraphs.org/css/kg.0.2.6.css" rel="stylesheet" type="text/css" /> -->
<!-- <script src="https://kineticgraphs.org/js/kg3d.0.2.6.js"></script> -->
<div class="kg-container" src="./graphs/twoPeriodCollateralConstraint.yml" clearcolor="#fff0"></div>



Another solution to information asymmetries.

You limit the amount of borrowing to the value of some tangible asset that can be taken. This limits losses for the lending institution because worst case, they can sell that asset.

Algebraically, we can represent this as a limit on borrowing:

You have some nonliquid asset worth $pH$

$$\max_{c,c'} \left[u(c)+\beta u(c')\right]$$

$$
\begin{aligned}\text{s.t. }
&\ \ \ \ c\geq0, \ \ \ \ c'\geq0\\
& c+s\leq\left(y-T\right)\\
& c'\leq\left(y'-T^{\prime}+pH\right)+(1+r)s\\
& s\geq -pH
\end{aligned}
$$

Intertemporal version:

$$\max_{c,c'} \left[u(c)+\beta u(c')\right]$$

$$
\begin{aligned}\text{s.t. }
&\ \ \ \ c\geq0, \ \ \ \ c'\geq0\\
& c+\frac{c'}{1+r}\leq\left(y-T\right)+\frac{y'-T^{\prime}+pH}{1+r}\\
& c-y+T\leq pH\\
\end{aligned}
$$

Once again Ricardian Equivalence is broken. When gov changes schedule of taxes, the desired amount of saving/borrowing will change. With this added constraint, a change in the endowment point will change the set of feasible allocations.

- People who had a binding debt limit are made better off if the government shifts the timing of taxes into the future. (Transfers today, taxes tomorrow).
- People who had a non-binding debt limit: They won't change consumption patterns and so will just save the extra money transferred to them today.


## To summarize

If the credit market has no imperfections, Gov borrowing money just means you are going to save more.

If it is more expensive for you to borrow than it is for the Gov, then the Gov can increase your options by essentially borrowing in your place, at a lower rate.

If there is a limit to how much you can borrow, then the Gov can increase your options by by essentially borrowing in your place. Your individual credit limits are limited, and so the Gov doing some of the borrowing expands the maximum you have access to today.
