---
title: National Savings
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: false
nav_order: 103
last_modified_date: 2022-08-23
---



In addition to the main national accounts, the BEA also keeps track of stats about savings derived from GDP
components and the like.

## Private Disposable Income 

How much income does the private sector have available to spend?

$$Y_d = \textcolor{#6c71c4}{Y} + \textcolor{#268bd2}{NFP} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT} - \textcolor{#b58900}{T}$$

<span style="color:">Private Disposable Income</span> = 
<span style="color:#6c71c4">Output</span> + 
<span style="color:#268bd2">Net factor payments</span> + 
<span style="color:#dc322f">Net transfers from the government to private individuals</span> + 
<span style="color:#859900">Interest on government debt held by individuals </span> - 
<span style="color:#b58900">Taxes</span>.

A few notes:
- GDP (labelled <span style="color:#6c71c4">Y</span> above) is the output that is produced in a country, physically within its borders. GNP is the output from residents of a country. $GNP = \textcolor{#6c71c4}{Y} + \textcolor{#268bd2}{NFP}$. Net factor payments can be thought of as the adjustment between GDP and GNP. 
- Privately held debt doesn’t show up in the above equation, nor do most transfers between individuals, because if I give you money that’s less disposable income for me but the same amount more for you.



## Private Sector Saving

The income that households had available, but which they did not spend.
Private Disposable Income, minus Consumption

$$S_p = Y_d - C$$

In the equation above, any disposable income not spent on final consumption goods counts as "savings".
On an individual level, buying used goods counts as savings by the above definition, but selling used goods counts as "negative savings", and so such transactions cancel out in aggregate.


## Government Savings 

All the money the government collects, minus the money that they spend.

$$S_g = \textcolor{#b58900}{T} - \textcolor{#2aa198}{G} - \textcolor{#dc322f}{TR} - \textcolor{#859900}{INT}$$

<span style="color:">Government Savings</span> = 
<span style="color:#2aa198">Government Expenditures</span> - 
<span style="color:#b58900">Taxes</span> - 
<span style="color:#dc322f">Net transfers from the government to private individuals</span> - 
<span style="color:#859900">Interest on government debt held by individuals </span>.

The government deficit is simply the negative of government savings.


$$\text{Government Deficit} =  \textcolor{#2aa198}{G} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT} - \textcolor{#b58900}{T}$$

- If $\textcolor{#b58900}{T} > (\textcolor{#2aa198}{G} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT})$, then government savings is positive, and we say the government has a budget surplus.
- If $\textcolor{#b58900}{T} < (\textcolor{#2aa198}{G} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT})$, then government savings is negative, we say the government has a budget deficit, and the value of this deficit is the difference between .


## National Savings


$$\begin{aligned}
S &=S_{p}+S_{g} \\
  &=\left(\textcolor{#6c71c4}{Y} + \textcolor{#268bd2}{NFP} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT} - \textcolor{#b58900}{T}-C\right)+\left( \textcolor{#b58900}{T} - \textcolor{#2aa198}{G} - \textcolor{#dc322f}{TR} - \textcolor{#859900}{INT}\right)\\
  &=\left(\textcolor{#6c71c4}{Y}-C-\textcolor{#2aa198}{G} \right)+\textcolor{#268bd2}{NFP}\\
  &=I+NX+\textcolor{#268bd2}{NFP}\\
  &=I+CA\\
\end{aligned}$$

where the current account (CA) is Net Exports plus Net Factor Payments.




<!---

https://fred.stlouisfed.org/series/NETFI
https://fred.stlouisfed.org/release/tables?rid=53&eid=5405#snid=5453


(Personal Income?)What is Disposable Personal Income?
After-tax income. The amount that U.S. residents have left to spend or save after paying taxes is important not just to individuals but to the whole economy. The formula is simple: personal income minus personal current taxes.

https://fred.stlouisfed.org/series/B087RC1Q027SBEA
https://fred.stlouisfed.org/release/tables?rid=54&eid=155443#snid=155470
https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/glossary.pdf
https://fred.stlouisfed.org/series/PI

https://fred.stlouisfed.org/release/tables?rid=53&eid=17757#snid=17764
https://fred.stlouisfed.org/release/tables?rid=53&eid=15274#snid=15278
https://fred.stlouisfed.org/release/tables?rid=53

https://fred.stlouisfed.org/release/tables?rid=53&eid=44068
GDP release tables
https://fred.stlouisfed.org/release/tables?rid=53

https://fred.stlouisfed.org/release/tables?rid=53&eid=5405#snid=5415

https://fred.stlouisfed.org/release/tables?rid=53&eid=15274#snid=15278

https://fred.stlouisfed.org/series/MTSDS133FMS

NIPA 2-7 Income and savings has some interesting notes on what isn't counted as savings

Private Sector Saving
: Private Disposable Income - Consumption

Government Saving
: Taxes - Transfers - Interest on Government Debt - Government Expenditures
-->
