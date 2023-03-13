---
title: Bank Runs
subtitle: Self-Fulfilling Prophecies in the Diamond-Dybvig Model
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 601
date: 2023-03-13
---


This is a simplified description of some of the concepts from the Diamond-Dybvig model[^ddcite] of bank runs.

[^ddcite]: If you'd like to read the paper by Diamond and Dybvig, a pdf can be accessed from the [Minneapolis Fed](https://www.minneapolisfed.org/research/quarterly-review/bank-runs-deposit-insurance-and-liquidity)



## Liquidity Risk

As the consumer, you will want to consume in *either* period 1 or period 2.
And you don't know which ahead of time.

- There is an exogenous probability $t$ that you have a need for short-term liquidity. In this case, you are an early consumer, and you get utility from consuming in period 1.
- And there is a probability $(1-t)$ that you are a late consumer and get utility from consuming in period 2.

A-priori expected utility (expected utility before you know whether you'll need liquidity) is

$$\mathbb E [U] = t \cdot u(c_1) + (1-t) \cdot u(c_2)$$

where $c_1$ is the consumption you have in period 1 if you are an early consumer,
and $c_2$ is the consumption you have in period 2 if you are a late consumer.

(Here. we're assuming that each type of consumer has the same preferences over consumption; they just vary in *when* they want to consume.)

How is $(c_1,c_2)$ determined?
Let's look at two different banking technologies.




## Individual Investment

You, the consumer, have 1 dollar in the bank.
(You put it there yesterday, at time zero.)

There is an asset which gives a real return of $r > 0$ between periods 1 and 2.

In this example, the bank just directly invests your dollar in the investment asset.

Your options:

- Take the dollar out today, in period 1, and either:
    - Consume it today. $(c_1,c_2)=(1,0)$
    - Stick it under your sofa and consume it tomorrow. $(c_1,c_2)=(0,1)$
- Keep the money in the bank until tomorrow, period 2. $(c_1,c_2)=(1,1+r)$

Now, clearly, there's no reason for an early consumer to keep their money in the bank,
nor any reason for a late consumer to take their money out early.
So:

$$\mathbb E [U] = t \cdot u(1) + (1-t) \cdot u(1+r)$$

Can we do better?




## Pooled Investment

Now suppose the bank offers the following contract to depositors:

- If you withdraw early, in period 1, you get $1+r_1 > 1$
- If you withdraw late, in period 2, you get $1+r_2 < 1+r$

In other words, this contract increases your payout if you need liquidity,
but decreases your payout when you don't.
This kind of banking service can be thought of as a kind of "liquidity insurance".

Note that $0 < r_1 < r_2 < r$.

Further suppose the bank doesn't make a profit or have any transactions costs.
The bank just breaks even.
What is the budget constraint which determines the rates they can set?
Well, if some fraction $t$ withdraw early, 
then for every dollar that was deposited in period 0:

- An average of $\textcolor{#87122d}{(1+r_1)t}$ is paid out per person in period 1
- This means that only $1-\textcolor{#87122d}{(1+r_1)t}$ per person is left to invest.
- An average of $\textcolor{#113074}{(1+r_2)(1-t)}$ is paid out per person in period 2.

For the bank to break even, it must be that:

$$(1+r)\cdot(1-\textcolor{#87122d}{(1+r_1)t}) = \textcolor{#113074}{(1+r_2)(1-t)}$$

$$t\cdot(1+r_1) + (1-t)\cdot\frac{(1+r_2)}{(1+r)} = 1$$

If the bank offers a contract that satisfies this equation, 
then how does this contract compare to individual investment?
The consumer receives the same amount of money *in expectation*,
but there is less variance in how much they receive.

If the utility function is concave down (which is the case if consumers dislike risk),
then the consumer is better off, in expectation, with this contract:

$$t \cdot u(1+r_1) + (1-t) \cdot u(1+r_2) \geq t \cdot u(1) + (1-t) \cdot u(1+r)$$


### Bank Runs

This is all well and good, but this contract depends on the fact that 
only the early consumers (fraction $t$ of depositors) withdraw early.

If the late consumers also withdraw early, 
then the bank won't be able to pay everyone.
If only early consumers withdraw, then the bank pays $(1+r_1)t < 1$ per person on average.
But if everyone withdraws, then the bank pays $(1+r_1) > 1$ per person.
And the bank only has 1 dollar of assets per person!

This means there are two possible equilibria:
- If late consumers keep their money in the bank, then the optimal thing to do as a late consumer is to keep your money in the bank as well. 
- If all the other late consumers withdraw early, then the optimal thing to do is to try to withdraw early yourself. Keeping your money under the sofa isn't a *great* investment, but it's better than losing it all when the bank collapses.

The latter equilibrium is called a bank run.
It's a kind of self-fulfilling prophecy.
A bank can be in a situation where they'll be unable to give money back to depositors,
but *only if* the depositors *believe* that the bank will be unable to give the money back.


This is the reason why bank deposits are insured in the US by the Federal Deposit Insurance Corporation (FDIC).  
The idea is that even if a bank run does happen, your money will be safe,
and that knowledge itself vastly decreases the chance of a bank run happening in the first place.
(The main downside of this kind of deposit insurance is moral hazard.
Moral hazard is when the act of making a risk less dangerous
makes people more inclined to engage in risky behavior.)

<!--
All the member banks pay money to the FDIC, and when a bank fails because of a bank run, the FDIC steps in to take over [add more details here]
-->
