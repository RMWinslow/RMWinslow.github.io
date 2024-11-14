---
title: Balance of Payments
subtitle: Imports, Exports, and Capital Flows
parent: Principles of Macro
grand_parent: Notes
layout: post
date: 2024-11-13
last_modified_date: 2024-11-13
---

placeholder 


<!--
Links to maybe include:

1
This is one of the few gov sources I can find that uses the phrase capital outflow
https://www.govinfo.gov/content/pkg/ERP-2006/pdf/ERP-2006-chapter6.pdf
Even wikipedia only cites Mankiw

2
https://fred.stlouisfed.org/series/BOPI
> This series has been discontinued as a result of the comprehensive restructuring of the international economic accounts 
Then a link to the following, published 2014:
https://apps.bea.gov/scb/pdf/2014/07%20July/0714_annual_international_transactions_accounts.pdf
which in turn links to BEA's "concepts and methods document for the International Economic Accounts (next block)

3
https://www.bea.gov/international/concepts_methods.htm
(Sadly, this isn't pedgagogically great. I do like the blue/orange color coding)
Skip to chapter ten here for ITA.

References IMF BoP manual, 6th edition (see block 10)
Also note there are a few deviations from IMF BPM
(mostly due to nadequate data on intermediate goods?)
One interesting deviation is if you ship goods overseas for processing,
IMF says you should count the value of the processing as an imported service.
But US doesn't have the right data so counts it as a big export of goods,
followed by a bigger import of goods. 
Same impact on net exports, but will affect the subcomponents differently.

They measure currency flows by looking at shipments of $100 dollar notes from 
FRB cash offices to foreign banks. 
So they ARE measuring that, just aren't calling it reserves like I thought I remembered.

> Transactions in monetary gold are rare. Such transactions can only take place with another monetary authority or with an international institution such as the IMF that is authorized to hold monetary gold. I

> For individual partner countries and regions, in addition to errors and omissions, 
[the statistical discrepancy] also reflects discrepancies that arise when transactions with one country or region are settled 
through transactions with another country or region. These transfers of funds between foreign 
areas often occur because the dollar is used extensively in settling international transactions 
and forms a large part of the foreign currency reserves of many countries. 

>  The net lending or net borrowing terminology 
reflects the accounting identity that deficits in the current and capital accounts must be financed 
by inflows of borrowing from abroad and that surpluses in these accounts are offset by outflows of 
lending to nonresidents.

> Conceptually, the financial-account measure of net lending or net borrowing equals the measure from the current and capital accounts. In practice, the two measures differ by the statistical discrepancy.



4.
Here's a table on FRED with the international transactions broken down by category.
https://fred.stlouisfed.org/release/tables?rid=49&eid=996
NSA version:
https://fred.stlouisfed.org/release/tables?rid=49&eid=1145
Note: we net export services.
https://fred.stlouisfed.org/graph/?id=IEABCGN,IEABCSN,IEABCPIN,IEABCSIN,
(These data only go back to 2000. The old international accounts only go up to 2014. Really annoying.)
I really think the financial account numbers are noisy. Take a look at this for example:
https://fred.stlouisfed.org/graph/?id=IEAADIN,IEAAPIN,IEAAOIN,IEAARN,
Giant spike in aquisition before covid? (specifically currency when you break it down)
Seems odd, like a data artifact or something? Unless travel bans elsewhere led to US unable to offload foreign currency?
Same spike shows up in liabilities graph.


5
breakdown of current account
https://fred.stlouisfed.org/release/tables?rid=53&eid=5405

6
Another import export table - don't know difference compared to above
https://fred.stlouisfed.org/release/tables?rid=51

7
Here's a fed speech that actually uses the term "capital outflow"
https://www.federalreserve.gov/newsevents/speech/kroszner20070515a.htm
(Thanks kagi!, though google does about as well)
So it isn't EXCLUSIVELY Mankiw that uses the term. 
Though it still doesn't seem to be the main term used by the BEA and similar.

8
A Primer on the U.S. International Economic Accounts
https://apps.bea.gov/scb/issues/2021/07-july/0721-iea-primer.htm
What I'm looking for is called ITAs by BEA
See here for interactive table of ITA and IIP
https://apps.bea.gov/iTable/?ReqID=62
(Remember to click the "Modify" button.)
I think this gives same as tables 996 and 1145 above

Current Account is:
Net Exports
+ Primary Income (investment income and compensation of employees)
+ secondary income (transfers - gov, charity, family, etc)

"Capital Account" now means transfers for things like debt forgiveness or insurance claims.
Seems like it could have just been folded in.

For financial account, BEA uses “net acquisition of financial assets” and “net incurrence of liabilities.”
Or "financial outflow" and "financial inflow" for short.
(Is the term NET FINANCIAL OUTFLOW used anywhere?)

TODO: Try to find list of "Principal Federal Economic Indicators"
> Principal Federal Economic Indicators are major statistical series designated by the Office of Management and Budget that describe the current condition of the U.S. economy.




9
Directly relevant FRED blog post:
https://fredblog.stlouisfed.org/2017/02/demystifying-the-trade-balance/

The Rest of the world; net lending (+) or borrowing (-) (capital account), Flow (DISCONTINUED) is discontinued
The Rest of the World; Net Lending (+) or Borrowing (-) (Capital Account), Transactions  (RWLBACQ027S) seems like a decent match.
That's from the flow of funds tables.
https://fred.stlouisfed.org/graph/?g=1APjc
Later has a link to "Financial Accounts Guide" which isn't super helpful
https://www.federalreserve.gov/apps/fof/Default.aspx
But the directory of tables might be useful
https://www.federalreserve.gov/apps/fof/FOFTables.aspx












10
Sixth Edition of the IMF's Balance of Payments and International Investment Position Manual (BPM6)
https://www.imf.org/external/pubs/ft/bop/2007/bopman6.htm

chapter 2 has concept overviews, not an overall great introduction, however
> The sum of the balances on the current and
capital accounts represents the net lending (surplus) or
net borrowing (deficit) by the economy with the rest of
the world. This is conceptually equal to the net balance
of the financial account. In other words, the financial
account measures how the net lending to or borrowing
from nonresidents is financed. The financial account
plus the other changes account explain the change in
the IIP between beginning- and end-periods



chapter 14 is meant to be " an introduction to the use 
of balance of payments and international investment 
position data in economic analysis"
AND YEAH, CHAPTER 14 IS THE PEDAGOGY MVP
(or actually, "androgogy", because I'm teaching adults?)

chapter 14 has the following relationships:

Supply = output + M = use = C+G+I+X+intermediate consumption
(which would mean "use" is GDP plus intermediates and imports)

GNDY = C+I+G+X-M+BPI+BSI
gross national disposable income = GDP + balance on primary income + balance on secondary income (net current transfers)
current account balance = X-M+BPI+BSI
    = GNDY-C-I-G

gross saving is S
S=I+CAB
CAB = S-I

S-I=Sp+Sg-Ip-Ig
CAB = (Sp-Ip)+(Sg-Ig)

NLB = CAB+KAB = NFA
Net lending/borrowing = current+capital account balances = net financial account entries
(I think for teaching, it would be fine to summarize the capital account as transfers)

Alternatively
CAB=NKF+RT
where NKF is net capital and financial account transactions (excluding reserves), and RT is reserve asset transactions
(why are reserves not excluded in the first version???)

"analytic presentation" seperates out reserves and similar.
Montary Presentation: NFA+ΔDC-ΔM+OTR=0

S-I=CAB
=BTG+BTS+BPI+BSI (balance on each part of current account)
=NKF+RT


Lots of caveats that these are identities, and so casaulity shouldn't be inferred.

Quotes from chapter 14 of IMF BPM:

> Private investment could be positively or negatively affected by higher taxes. The effect 
would depend, in part, on whether the taxes were levied 
on consumption, an action that would release domestic resources and thereby tend to “crowd in” domestic 
investment, or on returns to investment. In addition, 
private saving would tend to fall because of the decline 
in disposable income caused by taxes on consumption. 
Similarly, an increase in interest rates could tend to 
reduce private consumption and investment, but also 
tend to put upward pressure on the exchange rate with 
consequent effects on exports, imports, and differing 
effects on debt service for domestic currency and foreign currency liabilities

For example, 
imports of goods may be financed by nonresident suppliers so that an increase in imports can be matched by 
a financial inflow. At the expiration of the financing 
period, the payment to the nonresident supplier will 
involve either a drawdown of foreign assets (e.g., foreign deposits held by domestic banks) or the replacement of the liability to the nonresident supplier by 
another liability to nonresidents. There are also close 
connections between many financial account transactions. For example, the proceeds from the sale of bonds 
in foreign financial markets (a financial inflow) may 
be invested temporarily in short-term assets abroad (a 
financial outflow


> 3 Thus the net provision of resources to or from 
the rest of the world, as measured by the current and 
capital account balances, must—by definition—be 
matched by a change in net claims on the rest of the 
world. For example, a surplus on the current and capital 
accounts is reflected in an increase in net claims, which 
may be in the form of acquisition of reserve assets on 
the part of the monetary authorities or other official or 
private claims on nonresidents. Alternatively, a deficit 
on the current and capital accounts implies that the 
net acquisition of resources from the rest of the world 
must be paid for by either liquidating foreign assets or 
increasing liabilities to nonresidents

"change in NET CLAIMS"? Might be a term to use?

TODO: read the end of chapter 15 in more detail when it talks about implications and crises

> One important aspect of monetary policy in 
balance of payments adjustment is the link between 
reserve asset transactions and domestic monetary conditions. A decline in reserve assets may be associated 
with a current account deficit or a net financial outflow 
caused by an expansionary monetary policy or both. 
The reserve asset decline can lead to a reduction in 
the monetary base and therefore to a tightening in the 
stance of monetary policy.
A more restrictive monetary policy tends to correct the payments imbalance 
through higher interest rates that dampen domestic 
demand and make domestic assets more attractive to 
investors. However, this built-in adjustment mechanism 
can be short-circuited if the monetary authorities offset 
the effect of the loss of reserve assets on the monetary 
base by increasing the domestic component of the base 
(e.g., through open-market purchases of securities held 
by the banking system). Such offsetting action tends to 
prevent domestic interest rates from rising and thereby 
contributes to the persistence of the balance of payments deficit.

TODO: reread blurb about resource curse. good summary





11.
data.imf.org has some datasets that could be useful for class exercises.
Bit messy and hard to download albiet.






12
Mankiw says "net foreign investment" is another term for "net capital outflows"
I can find that one on BEA
https://www.bea.gov/help/glossary/balance-current-account-national-income-and-product-accounts
Here's an example of a .gov source that uses the phrase:
https://www.cbo.gov/sites/default/files/113th-congress-2013-2014/workingpaper/45140-NSPDI_workingPaper_1.pdf
Here's a couple more
https://home.treasury.gov/system/files/226/1-23-03speech.pdf
https://crsreports.congress.gov/product/pdf/RL/RL32964/29
(The latter is related to IIP which I should familiarize myself with.)
(and IMFBPM talks about changes in net foreign asset position)



---

Net lending as measured by financial account seems much noiser than as measured by current+capital account

https://fred.stlouisfed.org/graph/?id=IEABC,IEANLC,IEANLF,
compare also:
https://fred.stlouisfed.org/release/tables?rid=52&eid=812337#snid=812385
https://fred.stlouisfed.org/graph/?id=ADSLBAQ027S,ADSLFAQ027S,
https://fred.stlouisfed.org/graph/?id=ADSLBAQ027S,ADSLFAQ027S,RWLBACQ027S
https://fred.stlouisfed.org/series/RWLBACQ027S






---



from link 2:
"● Financial transactions are classified into five functional categories: direct investment, portfolio 
investment, other investment, reserve assets (assets 
only), and financial derivatives. Similarly, transactions in primary investment income are classified 
into four functional categories: direct investment, 
portfolio investment, other investment, and reserve 
assets (receipts only). "


Unrelated:
FRED International Indexes of Consumer Prices
https://fred.stlouisfed.org/release?rid=201
Discounted in 2012. Annoying

Unrelated:
A Millennium of Macroeconomic Data for the UK
https://fred.stlouisfed.org/release?t=&et=&rid=389

unrelated: goodness! this is so cool!
https://kagi.com/smallweb
Here are the first two I clicked on:
https://www.ciccarello.me/posts/2024/11/09/b-birthday/
https://pc.blogspot.com/2024/11/the-ungrateful-pedestrian-or-when-do.html

https://guides.library.cornell.edu/datasources/InternationalEconomic



TODO: Graph of national saving and investment like Mankiw has.
Private saving doesn't work at all. 
Gross saving lines up with investment pretty well but I don't think that's what I'm looking for. Is it?
https://fred.stlouisfed.org/graph/?g=1AP3p
It might be actually. Hrm.
And I could always manually calculate it using Y-C-G but that's cheating.
I also tried looking at (disposable income - C)+gov surplus, but that goes super duper negative.
https://fred.stlouisfed.org/graph/?g=1AP9p
Might be thinking about this wrong, and it's a tangent, anyways.


Principle Federal Economic Indicators are kinda sorta listed on homepage of https://www.bea.gov/
Full list seems a bit too broad to be used as a course outline.
https://www.whitehouse.gov/wp-content/uploads/2024/09/pfei_schedule_release_dates_cy2025_09202024.pdf
I guess you could just use the BEA/BLS stuff.
https://www.bls.gov/eag/abouteag.htm

-->

