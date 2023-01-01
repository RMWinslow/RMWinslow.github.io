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



## Changes to The Model

There are two changes we make to switch from a closed economy model to a small open economy model.
And the name of this kind of model hints at the changes we must make.

Small
: The interest rate is exogenously equal to the world interest rate.

Open
: There is now a term for net exports in output demand.

For the economy to be **Open** means that there is international trade in goods/assets.
We represent this by adding **a term for net exports** to the equation for output demand.


$$Y_{d}=C(r)+I(r)+G+NX$$

$$Y_{d}'=c' - (1-\delta)K' + G' + NX'$$

In the model, Net exports are free floating, and can attain any value which allows output supply to equal output demand.
This also means that *domestic* output demand, defined as $C+I+G$ isn't necessarily equal to output supply in equilibrium. The difference is made up for by importing or exporting.


The economy is **Small:** in the sense that the country as a whole is a price-taker in the international market for goods and assets.
Assume that when individuals make intertemporal decisions, they have access to a large international market. 
This market is so big that the domestic economy can't affect the global interest rate $r_{w}$. 
Thus **the real interest rate is now exogenous**. 

$$r=r_{w}$$


In other words, we are adding one constraint (fixed $r$) and simultaneously removing another (that $NX=0$).

The asset market now clears because of trade instead of price changes.

Note that the real wage $w$ is not exogenously fixed. The market clearing condition for labor doesn't change. 

<aside hidden>In many models of international trade, it's the fact that labor markets are separate that makes countries distinct.</aside>


<div class="pagebreak"></div>






















<details markdown="block" open>

### Full Definition of SOE Model from Chapter 16

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

Changes from the closed economy version of the model are highlighted in red.

<div class="pagebreak"></div>







## How does this change the effects of shocks in the model?

The labor market works pretty much the same as before.
Our agents are price-takers, which means they were already behaving as if the interest rate were exogenous.

But now shocks which would change the interest rate will instead just cause a change in $NX$, shifting the $Y_{d}$ curve to cancel out that change in interest rates.

- Increase in $z$:
    -  Like in closed economy (ch 11), this causes the $N_{d}$ and $Y_{s}$ curves to shift right.
    -  But, unlike in a closed economy, the $r$ is fixed, so the $Y_{d}$ must now shift to bring the economy back into equilibrium.
    - So equilibrium $NX$ will increase. Much of the extra production will thus be shipped overseas.
- Increase in $z'$:
    - The firm wants to invest more, which causes $Y_{d}$ to shift right.
    - Then NX decreases to cancel out this shift and keep the economy in its original equilibrium for $Y,r,N,w$.
    - Essentially, all that's happened is that net exports have been turned into investment.
- Increase in $G$:
    - In the closed economy, the direct effects are a shift rightwards in the $Y_d$ curve, as well as a shift rightwards in the $N_s$ curve because of higher taxes.
    - The latter effect still happens. Higher $T$ causes $N_{s}$ and $Y_{s}$ curves to shift right.
    - But the shift in the Y_{d} curve is counteracted by a decrease in $NX$.
    - So output goes up, but not as much as in the closed economy. 
- Increase in $r_w$:
    - Increase in $r$ makes the $N_{s}$ curve shift right as we move up along the $Y_{s}$ curve.
    -  And the $Y_{d}$ curve shifts to bring this into equilibrium as this extra output is exported.
    -  Note that the firm is investing less and consumer is consuming less because of the higher interest rate. So some of the preexisting output is being exported as well.







<!--


## Other Notes about Open Economies

### Current Account and Savings:

2 period endowment economy budget constraints:c+\frac{c'}{1+r}\leq(y-T)+\frac{y'-T'}{1+r}

G+\frac{G'}{1+r}=T+\frac{T'}{1+r}

In first period:s_{p}=(y-T)-c

• s_{g}=T-G

\text{national savings}	=s_{p}+s_{g}
	=(y-T)-c+T-G
	=y-c-G

In the closed economy, where the market clearing condition is y=c+G

In the open economy, the market clearing condition is y=c+G+NX\text{national savings}	=s_{p}+s_{g}
	=y-c-G
	=NX



### Additional Vocab Terms:

Current Account +capital account = balance of payments

Current Account: Net exports, and also transfers. 

Capital Account:

– portfolio investment: investment in a company that already exists
– foreign direct investment: creating a new business


-->