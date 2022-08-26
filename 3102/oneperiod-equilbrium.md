---
title: One Period Equilibrium
parent: 3102 Notes
grand_parent: Teaching
layout: post
toc: true
nav_order: 6
last_modified_date: 2022-08-23
---


## The Representative Consumer

Representative Consumer (Representative Household)

Any constrained optimization problem has a set of choice variables, constraints which limit what values those choices can take, and an optimand (the thing which is optimized).

### Choices

In the simplest version (as in ch 4,5) the representative consumer decides how much to consume $c$ and how much to work $N_{s}$ (or equivalently how much time to spend on leisure $l$)

- Consumption represents some aggregate of goods and services which are purchased
- Labor is equivalent to the total amount of time worked
- leisure is meant to represent both relaxing but also home production (any time not spent working)

### Constraints:

- time constraint - you only have so many hours in the day to allocate to labor or leisure
    - We have some variable h, representing the amount of time in the day
    - That time can be split between labor $N_{s}$ and leisure $$
    
        $$N_{s}+l=h \\ N_{s}=h-l$$
    
- Budget - Consumption is limited by disposable income
    - Most basic version: 
     
      $$\underbrace{c}_{consumption}\leq w\cdot N_{s}=\underbrace{w}_{realWage}\cdot\underbrace{(h-l)}_{laborSupplied}$$

    - More complicated version that includes government and divedends 

      $$c\leq w(h-l)+\underbrace{\pi}_{profit}-\underbrace{T}_{lumpSumTax}$$
    
    - Could also have, for example, a tax on labor: 
      
      $$c\leq w(h-l)\cdot\underbrace{(1-\tau)}_{laborTax}+\pi-T$$

- Non-negativity: can't consume or work negative amounts 
   
    $$c\geq0 \\ l\geq0 \\ N_{s}\geq0$$
    - Note that $N_{s}+l=h$, so   
    
      $$l\geq0\implies N_{s}\leq h \\ N_{s}\geq0\implies l\leq h$$

### Utility

Consumer's utility which they are trying to maximize.

$$U(c,l)$$

- For these simple models, we want a “representative consumer”, which is represented as a single agent but is meant to represent a large number of small agents. Rep Cons. is meant to represent aggregate decisions.
- To have a “representative consumer”, we need the utility function to have certain properties:
    - More (consumption and leisure) is preferred to less (U is strictly increasing). Need this to ensure budget constraint always binds.
    - The Rep. Cons. likes diversity (U is concave). This ensures a unique solution.
    - Consumption and leisure are normal goods. (The optimal $c$ and $l$ both increase when we increase income $(\pi-T+wN_{s})$)
- Another nice property: “Inada condition”
    - Marginal utility of a good is infinite if you don't have that good:

      $$\lim_{c\to0}\frac{\partial U}{\partial c}=+\infty$$
      $$\lim_{l\to0}\frac{\partial U}{\partial l}=+\infty$$

    - This isn't needed to have a representative consumer, but it makes the math easier because it makes it so the non-negativity conditions will always be non-binding.


