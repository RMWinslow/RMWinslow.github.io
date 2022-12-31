---
title: Shocks in Our Two Period Economy
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 505
last_modified_date: 2022-12-30
---



## A Summary of the model from Chapter 11

<details markdown="block" open>
<summary>Definition of the Closed Economy 2-Period Competitive Equilibrium</summary>

Given the exogenous parameters $\lbrace K,h,h',z,z',G,G'\rbrace$,
a competitive equilibrium is any set of endogenous prices $\lbrace w,w',r\rbrace$ and allocations $\lbrace c,c',l,l',N_{s}=h-l,N_{s}^{'}=h'-l',N_{d},N_{d}^{\prime},I,K^{\prime},T,T^{\prime}\rbrace$ that satisfy the following conditions:

- Representative Consumer, taking prices as given, solves:

$$\max_{c,c',l,'l} \left[u(c,l)+\beta u(c',l')\right]$$

$$\begin{aligned}
\text{s.t. }\ \ \ \ & c\geq0, \ \ \ \ c'\geq0, \ \ \ \ 0\leq l \leq h, \ \ \ \ 0\leq l' \leq h' \\
& c+\frac{c'}{1+r}\leq\left[w(h-l)+\pi-T\right]+\frac{w'(h'-l')+\pi'-T'}{1+r}\\
\end{aligned}$$

- Representative Firm, taking prices as given, solves:

$$\max_{c,c',l,'l} \left[u(c,l)+\beta u(c',l')\right]$$

$$\begin{aligned}
\text{s.t. }\ \ \ \ & N_d\geq0, \ \ \ \ N_d'\geq0, \ \ \ \ K'\geq 0\\
& K' = (1-\delta)K + I\\
& \pi = zF(K,N_d) - wN_d - I\\
& \pi' = z'F(K',N_d') - w'N_d' + (1-\delta)K'
\end{aligned}$$

- Markets Clear:
  
$$\begin{aligned}
N_d &= N_s = h-l\\
N_d' &= N_s' = h'-l'\\
zF(K,N_d) &= c + G + I\\
z'F(K',N_d') K' &= c'+ G' - (1-\delta)\\
\end{aligned}$$

<!--- Profit is $\pi=Y-wN_{d}$-->

- Government Budget is balanced:

$$G+\frac{G^{\prime}}{1+r}=T+\frac{T^{\prime}}{1+r}$$

</details>


### Solving the Consumer's Problem

Characterizing Equations are:

$$MRS_{lc} = w$$

$$MRS_{l'c'} = w'$$

$$MRS_{cc'} = (1+r)$$

$$c+\frac{c^{\prime}}{(1+r)}=\left[w(h-l)+\pi-T\right]+\frac{\left[w^{\prime}(h^{\prime}-l^{\prime})+\pi^{\prime}-T^{\prime}\right]}{1+r}$$


### Solving the Firms's Problem

Characterizing Equations are:

$$MP_{N}=\frac{\partial}{\partial N_{d}}zF(K,N_{d})=w$$

$$MP_{N^{\prime}}=\frac{\partial}{\partial N_{d}^{\prime}}z'F(K',N_{d}^{\prime})=w'$$

$$r+\delta=\frac{\partial}{\partial K'}z'F(K',N_{d}^{\prime})=MP_{K^{\prime}}$$







## Determining Equilibrium

For the Labor market (N,w):

- The labor demand curve is determined by $MP_N = w$
- The labor supply curve is a bit more complicated.
    - For simplicity, we assume leisure goes down when w goes up (substitution effect is stronger), which makes the labor demand curve slope upward.
    - Note that the position of the labor supply curve is determined by the interest rate $r$. An increase in $r$ means saving is more attractive, borrowing less attractive, so the labor supply curve shifts right.
- Given any particular $r$, we get a particular labor supply curve, which gives us a particular equilibrium $w$ such that $N_d = N_s$.
- Given any particular $r$, we get a particular labor supply curve, which gives us a particular equilibrium $w$ such that $N_{d} = N_{s}$. <!--Testing a markdown rendering quirk. Are the brackets needed to prevent italics?-->

For the output market (Y,r):

- The output supply curve comes from the labor market outcome. 
    - Given $r$, some equilibrium is determined, which can be plugged into the production function to get the quantity of output supplied.
- The output demand curve comes from $Y_d(r) = c(r) + I(r) + G$. The book goes into more detail about this, but what I want students to remember is just:
    - We know from the firm's optimal investment rule that $I$ is a decreasing function of $r$.
    - A higher interest rate means the consumer will tend to save more and consume less today. So $c$ is also a decreasing function of $r$. <!--As my wife said, "when the interest rate is so high, I don't want to live; I just want to save."-->
    - Thus the quantity of output demanded decreases when the interest rate goes up. And the output demand curve is downwards sloping.

Then given exogenous parameters, there is one specific equilibrium $r$ such that the output from the labor market at this interest rate is equal to $c+I+G$







## Shocks to the 2 Period Model

- Increase in $z$:
    - $N_d$ curve shifts right.
    - At any $r$, we have higher $Y$, <!--(because of higher $z$, but also because of higher $N$)--> so $Y_s$ curve shifts right.
    - Equilibrium $r$ increases causing the $N_s$ curve to shift to the left.
    - Results: $w\uparrow$, $r\downarrow$, $Y\uparrow$, $N\uparrow?$, 
- Increase in $z'$:
    - Firms want to invest more.
    - $Y_d$ curve shifts right because of the increase in investment demand.
    - Equilibrium $r$ and equilibrium $Y$ rise.
    - As $r$ goes up, $N_s$ curve shifts right, increasing output and moving along the $Y_s$ curve until things come back into equilibrium.
    - Results: $w\downarrow$, $r\uparrow$, $Y\uparrow$, $N\uparrow$, 

<!--Increase z and z'
• Increase z and z'

– Increase in z shifts N_{d} curve and Y_{s} curve right

– Increase in z^{\prime}shifts Y_{d} curve right

– Change in equilibrium r ambiguous

∗ Amibiguous shift in the N_{s} curve

– Results: w\uparrow?, r?,Y\uparrow,N\uparrow^{*}

• In particular, an increase in z combined with a smaller increase in z'

– r goes down, which means N_{s} shifts left and w unambiguously goes up.
-->

- Increase in $K$:
    - Like the shock to $z$, shifts $N_d$ and $Y_s$ curves shift to the right.
    - $Y_d$ curve shifts left because the firm needs to invest less to meet their goals for $K'$ because they already start with lots of capital.
    - Equilibrium $r$ decreases, but the change in $Y$ is technically ambiguous.
    - The $N_s$ curve shifts left because of the change in $r$.
    - Results: $w\uparrow$, $r\downarrow$, $Y\uparrow?$, $N\uparrow?$, 
- Increase in $G$:
    - Two direct effects:
        - Increase in $G$ shifts $Y_d$ curve to the right.
        - Increase in $G$ requires higher taxes, which makes the consumer work more, shifting $N_s$ curve to the right.
    - This (non-interest-rate related) shift in the $N_s$ curve shifts the $Y_s$ curve to shift right as well.
    - The change in $r$ causes a second shift in the $N_s$ curve.
    - Like the shock to $z$, shifts $N_d$ and $Y_s$ curves shift to the right.
    - $Y_d$ curve shifts left because the firm needs to invest less to meet their goals for $K'$ because they already start with lots of capital.
    - Equilibrium $r$ decreases, but the change in $Y$ is technically ambiguous.
    - Results: $w\downarrow$, $r\uparrow?$, $Y\uparrow$, $N\uparrow$, 