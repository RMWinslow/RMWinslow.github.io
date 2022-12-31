---
title: Social Security
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: false
nav_order: 503
last_modified_date: 2022-12-30
---

We want to give money to the elderly. In order to fund this, we need to take money from young people at some point.


## Fully Funded (Privatized):

- You pay for your own benefits.

- Government collects T in taxes when you are young.

- Pay you b benefits when you are old.

- Consumer constraints without the social security: $$c+s\leq y\\c'\leq y'+(1+r)s\\c+\frac{c'}{1+r}\leq y+\frac{y'}{1+r}$$

- Consumer budget with this program: $$c+s\leq y-T\\c'\leq y'+(1+r)s+b\\c+\frac{c'}{1+r}\leq\left(y-T\right)+\frac{\left(y'+b\right)}{1+r}$$

- Gov budget balanced (and the government isn't doing anything other than this social security program.) $$G+\frac{G'}{1+r}=T+\frac{T^{\prime}}{1+r}\\0+\frac{0}{1+r}=T+\frac{-b}{1+r}\\T=\frac{b}{1+r}\\(1+r)T=b$$

- The present value budget for the consumer becomes:$$c+\frac{c'}{1+r}\leq\left(y-T\right)+\frac{\left(y'+(1+r)T\right)}{1+r}c+\frac{c'}{1+r}\leq\left(y\right)+\frac{\left(y'\right)}{1+r}$$
- No different than forced savings. Potentially makes things worse if their are credit market imperfections.
- There are arguments for this kind of system (see chapter 10 in the book), but not within our simple 2 period model.

## Pay-as-you-go:

- You pay for the benefits of the previous generation.

- The current young pay the benefits of the current old.

- Government collects $T$ in taxes when you are young.

- Government immediately pays that money to the people who are already old. ($b$ to each person).

- OLG (Overlapping Generations model):

    - Your generation, the generation born in time period $t$, has $N_{t}$ population

    - The older generation, who are old when you are young, has population $N_{t-1}$.

    - The younger generation, who is young when you are old, has population $N_{t+1}$.

    - Say that population is growing at rate $n$, so $N_{t+1}=(1+n)N_{t}$ for any $t$. $N_{t}=(1+n)N_{t-1}$.

- Gov budget must be balanced, and for simplicity we will assume no other government programs are happening, just the lump sum tax and transfer each period.

    - In time period t, when you are young:

        - Revenue = $T\cdot N_{t}$

        - Benefits paid out = $b\cdot N_{t-1}$

        $$T\cdot N_{t}=b\cdot N_{t-1}\\
        T\cdot(1+n)N_{t-1}=b\cdot N_{t-1}\\
        T\cdot(1+n)=b\\
    b_{t-1}=T\cdot\frac{N_{t}}{N_{t-1}}$$

    - In time period $t+1$, when you are old:

        - Revenue = $T\cdot N_{t+1}$
        - Benefits paid out = $b\cdot N_{t}$
            $$T\cdot N_{t+1}=b\cdot N_{t} \\ b_{t}=T\cdot\frac{N_{t+1}}{N_{t}}=T\cdot(1+n)$$

How does this program affect the consumer's budget constraint?

$$c+\frac{c'}{1+r}\leq\left(y-T\right)+\frac{\left(y'+b\right)}{1+r}\\
c+\frac{c'}{1+r}\leq\left(y-T\right)+\frac{\left(y'+T\cdot(1+n)\right)}{1+r}\\
c+\frac{c'}{1+r}\leq\left(y\right)+\frac{\left(y'\right)}{1+r}-T+\frac{T\cdot(1+n)}{1+r}$$

- The present value of the change in lifetime present value income from this program for your generation is
$$-T+\frac{T\cdot(1+n)}{1+r}$$

- This will be positive, meaning that this expands your intertemporal budget constraint iff
 
$$T < \frac{T\cdot(1+n)}{1+r}\\
1+r < 1+n\\
r < n$$

