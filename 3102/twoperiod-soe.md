---
title: Small Open Economy
subtitle: Opening our model up to trade.
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 508
last_modified_date: 2022-01-01
---

There are two changes we make to swtich from a closed economy model to a small open economy model.
And the name of this kind of model hints at the changes we must make.

- **Small:** Assume that when individuals make intertemporal decisions, they have access to a large international market. This market is so big that the domestic economy can't affect the global $r_{w}$. Thus the real interest rate is now exogenous. (“small”) 

Open
: We add a term for net exports to the market clearing conditions and equations for output Demand.
: Domestic output supply can now be different from domestic output demand.

$Y_{d}=C(r)+I(r)+G+NX$


In other words, we are adding one constraint (fixed $r$) and simultaneously removing another (that $NX=0$).

The asset market now clears because of trade instead of price changes.

Note that the real wage $w$ is not exogenously fixed. The market clearing condition for labor doesn't change. 

<aside hidden>In many models of international trade, it's the fact that labor markets are seperate that makes countries distinct.</aside>



## A Summary of the model from Chapter 11

<details markdown="block" open>
<summary>Definition of the Small Open Economy 2-Period Model</summary>

Given the exogenous parameters $\lbrace K,h,h',z,z',G,G', \textcolor{#f00}{r_w}\rbrace$,
a competitive equilibrium is any set of endogenous prices $\lbrace w,w'\rbrace$ and allocations $\lbrace c,c',l,l',N_{s}=h-l,N_{s}^{'}=h'-l',N_{d},N_{d}^{\prime},I,K^{\prime},T,T^{\prime},\textcolor{#f00}{NX},\textcolor{#f00}{NX'}\rbrace$ that satisfy the following conditions:

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
zF(K,N_d) &= c + G + I + \textcolor{#f00}{NX}\\
z'F(K',N_d') &= c'+ G' - (1-\delta)K' + \textcolor{#f00}{NX'}\\
\end{aligned}$$

<!--- Profit is $\pi=Y-wN_{d}$-->

- Government Budget is balanced:

$$G+\frac{G^{\prime}}{1+r}=T+\frac{T^{\prime}}{1+r}$$

</details>

