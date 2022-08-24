---
title: Graph Test
subtitle: This will be deleted soon
parent: 3102 Notes
grand_parent: Teaching
layout: post
nav_order: 20
last_modified_date: 2022-08-23
---


<link href="https://kineticgraphs.org/css/kg.0.2.6.css" rel="stylesheet" type="text/css">
<script src="https://kineticgraphs.org/js/kg.0.2.6.js"></script>

<div class="kg-container">

params:
- {name: a, value: 3, min: 0, max: 10, round: 0.1}
- {name: y1, value: 3, min: 0, max: 10, round: 0.1}
- {name: y2, value: 3, min: 0, max: 10, round: 0.1}
- {name: r, value: 0.25, min: 0, max: 3, round: 0.05}
calcs:
  we1: "(params.y1+params.y2/(1+params.r))"
  we2: "(params.y2+(1+params.r)*params.y1)"


layout:
  OneGraphPlusSidebar:
    graph:
      objects:
      
      - EconBudgetLine:
          p1: 1
          p2: 1/(1+params.r)
          m: calcs.we1
          label: {text: Budget, location: 0.9}
      
      
      - Curve: 
          univariateFunction: 
            fn: (sin(x))*params.a
            ind: x
            
      - Curve: 
          univariateFunction: 
            fn: calcs.we2 - x*(1+params.r)
            ind: x
            max: params.y1+1
          color: red
          label:
            text: "'f(x) = 1 + 2x'"
            x: 2
            y: 3
            align: left

      # Point object at coordinates (6,4)
      - Point:
          coordinates: [6,4]
          label:
            text: A

      # Red point object at coordinates (3,3)
      - Point:
          coordinates: [params.y1,params.y2]
          color: red
          label:
            text: \text{E}
          drag: 
            - horizontal: y1
            - vertical: y2

    sidebar:
      controls:
      - title: Exogenous Variables
        sliders:
        - {param: a, label: a}
        - {param: y1, label: y}
        - {param: y2, label: y^\prime}
        - {param: r, label: r}

</div>




<div class="kg-container">

schema: EconSchema
layout:
  OneGraph:
    graph:
      xAxis: 
        title: "Good 1"
      yAxis: 
        title: "Good 2"
      objects: 
      - EconBudgetLine:
          p1: 1
          p2: 2
          m: 8
          label: {text: M, location: 0.9}
      - EconBudgetLine:
          p1: 2
          p2: 1
          m: 8
          color: blue
          label: {text: M, location: 0.9}

</div>