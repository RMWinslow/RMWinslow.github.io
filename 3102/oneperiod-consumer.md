---
title: Representative Consumer
subtitle: The consumer in a one-period competitive equilibrium, and the labor leisure tradeoff. 
parent: Competitive Equilibrium
grand_parent: Notes
layout: post
toc: true
nav_order: 101
last_modified_date: 2022-08-23
---


<!--(Representative Household)-->

In a competitive equilibrium model, the representative consumer (also called the "representative household")
is a single agent which represents the collective behavior of of a large number of small individual households or consumers.
This representative consumer takes prices as given (because each individual consumer can't affect the price level), and chooses a level of consumption and leisure that maximizes their utility.


<details markdown="block" open>
<summary> Definition of the representative consumer's problem with lump-sum taxes
</summary>

Taking prices, profits, taxes, and time available as given $\lbrace w,\pi,T,h\rbrace$, 
the consumer chooses labor supplied, leisure and consumption $\lbrace N_{s},l,c\rbrace$  to solve:

$$\begin{aligned}
\max_{\lbrace N_{s},l,c\rbrace } & U(c,l) \\
\text{s.t. } & c\geq0,\ \ \ l\geq0,\ \ \ N_{s}\geq0 \\
& c\leq w\cdot(h-l)+\pi-T \\ 
& N_{s}=(h-l)
\end{aligned}$$

</details>





(Note that $\lbrace w,\pi,T,h\rbrace$
are “exogenous” and $\lbrace N_{s},l,c\rbrace$ are “endogenous”)

We can simplify the consumer's problem to just have $c,l$ as our endogenous variables:

$$\begin{aligned}\max_{\lbrace l,c\rbrace } & U(c,l) \\
\text{s.t. } & c\geq0,\ \ \ 0\leq l\leq h \\
& c\leq w\cdot(h-l)+\pi-T \\
\end{aligned}$$


Assuming an interior solution, the characterizing equations are:

$$c=w\cdot(h-l)+\pi-T \\ MRS=\frac{MU_{l}}{MU_{c}}=w$$









## Details about the problem.

Any constrained optimization problem has a set of choice variables, constraints which limit what values those choices can take, and an optimand (the thing which is optimized).

### Choices

In the simplest version (as in ch 4,5) the representative consumer decides how much to consume $c$ and how much to work $N_{s}$ (or equivalently how much time to spend on leisure $l$)

- Consumption represents some aggregate of goods and services which are purchased
- Labor is equivalent to the total amount of time worked
- leisure is meant to represent both relaxing but also home production (any time not spent working)

### Constraints:

- The **time constraint** - You only have so many hours in the day to allocate to labor or leisure
    - We have some variable h, representing the amount of time in the day
    - That time can be split between labor $N_{s}$ and leisure $$
    
        $$N_{s}+l=h \\ N_{s}=h-l$$
    
- The **Budget Constraint** - Consumption is limited by disposable income.
    - Most basic version: 
     
      $$\underbrace{c}_{consumption}\leq w\cdot N_{s}=\underbrace{w}_{realWage}\cdot\underbrace{(h-l)}_{laborSupplied}$$

    - A more complicated version that includes government and dividends 

      $$c\leq w(h-l)+\underbrace{\pi}_{profit}-\underbrace{T}_{lumpSumTax}$$
    
    - Could also have, for example, a tax on labor: 
      
      $$c\leq w(h-l)\cdot\underbrace{(1-\tau)}_{laborTax}+\pi-T$$

- The **Non-negativity Constraints**: You can't consume or work negative amounts.
   
    $$c\geq0 \\ l\geq0 \\ N_{s}\geq0$$

    - Note that $N_{s}+l=h$, so   
    
      $$l\geq0\implies N_{s}\leq h \\ N_{s}\geq0\implies l\leq h$$


### The Optimand (Utility)

The consumer is trying to maximize a utility function which represents their preferences.

$$U(c,l)$$

- For these simple models, we want a “representative consumer”, which is represented as a single agent but is meant to represent a large number of small agents. Rep Cons. is meant to represent aggregate decisions.
- To have a “representative consumer”, we need the utility function to have certain properties:
    - More (consumption and leisure) is preferred to less (U is strictly increasing). Need this to ensure budget constraint always binds.
    - The Rep. Cons. likes diversity (U is concave). This ensures a unique solution.
    - Consumption and leisure are normal goods. (The optimal $c$ and $l$ both increase when we increase income $(\pi-T+wN_{s})$)
- Another nice property to have: Marginal utility of a good is infinite if you don't have that good:

    $$\lim_{c\to0}\frac{\partial U}{\partial c}=+\infty$$

    $$\lim_{l\to0}\frac{\partial U}{\partial l}=+\infty$$

    - This isn't needed to have a representative consumer, but it makes the math easier because it makes it so the non-negativity conditions will always be non-binding.

<!-- “Inada condition”-->












## Example 

Example: Let $U(c,l)=\ln c+\ln l$

This utility function satisfies all all requirements for a rep. consumer problem:

$$\begin{aligned}
\max_{\lbrace l,c\rbrace } & (\ln c+\ln l) \\
\text{s.t. } & c\geq0,\ \ \ l\geq0,\ \ \ h\geq l \\
& c\leq w\cdot(h-l)+\pi-T \\
\end{aligned}$$

Assuming an interior solution, this consumer's optimum is characterized by the following:

$$MRS=\frac{MU_{l}}{MU_{c}}=\frac{\left(\frac{1}{l}\right)}{\left(\frac{1}{c}\right)}=w=MRT$$

$$c=w(h-l)+\pi-T$$

Solving this example for optimal $c$ and $l$

$$l^{*}=\frac{wh+\pi-T}{2w}$$

$$c^{*}=\frac{wh+\pi-T}{2}$$


### Examples of testing the interior solutions assumption

If $w=1$, $h=60$, $\pi=30$, $T=10$, then we have an interior solution 

$$l^{*}=\frac{60+20}{2}=40$$

$$c^{*}=\frac{60+20}{2}=40$$

If $w=0.5,h=30,\pi=30,T=10,$ if we try to plug in the above

$$l^{*}=\frac{15+20}{1}=35$$

$$c^{*}=\frac{15+20}{2}=35/2$$

So for these parameters, the assumption of an interior solution cannot be correct. 
In this particular case, the actual solution is found at the "corner" where the consumer doesn't work and only consumes their exogenous income.


### Shocks to exogenous variables

#### Lump-sum taxes goes up:

Exogenous outcome $\pi-T$ goes down, then because $l$ and $c$ are normal goods, the solution will have less of each 

$$\frac{\partial}{\partial T}l^{*}=\frac{\partial}{\partial T}\frac{wh+\pi-T}{2w}=\frac{\partial}{\partial T}\frac{-T}{2w}=\frac{-1}{2w} < 0$$

$$\frac{\partial}{\partial T}c^{*}=\frac{\partial}{\partial T}\frac{wh+\pi-T}{2}=-\frac{1}{2} < 0$$

#### Time endowment goes up:

Because $c+wl\leq wh+\pi-T$, the time endowment is like an endowment of potential income, then because $l$ and $c$ are normal goods, the optimum have more of each


#### Profits goes up:

Exogenous outcome $\pi-T$ goes up, then because l and c are normal goods, the optimum have more of each

$$\frac{\partial}{\partial\pi}l^{*}=\frac{\partial}{\partial\pi}\frac{wh+\pi-T}{2w}=\frac{1}{2w} > 0$$

$$\frac{\partial}{\partial\pi}c^{*}=\frac{\partial}{\partial\pi}\frac{wh+\pi-T}{2}=\frac{1}{2} > 0$$

#### Real wage goes up:

Because the consumer's decisions are bound by the budget constraint $c+wl\leq wh+\pi-T$, an increase in the real wage has two effects:

- Income effect: $wh$ goes up, increases potential labor income, which increases $l^{*}$ and $c^{*}$

- Substitution effect: $wl$ goes up, increasing opportunity cost of $l$ is higher, causing substitution with $l$ going down and $c$ going up

For consumption, both effects move in the same direction, so $c$ goes up when $w$ goes up.

$$\frac{\partial}{\partial w}c^{*}=\frac{\partial}{\partial w}\frac{wh+\pi-T}{2}=\frac{h}{2}$$

For leisure, when $w$ goes up, $l$ could go up or down, depending on which effect is stronger.

$$\frac{\partial}{\partial w}l^{*}=\frac{\partial}{\partial w}\frac{wh+\pi-T}{2w}$$




## A Graphical Example


<iframe height="510px" width="100%" src="./highcharts/onePeriodConsumer.html"></iframe>

[Standalone Link](https://www.rmwinslow.com/3102/highcharts/onePeriodConsumer.html)

