---
title: Econ 330 HW4
subtitle: Interest Rates
# parent: M&B HW
# grand_parent: Money and Banking
# great_grand_parent: Notes
layout: post
# has_children: false
# has_toc: false
# toc: true
# date: 2025-11-02
# modified: 2025-11-02
nav_exclude: true
---

<!-- TODO: I WANT SOME ALGEBRA -->

<!-- This assignment is adapted in-part from material by Terry J. Fitzgerald. -->

This assignment is under construction.

<!-- 
## Instructions

Each problem in this assignment asks you to work with data and/or answer one or more reflection questions about the data.
Each chart you produce *must* be clearly labeled, self-contained, and easy to read. 
Your answers to the reflection questions should be succint and insightful. 
When writing your answers, imagine that you are preparing a report for your very busy, non-economist, manager.

You must submit one report (preferable in PDF format) to D2L, 
which contains all of your charts and your answers to the questions.
Once again, your analysis and charts must be self-contained and clearly labeled. 

You are allowed to work with others on this assignment, but:
- Be sure to include attribution at the top of your submission. If someone helped you create a document, their name should be somewhere on the document.
- Submitted work should be your own. *(Charts will naturally look similar. That’s fine.)* -->


## Problem 1: 

Calculate the **Present Value**, to the nearest dollar, for each of the following cash flows.
Assume a **10% interest rate** for each.
Show your work. (The relevant formulas are in chapter 4 of Mishkin)

1. 1100 dollars next year, 1210 dollars two years from now, and 1331 dollars three years from now.
2. 7400 dollars, 21 years from now.
3. 2000 dollars every year, forever.
4. 2000 dollars every year, for 7 years

### SOLUTIONS

1. $3000


$$
PV = \frac{1100}{(1.10)^1} + \frac{1210}{(1.10)^2} + \frac{1331}{(1.10)^3}
$$

$$
PV = 1,000 + 1,000 + 1,000 = 3,000
$$


**Present Value = $3,000**

1. $1000

$$
PV = \frac{7400}{(1.10)^{21}} = \frac{7400}{7.40024994} \approx 1000
$$

(Note: I chose the numbers to make things very convenient. (1.10)^21 ≈ 7.400)


3. $20,000

Formula for perpetuity:  
$$
PV = \frac{C}{r} = \frac{2000}{0.10} = 20,000
$$

You can find this formula in the book or derive it yourself,
or you could use a spreadsheet and just add of the present value of future cash flows until things diverge.

4. $9737


Here is the full expanded version of problem #4, writing the present value of the 7-year annuity as the sum of all seven individual discounted cash flows:

$$
\begin{aligned}
PV &= \frac{2000}{(1.10)^1} + \frac{2000}{(1.10)^2} + \frac{2000}{(1.10)^3} + \frac{2000}{(1.10)^4} + \frac{2000}{(1.10)^5} + \frac{2000}{(1.10)^6} + \frac{2000}{(1.10)^7} \\
&= 2000 \times \left( \frac{1}{1.10} + \frac{1}{1.10^2} + \frac{1}{1.10^3} + \frac{1}{1.10^4} + \frac{1}{1.10^5} + \frac{1}{1.10^6} + \frac{1}{1.10^7} \right) \\
&\approx  2000 \times 4.8684 \\
&\approx 9736.8
\end{aligned}
$$




<!-- 
Sum from 1 to infinity of 1/(1+x) = 1/x if |x| < 1

Disney's Sleeping beauty bonds:
100 year maturity, 7.55% interest rate
https://www.latimes.com/archives/la-xpm-1993-07-22-fi-15802-story.html
-->


## Problem 2: 

Calculate the **Yield to Maturity** for each of the following assets.
Show your work, and verify that the present value of future payments equals the initial price you paid.

1. You pay 1000 dollars today and receive 1340 dollars six years from now.
2. You pay 1000 dollars today. You receive 100 dollars every year for the next nine years. Then ten years from now, you receive 1100 dollars.

<!-- 2. You pay 300,000 dollars today and receive 60,000 dollars every year for the next ten years. -->

### PROBLEM 2 Solutions:

1. 5%. 

YTM is value of i that solves 

$$
1000 = \frac{1340}{(1+i)^6}
$$


## Problem 3:

This goes a bit beyond what's in the book.
Suppose you have a fixed payment loan that pays C dollars each year for 30 years.
If the interest rate is i, then the present value of the cash flow from this loan is :

$$
PV = \frac{C}{(1+i)} + \frac{C}{(1+i)^2} + ... + \frac{C}{(1+i)^{30}}
$$

With a bit of algebra, we can derive a simpler form:

$$
PV=\frac{C}{i}\cdot\left(1-\frac{1}{(1+i)^{30}}\right)
$$

1. Algebraically derive the second formula from the first.
2. How much money could you borrow using a fixed payment loan with 30 annual fixed payments of 10,000 dollars each, and an interest rate of 5%. Show your work.


<!-- 2. If you borrowed 300,000 dollars via a fixed payment loan with an interest rate of 5%, what would your annual fixed payment amount be? -->

<!-- (Actual mortgages usually have monthly payments, but whatever.) -->



<!-- 
PV=\frac{C}{(1+i)}+\frac{C}{(1+i)^{2}}+...+\frac{C}{(1+i)^{30}}

(1+i)PV=C+\left[\frac{C}{(1+i)}+...+\frac{C}{(1+i)^{29}}\right]

PV+i\cdot PV=C+\left[PV-\frac{C}{(1+i)^{30}}\right]

i\cdot PV=C-\frac{C}{(1+i)^{30}}

PV=\frac{C}{i}-\frac{C}{i\cdot(1+i)^{30}}
 -->



## Problem 4:

Suppose a Discount Bond promises 2000 dollars in one year's time.
For each of the following prices for this bond, calculate the interest rate (yield to maturity):
2000 dollars, 1900 dollars, 1800 dollars, 1700 dollars, 1600 dollars.
Show your work.

## Problem 5:

Suppose the state of South Dakota reduces state taxes without reducing state spending, and has a state-level budget deficit as a result. 

In about 20-30 words, describe what this might do to the supply and demand for South Dakota Municipal bonds, and why.

Attach a sketch of this shock to your homework, ala the depictions of shocks in Mishkin ch5. (I would prefer that you insert it into your submission file, if possible.) 
What do you expect would happen to equilibrium Price, Interest Rate, and Quantity sold for this bond?

<!-- Either S increase OR supply increase + demand decrease -->



<!-- 
## Problem 5:
 I want something related to yeild curves but maybe I'll put it off to the next homework. 
 -->





<!-- 

---

## Context and answers:

TODO

TODO: Definitions of things like simple bonds, discount bonds...

simple loan
fixed payment loan (annuity / fully amortized loan)

PV = C/r - C/r * 1/ (1+r)^T
https://youtu.be/4F1J5Q3DiaI?t=3180


Coupon Bond
perpetuity
(not in book, add perpetuity with growing return
https://www.youtube.com/watch?v=4F1J5Q3DiaI
"China has been growing 10% per year for the last 15 years. That can't last forever,
or every planet in the galaxy would be speaking chinese."
)

Present Value

Yield to Maturity



Discount Bond

Mortgage

Lottery


Monthly rate conversion? 

Yield curve, 
    expectations theory
    segmented markets theory
    liquidity premium theory




-->






<!-- 

## Mishkin HW suggestions

### Chapter 4

various YTM questions
    property taxes
    perpetuity
    capital gain
    lots of stuff
Get data in 4 year auto loan, borrow 20k, pay 4 fixed payments. What will payments be?
Take a look at Treasury Inflation Indexed Securities (FRED: DGS5 vs DFII5, likewise for 7,10,20,30)
    Went negative in 2008. Why?
    My suggestion: Compare to Real interest rate calculate another way?


## LT hw Qs for this block:

### Applicable Ideas

basic vocab
ex4f07 essay question about subprime mortgage crisis (adjustable rate mortgages)
ex4f10 supply and demand shifters for bonds ←→
    wealth: D➡️, maybe S⬅️
    SEC reduces brokerage fees: D➡️, maybe S➡️
    Bernanke gives speech, expected interest rates rise: D⬅️
    higher than expected government deficit: S➡️
ex5f07 College Cost Reduction and Access Act (H.R. 2669)
ex6f06 Fannie Mae and the U.S. Housing Bubble Controversy


### Interesting, but not quite what I'm looking for here:

ex3f07 Make an appointment with your bank to ask what they do with checkable accounts funds.
ex3f06 stock return volatility
ex3f11 irrational exuberance in stock market
ex4f06 free banking era
ex4f11 mobile money (eg in kenya)
ex5f11 "End of the 30 Year Mortgage?" - Fannie May and Freddie Mac (Interesting, but multiple choice only)
ex5f10 compare and contrast DJIA, S&P 500, NASDAQ
ex6f10 EU economic integration, Schuman Declaration
ex7f06 Why is the world bank controversial?
ex7f11 Facebook business model
ex7f07 Stock Portfolio Simulation (Idea: I could have them pick some stocks for a future homework???)
ex8f10 Akerloff nobel prize essay (Lemons)
ex8f11 Eurozone Crisis
ex8f06 Stock Options for Executives




## Reed HW ideas for this block


### From Ch 5&6 Practice Assignments in main folder:

Three theories for term structure of interest rates. Expectations Theory vs Liquidity Premium Theory
Risk premium shock.


It looks like Chapter 7 is skipped, but topics are mentioned above.
Maybe the previous edition had them merged?

Chapter 9: know your bank activity looks neat

### Fall 2019 folder:

hw1 college Tutition, pay upfront or in installments
    rate of return, coupon rate, yield to maturity
hw2 Checklist of responses to high stock returns or increased interest rates
    adverse selectio vs moral hazard
    principal agent problem
hw3 bank excess reserves
    general bank balance sheet questions
    liabilities, etc.
    Riegle-Neal Act 
hw4 Choose an article from Federal reserve website and summarize
    https://www.federalreservehistory.org/topics/supervision-and-regulation
    (GREAT idea, just not what I want for this homework.)
hw5 discount loans outstanding
    interest on reserves
    open market sales
    old model of reserve requirements which I'm not sure illuminates anything...
hw6 watch fed announcement, describe actions in terms of AD/AS model


### Spring 2019 folder

hw1 capital market vs money market
    debt vs equity,
    money stocks
...
Otherwise similar to Fall 2019, just less refined, I think.


## Terry?

All his material seems monetary policy focused...


-->
