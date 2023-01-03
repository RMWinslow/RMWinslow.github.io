---
title: Two Period Firm
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 504
last_modified_date: 2022-12-30
---


<!--
Consumers in an intertemporal endowment economy

$$\max_{c,c'}u(c)+\beta u(c')$$

subject to:

$$c\geq0,c'\geq0\\
c+\frac{c'}{1+r}\leq y+\frac{y'}{1+r}+\left(-T-\frac{T^{\prime}}{1+r}\right)$$

Characterizing equations:

Intertemporal Euler condition $$MRS_{cc'}=(1+r)$$

Consumers in an intertemporal economy, with labor leisure

\max_{c,c',l,l'}u(c,l)+\beta u(c',l')c\geq0,c'\geq0,h\geq l\geq0,h\geq l'\geq0c+\frac{c'}{1+r}\leq w(h-l)+\frac{w^{\prime}(h^{\prime}-l^{\prime})}{1+r}+\left(-T-\frac{T^{\prime}}{1+r}\right)

Or if we include labor explicitly\max_{c,c',l,l',N_{s},N_{s}^{\prime}}u(c,l)+\beta u(c',l')c\geq0,c'\geq0,l\geq0,l'\geq0,N_{s}\geq0,N_{s}^{\prime}\geq0c+\frac{c'}{1+r}\leq w(h-l)+\frac{w^{\prime}(h^{\prime}-l^{\prime})}{1+r}+\left(-T-\frac{T^{\prime}}{1+r}\right)N_{s}=h-lN_{s}^{\prime}=h-l^{\prime}

Characterizing equations

- Intertemporal Euler conditionMRS_{cc'}=(1+r)

- Intratemporal Euler conditionsMRS_{lc}=wMRS_{l'c'}=w

- Budgetc+\frac{c'}{1+r}=w(h-l)+\frac{w^{\prime}(h^{\prime}-l^{\prime})}{1+r}+\left(-T-\frac{T^{\prime}}{1+r}\right)

Quick Note about utility across time:

2 period version isU(c,c',l,l')=u(c,l)+\beta u(c',l')

Infinite period version is typically written

U(c_{0},c_{1},...,l_{0},l_{1},...)=\sum_{t=0}^{\infty}\beta^{t}u(c_{t},l_{t})

Note that this is “exponential” time preferences, experimentally, it seems people have “hyperbolic” time preferences.

(You don't need to worry about this for this class. We're sticking to 2 time periods.)
-->


## Firms in the one period economy

- Firms own exogenous capital $K$ at the start of the only period.
- The firm's profit maximization problem is:

$$\max_{N_{d}}\left[zF(K,N_{d})-wN_{d}\right]$$

subject to $N_{d}\geq0$

## Firms in an intertemporal economy

- Firms own exogenous capital $K$ at the start of the first period.
- Second period capital is determined by $K^{\prime}=K\cdot(1-\delta)+I$, where $I$ is the firm's investment in the first period.
- The firm also chooses the amount of labor to hire in each period $N_d, N_d'$
- The firm's goal is to maximize present-value profits $\pi + \frac{\pi'}{1+r}$
- In the first period, profits are output minus the cost of labor and investment.
- In the second period, the firm must still hire workers, but is no need to invest because there is no third period. 
- Any capital left over after period two, $(1-\delta)K'$ will be sold as units of output.

The firm's problem is thus:

$$\max_{N_{d},N_{d}^{\prime},I,K^{\prime}}\pi+\frac{\pi^{\prime}}{1+r}$$


$$
\begin{aligned}
\text{s.t. }\ \ \ \ &N_{d}\geq0,\ \ N_{d}^{\prime}\geq0,\ \ K^{\prime}\geq0 \\
&\pi=zF(K,N_{d})-wN_{d}-I \\
&\pi^{\prime}=z^{\prime}F(K^{\prime},N_{d}^{\prime})-w^{\prime}N_{d}^{\prime}+K^{\prime}\cdot(1-\delta) \\
&K^{\prime}=(1-\delta)K+I
\end{aligned}
$$

Solve for $I$ and plug into profit equations:

$$I = K^{\prime}-(1-\delta)K$$

$$\pi = zF(K,N_{d})-wN_{d}-K^{\prime}+(1-\delta)K$$

If we set up the firm's problem with these substitutions:

$$\max_{N_{d},N_{d}^{\prime},I,K^{\prime}}\pi+\frac{\pi^{\prime}}{1+r}$$

$$
\begin{aligned}
\text{s.t. }\ \ \ \ &N_{d}\geq0,\ \ N_{d}^{\prime}\geq0,\ \ K^{\prime}\geq0 \\
&\pi=zF(K,N_{d})-wN_{d}-K^{\prime}+(1-\delta)K \\
&\pi^{\prime}=z^{\prime}F(K^{\prime},N_{d}^{\prime})-w^{\prime}N_{d}^{\prime}+K^{\prime}\cdot(1-\delta) \\
\end{aligned}
$$

On one line: 

$$\max_{N_{d},N_{d}^{\prime},K^{\prime}}zF(K,N_{d})-wN_{d}-K^{\prime}+(1-\delta)K+\frac{z^{\prime}F(K^{\prime},N_{d}^{\prime})-w^{\prime}N_{d}^{\prime}+K^{\prime}\cdot(1-\delta)}{1+r}$$

$$\text{s.t. }\ \ \ \ N_{d}\geq0,\ \ N_{d}^{\prime}\geq0,\ \ K^{\prime}\geq0$$

If we have an interior solution, then 

$$\mathcal{L}=zF(K,N_{d})-wN_{d}-K^{\prime}+(1-\delta)K+\frac{z^{\prime}F(K^{\prime},N_{d}^{\prime})-w^{\prime}N_{d}^{\prime}+K^{\prime}\cdot(1-\delta)}{1+r}$$

First order conditions:

$$0=\frac{\partial}{\partial N_{d}}\mathcal{L}=MP_{N}-w\\
0=\frac{\partial}{\partial N_{d}^{\prime}}\mathcal{L}=\frac{MP_{N^{\prime}}-w^{\prime}}{1+r}\\
0=\frac{\partial}{\partial K^{\prime}}\mathcal{L}=-1+\frac{MP_{K^{\prime}}+1-\delta}{1+r}$$

Simplify/rearrange:

$$w=MP_{N}\\
w^{\prime}=MP_{N^{\prime}}$$

$$r+\delta=MP_{K^{\prime}}$$

Characterizing Equations for two period firm

- First period optimal hiring rule: $MP_{N}=\frac{\partial}{\partial N_{d}}zF(K,N_{d})=w$
- Second period optimal hiring rule: $MP_{N^{\prime}}=\frac{\partial}{\partial N_{d}^{\prime}}z'F(K',N_{d}^{\prime})=w'$
- Optimal Investment rule: $r+\delta=\frac{\partial}{\partial K'}z'F(K',N_{d}^{\prime})=MP_{K^{\prime}}$

<!--
Combine the two period consumer and two period firm

Market clearing conditions are 

$$\begin{aligned}
N_{s}=h-l=N_{d} &  & c+I+G=Y=zF(K,N_{d})\\
N_{s}'=h'-l'=N_{d}' &\;\;\;\;  & c'+G'=Y=z'F(K',N_{d}')+(1-\delta)K'\\
\end{aligned}$$
-->

