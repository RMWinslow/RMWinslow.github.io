---
title: Constrained Optimization
subtitle: An example of applying the Lagrangian technique.
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: true
nav_order: 001
date: 2023-09-11
last_modified_date: 2023-09-11
---

## The Problem:

$$
\begin{align*}
\max_{x,y}\,\,\,&x^{\alpha}y^{1-\alpha}\\
\text{s.t.\,\,\,}&x\geq0\\
&y\geq0\\
&x+y\leq10
\end{align*}
$$

## The Solution

### Setting up the Lagrangian:

To set up the lagrangian, we add in a term for each binding constraint. (“Binding” here means, that at the optimum, the constraint will hold with equality.)

For this problem, the budget constraint ($x+y\leq10$) will be binding, and the non-negativity constraints won't be. (Why? That argument is left as an exercise for the reader.)

$$\mathcal{L}=x^{\alpha}y^{1-\alpha}-\lambda\cdot\left[x+y-10\right]$$

The basic recipe for the Lagrangian is 

1. Start with the thing you're trying to optimize.
2. For each binding constraint
    - Take the constraint and move everything to one side.
    - Multiply the constraint by a new variable, which is called the “Lagrange Multiplier” for that constraint.


If you have multiple binding constraints, you'll need a lagrange multiplier for each one. 
$\lambda$ is the typical symbol used for these variables, and that's what I've used above.

Note also that we could write the above equation like so:

$$\mathcal{L}=x^{\alpha}y^{1-\alpha}+\lambda\cdot\left[10-x-y\right]$$

This is equivalent.

### First Order Conditions:

Now we take the partial derivatives of the Lagrangian, and set each derivative equal to zero:

$$\frac{\partial\mathcal{L}}{\partial x}=\alpha x^{\alpha-1}y^{1-\alpha}-\lambda=0\tag{x}$$

$$\frac{\partial\mathcal{L}}{\partial y}=\left(1-\alpha\right)x^{\alpha}y^{-\alpha}-\lambda=0\tag{y}$$

$$\frac{\partial\mathcal{L}}{\partial\lambda}=10-x-y=0\tag{λ}$$



<aside>A “First Order Condition”, or FOC, is an equation you get by setting a derivative equal to zero. The name comes from the fact that a derivative is sometimes called a “first-order derivative” to be more precise.</aside>

Next, we can rearrange these equations to get:

$$\alpha x^{\alpha-1}y^{1-\alpha}=\lambda\tag{x}$$

$$\left(1-\alpha\right)x^{\alpha}y^{-\alpha}=\lambda\tag{y}$$

$$x+y=10\tag{\lambda}$$

The solution to this system of equations gives us the critical points for $\mathcal{L}$, and thus potential solutions to the original problem.

Note that the last equation is just our budget constraint! This is the magic behind the Lagrangian: it transforms constraints into FOCs.

### Solving the System of Equations:

If we want to solve for x and y, we need to start by getting rid of that extra variable \lambda we added. In this case, that's easy. We just combine the first two FOCs like so:

$$\alpha x^{\alpha-1}y^{1-\alpha}=\lambda=\left(1-\alpha\right)x^{\alpha}y^{-\alpha}$$

$$\alpha x^{\alpha-1}y^{1-\alpha}=\left(1-\alpha\right)x^{\alpha}y^{-\alpha}$$

The next step is to solve for one of the two remaining variables in terms of the other. We can start by cancelling x from one side and y from the other.

$$
\begin{align*}
\alpha x^{\alpha-1}y^{1-\alpha}&=\left(1-\alpha\right)x^{\alpha}y^{-\alpha}\\
\frac{\alpha\cancel{x^{\alpha-1}}y^{1-\alpha}}{\cancel{x^{\alpha-1}}y^{-\alpha}}&=\frac{\left(1-\alpha\right)x^{\alpha}\cancel{y^{-\alpha}}}{x^{\alpha-1}\cancel{y^{-\alpha}}}\\
\frac{\alpha y^{1-\alpha}}{y^{-\alpha}}&=\frac{\left(1-\alpha\right)x^{\alpha}}{x^{\alpha-1}}
\end{align*}
$$

Next we can simplify and rearrange a bit more to get:

$$
\begin{align*}
\frac{\alpha y^{1-\alpha}}{y^{-\alpha}}&=\frac{\left(1-\alpha\right)x^{\alpha}}{x^{\alpha-1}}\\
\alpha y^{1-\alpha-(-\alpha)}&=\left(1-\alpha\right)x^{\alpha-(\alpha-1)}\\
\alpha y^{1}&=\left(1-\alpha\right)x^{1}\\
y&=\frac{1-\alpha}{\alpha}\cdot x
\end{align*}
$$

Substitute this expression of y into the budget and solve for x:

$$
\begin{align*}
10	&=x+y\\
10	&=x+\left(\frac{1-\alpha}{\alpha}\cdot x\right)\\
10	&=\left(1+\frac{1-\alpha}{\alpha}\right)\cdot x\\
10	&=\left(\frac{\alpha}{\alpha}+\frac{1-\alpha}{\alpha}\right)\cdot x\\
10	&=\left(\frac{1}{\alpha}\right)\cdot x\\
\alpha\cdot10	&=x
\end{align*}
$$

Fantastic! We've solved for x. It's fine that $\alpha$ is still in there because $\alpha$ is a constant, not a variable. The last step is to plug our solution for x back into the expression for y:

$$
\begin{align*}
y	&=\frac{1-\alpha}{\alpha}\cdot x\\
y	&=\frac{1-\alpha}{\cancel{\alpha}}\cdot\left(\cancel{\alpha}10\right)\\
y	&=\left(1-\alpha\right)10\\
\end{align*}
$$

### And We've Found the Solution:

$$
\boxed{
\begin{align*}
x	&=10\cdot\alpha\\
y	&=10\cdot\left(1-\alpha\right)
\end{align*}}
$$


## What about MRS=MRT?

You may remember from micro that finding the solution to a constrained optimization problem involves the condition that at the optimum, the marginal rate of substitution (MRS) is equal to the marginal rate of transformation (MRT).

In this problem, where $u(x,y)=x^{\alpha}y^{1-\alpha}$, we can find the MRS by dividing one marginal utility by the other:

$$MRS\equiv\frac{(\partial u/\partial y)}{(\partial u/\partial x)}=\frac{\left(1-\alpha\right)x^{\alpha}y^{-\alpha}}{\alpha x^{\alpha-1}y^{1-\alpha}}=\frac{1-\alpha}{\alpha}\cdot\frac{x}{y}$$

And in the budget constraint, $x$ and $y$ each “cost” one unit, so the MRT is $\frac{1}{1}=1$.

Setting MRT=MRS, we get:

$$1	=\frac{1-\alpha}{\alpha}\cdot\frac{x}{y}$$

which we can rearrange to get

$$y=\frac{1-\alpha}{\alpha}\cdot x$$

Now wait a second. Is that the same equation we go by combining our FOCs? 

It is!

This is, in fact, where the MRS=MRT rule comes from. And the same process can be used to derive similar “characterizing equations” for other constrained optimization problems.

<!--PS: If you ever hear me referring to the “Euler Equation”, this is what I'm referring to.-->