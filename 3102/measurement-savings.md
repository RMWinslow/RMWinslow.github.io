---
title: National Savings
parent: 3102 Notes
grand_parent: Teaching
---

<style>
@font-face {
  font-family: 'Quattrocento';
  src: url(../../webfonts/serif/Quattrocento-Regular.ttf);
}
@font-face {
  font-family: 'Roboto';
  src: url(../../webfonts/serif/RobotoSlab-VariableFont_wght.ttf);
}
main {
  font-family: 'Quattrocento';
}
</style>


In addition to the main national accounts, the BEA also keeps track of stats about savings derived from GDP
components and the like.

Private Disposable Income 
: How much income do households have available to spend?

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



Private Sector Saving
: The income that households had available, but which they did not spend.
: Private Disposable Income, minus Consumption

$$S_p = Y_d - C$$

In the equation above, any disposable income not spent on final consumption goods counts as "savings".
On an individual level, buying used goods counts as savings by the above definition, but selling used goods counts as "negative savings", and so such transactions cancel out in aggregate.


Government Savings 
: All the money the government collects, minus the money that they spend.

$$S_g = \textcolor{#b58900}{T} - \left(  \textcolor{#2aa198}{G} + \textcolor{#dc322f}{TR} + \textcolor{#859900}{INT}     \right) $$

<span style="color:">Government Savings</span> = 
<span style="color:#2aa198">Government Expenditures</span> - 
<span style="color:#b58900">Taxes</span> - 
<span style="color:#dc322f">Net transfers from the government to private individuals</span> - 
<span style="color:#859900">Interest on government debt held by individuals </span>.


### National Savings

$$\begin{align*}
S &=S_{p}+S_{g} \\
 &=\left(Y+NFP+TR+INT-T-C\right)+\left(T-G-TR-INT\right)\\
 &=\left(Y-C-G\right)+NFP\\
 &=I+NX+NFP\\
 &=I+CA\\
\end{align*}$$


<!---

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
