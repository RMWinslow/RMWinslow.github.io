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
<script src="https://kineticgraphs.org/js/kg.0.2.6.js"></script>


## Two Period Endowment Economy


### Basic Model without Credit Market Imperfections


<div class="kg-container">

schema: EconSchema
params:
- {name: a, value: 3, min: 0, max: 10, round: 0.1}
- {name: y1, value: 3, min: 0, max: 10, round: 0.1}
- {name: y2, value: 3, min: 0, max: 10, round: 0.1}
- {name: t1, value: 0, min: -10, max: 10, round: 0.1}
- {name: t2, value: 0, min: -10, max: 10, round: 0.1}
- {name: b, value: 0.8, min: 0, max: 1, round: 0.05}
- {name: r, value: 0.25, min: 0, max: 3, round: 0.05}
calcs:
  we1: "(params.y1-params.t1+(params.y2-params.t2)/(1+params.r))"
  we2: "(calcs.we1 * (1+params.r))"
  c1: "(calcs.we1 / (1+params.b))"
  c2: "(calcs.c1 * params.b * (1+params.r))"
  s: "(calcs.y1 - calcs.t1 - calcs.c1)"
  utility: "(log(calcs.c1)+params.b*log(calcs.c2))"
  MRS: "(calcs.c2/(params.b*calcs.c1))"

layout:
  OneGraphPlusSidebar:
    graph:
    
      xAxis: 
        title: "$c$: Consumption Today"
      yAxis: 
        title: "$c'$: Consumption Tomorrow"

      objects:
      
      
      - ContourMap:
          levels: [0,1,1.5,2,2.5,3, params.utility]
          fn: "log(x)+params.b*log(y)"
      
      - EconBudgetLine:
          p1: 1
          p2: 1/(1+params.r)
          m: calcs.we1
          label: None


      # Endowment Point
      - Point:
          coordinates: [params.y1-params.t1,params.y2-params.t2]
          color: green
          label:
            text: \text{E}
          drag: 
            - horizontal: y1
            - vertical: y2


      # Optimum Point
      - Point:
          coordinates: [calcs.c1,calcs.c2]
          color: red
          label:
            text: \text{★}

    sidebar:
      controls:
      - title: Exogenous Variables
        sliders:
        - {param: a, label: a}
        - {param: y1, label: y}
        - {param: y2, label: y^\prime}
        - {param: t1, label: t}
        - {param: t2, label: t^\prime}
        - {param: r, label: r}
        - {param: b, label: \beta}

</div>









