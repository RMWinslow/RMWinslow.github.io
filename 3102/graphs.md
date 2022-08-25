---
title: 3102 Graphs
parent: 3102 Notes
grand_parent: Teaching
layout: post
nav_order: 20
date: 2022-08-23
last_modified_date: 2022-08-24
---


<link href="https://kineticgraphs.org/css/kg.0.2.6.css" rel="stylesheet" type="text/css">
<script src="https://kineticgraphs.org/js/kg3d.0.2.6.js"></script>


## One Period Competitive Equilibrium


### Consumer's Problem

<div class="kg-container" src="./graphs/onePeriodConsumer.yml" clearColor='#fff0'></div>


### Producer's Problem

<div class="kg-container" src="./graphs/onePeriodProducer.yml" clearColor='#fff0'></div>

### Consumer and Producer's Problem Combined

<div class="kg-container" src="./graphs/onePeriodBoth Agents.yml" clearColor='#fff0'></div>

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



