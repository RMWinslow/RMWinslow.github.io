---
title: Representative Producer
subtitle: The Producer in a one-period competitive equilibrium.
parent: 3102 Notes
grand_parent: Teaching
layout: post
toc: true
nav_order: 202
last_modified_date: 2022-08-23
---


## The Firm's Problem

Taking prices and capital $\lbrace w,K,z\rbrace$  as given, the firm chooses $\lbrace Y,N_{d}\rbrace$  to solve:

$$\begin{aligned}
\max_{Y,N_{d}} & \left[\pi=Y-wN_{d}\right] \\
\text{s.t. } & N_{d}\geq0,\ Y\geq0 \\
 & Y=zF(K,N_{d})
\end{aligned}$$

Note that we can simplify this problem by substituting away $Y$ to get

$$\begin{aligned}
\max_{N_{d}} & \left[\pi=zF(K,N_{d})-wN_{d}\right] \\
\text{s.t. } & N_{d}\geq0,\ \ \ \ zF(K,N_{d})\geq0
\end{aligned}$$


### What decisions does the firm make?

The firms chooses:
- how much output to produce $Y$ and 
- how much labor to hire $N_{d}$.

In general, we might also have the firm make investment decisions related to capital. But in this model (ch 4, 5), capital is exogenously given.

### What constraints do they operate under?

First of all, output and labor demand are **non-negative**:

$$Y\geq0 \\ N_{d}\geq0$$

Also, output is limited by the inputs. 
Inputs (labor,capital) are transformed into outputs using some **production technology**. 

$$\textcolor{#6c71c4}{Y} =\textcolor{#268bd2}{z} \textcolor{#dc322f}{F}(\textcolor{#859900}{K}, \textcolor{#b58900}{N_d})$$

<span style="color:#6c71c4">Output</span> is equal to 
<span style="color:#268bd2">some total factor productivity multiplier</span> times 
<span style="color:#dc322f">some function of</span> 
<span style="color:#859900">the capital stock</span> and
<span style="color:#b58900">the amount of labor hired</span>.


<!--$$\text{Output = A function of (capital, labor hired)}$$-->

Useful properties for this function to have:

-  **Constant Returns to Scale**: Scaling up all inputs scales up output by the same amount. For any constant $x$, $zF(xK,xN_{d})=xzF(K,N_{d})$
-  **Strictly increasing in $N_{d}$ and in $K$**. 
 
  $$MP_{N}=zF_{N}^{\prime}(K,N)>0\\
  MP_{K}=zF_{K}^{\prime}(K,N)>0$$

-  The marginal product of one input increases when we increase the quantity of the other input. 
   
  $$\frac{\partial}{\partial N}\frac{\partial}{\partial K}zF(K,N)=\frac{\partial}{\partial N} MP_{K} > 0 \\
  \frac{\partial}{\partial K}\frac{\partial}{\partial N}zF(K,N)=\frac{\partial}{\partial K}MP_{N} > 0$$
  
-  The marginal product of an input decreases as we increase the quantity of that input. 
  
  $$\frac{\partial}{\partial K}\frac{\partial}{\partial K}zF(K,N)=\frac{\partial}{\partial K}MP_{K} < 0 \\
  \frac{\partial}{\partial N}\frac{\partial}{\partial N}zF(K,N)=\frac{\partial}{\partial N}MP_{N} < 0$$

<!--TODO: example of verifying properties
#### Example: Cobb-Douglas
$$zF(K,N)=zK^{\alpha}N^{1-\alpha}$$ 
for some $\alpha\in(0,1)$. Let's verify the properties above:
...-->

### What is the firm's goal?

Maximize Profit. 

-  Profit = Revenue - Costs
-  Revenue in this model is simply output $Y$. (Because this is a “real” model, where the price of a unit of aggregate goods is 1).
-  Costs = The money spent to hire labor. $= wN_{d}$
    
    $$\underbrace{w}_{realWage}\cdot\underbrace{N_{d}}_{laborDemand}$$
    
    -  Capital is an input but not included in the cost, because with only time period, there is no investment, so capital is just exogenous.
        -  For simplicity, we'll just assume that the firm owns the initial exogenous capital.
        -  We could also have consumers own it, and sell to the firm, but that wouldn't change equilibrium allocations.
-  Therefore profit is $\pi=Y-wN_{d}=zF(K,N_{d})-wN_{d}$

Putting it together, we get the rep firm's constrained optimization problem.



### First Order Conditions

Assuming an interior solution, the firm's profit maximization problem is characterized by 

$$\text{Marginal Cost of Labor}=\text{Marginal Benefit of Labor}$$

$$w=MP_{N}$$

For Cobb Douglas ($zK^{\alpha}N^{1-\alpha}$), this is

$$w=(1-\alpha)z\left(\frac{K}{N^{*}}\right)^{\alpha}$$

which can be solved for $N^{*}$ to get

$$N^{*}=\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1}{\alpha}}$$









## A Graphical Example

<link href="https://kineticgraphs.org/css/kg.0.2.6.css" rel="stylesheet" type="text/css" />
<script src="https://kineticgraphs.org/js/kg3d.0.2.6.js"></script>
<div class="kg-container" src="./graphs/twoPeriodCollateralConstraint.yml" clearcolor="#fff0"></div>










## Shocks to our exogenous parameters:

How does the Firm's decisions change in response to changes in exogenous parameters?

Exogenous parameters: $w,K,z,\alpha$

### Increase in real wage $w$

$N_{d}^{*}$ decreases and so $Y^{*}$ decreases. 
For example, with Cobb-douglass, this can be shown by:

$$\frac{\partial}{\partial w}N_{d}^{*}=\frac{\partial}{\partial w}\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1}{\alpha}} < 0$$

### Increase in the exogenous capital stock $K$

$N_{d}^{*}$ increases and so $Y^{*}$ increases.

In Cobb-Douglas:

$$\frac{\partial}{\partial K}N_{d}^{*}=\frac{\partial}{\partial K}\left(\frac{(1-\alpha)z}{w}\right)^{\frac{1}{\alpha}}K=\left(\frac{(1-\alpha)z}{w}\right)^{\frac{1}{\alpha}} > 0$$

### Increase in total factor productivity $z$

In this model, without investment, this has the same effect as increase in K. 
$N_{d}^{*}$ increases and so $Y^{*}$ increases.

In Cobb-Douglas:

$$\frac{\partial}{\partial z}N_{d}^{*}=\frac{\partial}{\partial z}\left(\frac{(1-\alpha)K^{\alpha}}{w}\right)^{\frac{1}{\alpha}}z^{\frac{1}{\alpha}}=\left(\frac{(1-\alpha)K^{\alpha}}{w}\right)^{\frac{1}{\alpha}}\frac{1}{\alpha}z^{\frac{1}{\alpha}-1} > 0$$

###  Increase in `$\alpha$`: 

(This one only applies for Cobb-Douglas)

It becomes optimal to hire less labor because labor has less impact on output. $N_{d}^{*}$ decreases.





<aside markdown="block">

Interesting note about Cobb-Douglas:

$$Y^{*}=zK^{\alpha}\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1-\alpha}{\alpha}}$$

$$N_{d}^{*}=\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1}{\alpha}}$$

$$\begin{aligned}
\frac{wN_{d}^{*}}{Y^{*}} & =\frac{w\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1}{\alpha}}}{zK^{\alpha}\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1-\alpha}{\alpha}}} \\
 & =\frac{w}{zK^{\alpha}}\left(\frac{(1-\alpha)zK^{\alpha}}{w}\right)^{\frac{1}{\alpha}-\frac{1-\alpha}{\alpha}} \\
 & =\frac{w}{zK^{\alpha}}\frac{(1-\alpha)zK^{\alpha}}{w} \\
 & =(1-\alpha)
\end{aligned}$$

$$\frac{\pi^{*}}{Y^{*}}=\frac{Y^{*}-wN_{d}^{*}}{Y^{*}}=\alpha$$

So if we want a "real-world" estimate of $1-\alpha$, we can use the [labor compensation as a share of GDP](https://fred.stlouisfed.org/series/LABSHPUSA156NRUG), which gives us $\alpha\approx30-40\%$

</aside>



