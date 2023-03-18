---
title: Predicting Unemployment Status
subtitle: My Winning Submission for the MEBDI 2022 Machine Learning Competition
has_children: false
layout: post
parent: Research
---


I participated in the [2022 MEBDI Machine Learning Competition](https://mebdi.squarespace.com/competitions/2022-ml-competition-winner), and took 1st place.


## Executive Summary for My Submission


> I use a set of machine learning tools to predict next-year unemployment status for individuals
in the Current Population Survey, using a subset of variables specified by the MEBDI competition
judges. I use a Decision Tree algorithm, and two regularized linear regressions, and I improve the
classification performance by combining these three classifiers using a hard-voting ensemble. This
combined classifier is able to predict future unemployment in a holdout testing set with 70.95%
accuracy and future non-unemployment (employment or not-in-labor-force) with 79.92% accuracy,
for an average accuracy across classes of 75.44%.
>
> The most important predictive features are a person’s current work/employment status. Essentially, the best signal that someone will be unemployed next year is that they don’t have a job this
year.

[pdf link](pdf/WinslowMebdi22Summary.pdf)



## A Short Note on the Competition Metric

[pdf link](pdf/MEDBI22_metrics_comparison.pdf)

<!--TODO: Post Link to Code-->