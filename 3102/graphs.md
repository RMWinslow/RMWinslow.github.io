---
title: 3102 Graphs
parent: Intermediate Macro Notes
grand_parent: Notes
layout: post
toc: false
nav_exclude: true
date: 2022-08-23
last_modified_date: 2023-09-20
---

<!--
https://www.econgraphs.org/
https://kineticgraphs.org/
https://github.com/cmakler/kgjs
https://www.econgraphs.org/textbook
-->

<link href="https://kineticgraphs.org/css/kg.0.2.6.css" rel="stylesheet" type="text/css">
<script src="https://kineticgraphs.org/js/kg3d.0.2.6.js"></script>


## One Period Competitive Equilibrium


### Consumer's Problem

<div class="kg-container" src="./graphs/onePeriodConsumer.yml" clearColor='#fff0'></div>


### Producer's Problem

<div class="kg-container" src="./graphs/onePeriodProducer.yml" clearColor='#fff0'></div>

### Consumer and Producer's Problem Combined

<div class="kg-container" src="./graphs/onePeriodBothAgents.yml" clearColor='#fff0'></div>

### Equilibrium






## Two Period Endowment Economy


### Basic Model without Credit Market Imperfections


<div class="kg-container" src="./graphs/twoPeriodEndowment.yml" clearColor='#fff0'></div>

<!--
Cobb Douglass preferences are equivalent to log plus beta log preferences when alpha = 1/(1+beta) ???
      - ContourMap:
          levels: [0,1,1.5,2,2.5,3, params.utility]
          fn: "log(x)+params.b*log(y)"

      - EconIndifferenceMap:
          utilityFunction:
            CobbDouglas: {alpha: 1/(1+params.b)}
          levels: [1,2,3,4,5, calcs.utility]
      
-->




### Interest Rate Spread


<div class="kg-container" src="./graphs/twoPeriodInterestRateSpread.yml" clearColor='#fff0'></div>

<!--See also here: https://www.econgraphs.org/graphs/micro/exchange/intertemporal_choice/different_rates-->


### Collateral Constraints

<div class="kg-container" src="./graphs/twoPeriodCollateralConstraint.yml" clearColor='#fff0'></div>







## Two Period Economy with Labor

<div class="kg-container" src="./graphs/twoPeriodEquilibrium.yml" clearColor='#fdf6e3'></div>



---

The above graphs are made using Chris Makler's open source [KineticGraphs JavaScript Engine](https://github.com/cmakler/kgjs)

See also [the previous versions of these graphs](graphs2).



