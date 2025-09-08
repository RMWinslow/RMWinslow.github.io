---
title: Remark Formatting Test
layout: remark_slides
date: 2023-05-12
nav_exclude: true
---

class:center,middle

# Remark Formatting Test

Robert Winslow

2023-05-09







---

* Does this become a table of contents? (If you see this, the answer is no.)
{:toc}



---

## Slide with a Footnote

This is a standard jekyll style footnote.[^footnoteexample]
And here is another sentence.

[^footnoteexample]: This should appear in a footnote.

(Doesn't work, sadly)

---

## alt footnote test


Markup for a title slide, for footnotes$^1$.footnote[$1.$ Here is a footnote, located at the bottom of the page as the name suggests.], and for citations 




---


layout: true
class: header

## Section

---

### Sub section 1

---

### Sub section 2


---

layout: true
class: header

## New Section

---

### Sub section 1b

---

### Sub section 2b


---

yeehaw

---

layout: false

okey dokes

---


inline $\int_{-\infty}^\infty e^{-i \omega \tau} R_{zz}(\tau) \, d\tau=  S_{zz}(\omega)$

and display:

$$\int_{-\infty}^\infty e^{-i \omega \tau} R_{zz}(\tau) \, d\tau=  S_{zz}(\omega)$$

Same thing but across multiple lines


$$
\int_{-\infty}^\infty 
e^{-i \omega \tau} R_{zz}(\tau) \, d\tau= 
S_{zz}(\omega)$$


Same thing but different delimiters

\\[\int_{-\infty}^\infty e^{-i \omega \tau} R_{zz}(\tau) \, d\tau=  S_{zz}(\omega)\\]



And here's the same thing but with slashes before the underscore

$$\int\_{-\infty}^\infty e^{-i \omega \tau} R\_{zz}(\tau) \, d\tau=  S\_{zz}(\omega)$$


Same thing but wrapped in a div

<div>
$$\int_{-\infty}^\infty e^{-i \omega \tau} R_{zz}(\tau) \, d\tau=  S_{zz}(\omega)$$
</div>


---

## katex gdefs

$$\gdef\foo#1{#1^2} \foo{y} + \foo{y}$$

$$\foo{34}$$

$$\gdef\RIZZ{R_{zz}(\tau)}$$

$$\gdef\SIZZ{S_{zz}(\omega)}$$


$$\int\_{-\infty}^\infty e^{-i \omega \tau} \RIZZ \, d\tau=  \SIZZ$$


---

## katex multiline

$$\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\
    \theta_T & \text{if } t\geq T
\end{cases}$$


$$\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\\\
    \theta_T & \text{if } t\geq T
\end{cases}$$



---


$$
\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\
    \theta_T & \text{if } t\geq T
\end{cases}
$$


<div>
$$
\theta(t) = 
\begin{cases}
    \theta_t & \text{if } t\in\{0,...,T-1\} \\
    \theta_T & \text{if } t\geq T
\end{cases}
$$
</div>

---

Two slashes:

`\\`

Four slashes

`\\\\`

---


layout: true
class: header

## lists

---

### ordered

1. test
1. test
1. test
1. test
1. test
1. test


---

### Unordered

- test
- test
- test
- test
- test
- test

---

### dlist

term
: definition

term
: definition

term
: definition

term
: definition







---

layout: true

## table


---

| a | b | c |
|:--|:-:|--:|
| test | test | test |
| test | test | test |
| test | $\beta^2$ | test |
| test | test | test |

--

### alt format

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell




---

layout: false
class:caption-slide

## Images

I want images to autofit to page.

![test image, ignore the content](https://www.rmwinslow.com/3102/img-money-snails.webp)

---

![test image, ignore the content](https://www.rmwinslow.com/3102/img-money-snails.webp)







---

<figure markdown="block">
<img src="img-money-snails.webp">
<figcaption  markdown="block">Monetaria Moneta, the Money Cowrie. The shells of these snails were widely used as money.
<br>
Left: [Live money snail. CC-BY-SA-5 Philippe Bourjon.](https://commons.wikimedia.org/wiki/File:Monetaria_moneta_-_2.jpg)
Center: [Ancient Chinese Shell Money. CC-BY-SA-3 PHGCOM.](https://commons.wikimedia.org/wiki/File:Chinese_shell_money_16th_8th_century_BCE.jpg)
Right: [Lithograph of traders using shells. 1845](https://commons.wikimedia.org/wiki/File:A_print_from_1845_shows_cowry_shells_being_used_as_money_by_an_Arab_trader.jpg)
</figcaption>
</figure>


---

class:center,middle


![test image, ignore the content](https://www.rmwinslow.com/3102/img-money-snails.webp)







---

class:center,middle


<figure markdown="block">
<img src="img-money-snails.webp">
<figcaption  markdown="block">Monetaria Moneta, the Money Cowrie. The shells of these snails were widely used as money.
<br>
Left: [Live money snail. CC-BY-SA-5 Philippe Bourjon.](https://commons.wikimedia.org/wiki/File:Monetaria_moneta_-_2.jpg)
Center: [Ancient Chinese Shell Money. CC-BY-SA-3 PHGCOM.](https://commons.wikimedia.org/wiki/File:Chinese_shell_money_16th_8th_century_BCE.jpg)
Right: [Lithograph of traders using shells. 1845](https://commons.wikimedia.org/wiki/File:A_print_from_1845_shows_cowry_shells_being_used_as_money_by_an_Arab_trader.jpg)
</figcaption>
</figure>







---



![Mizaru](https://upload.wikimedia.org/wikipedia/commons/6/6e/Emoji_u1f648.svg)

(This won't work because the `remark_slides` template will break the underscore in the file name.)
