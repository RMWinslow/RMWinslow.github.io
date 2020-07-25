# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 02:08:17 2020

@author: RobertWinslow
"""

import numpy as np
import matplotlib.pyplot as plt

length = 100
timePeriods = range(0,length)

#%% Parameters

ε = 0.001 #initial infected percentage
η = 20 #number of neighbors each person has
rate = 0.08 #chance that an I neighbor spreads to a S neighbor.
β = rate*η #average number of potential infection events per person.



#%% Generate path
#simplified version that doesn't use actual rates of spread on network. "density dependent"

#percentages of people in each state:
SPath = [1-ε] 
IPath = [ε]
RPath = [0]


for t in timePeriods[1:]:
    S = SPath[-1]
    I = IPath[-1]
    R = RPath[-1]
    
    newR = R + I
    newI = β*S*I
    newS = S - newI

    SPath.append(newS)
    IPath.append(newI)
    RPath.append(newR)
    
    
#%% Plot Results

plt.plot(timePeriods, SPath)
plt.plot(timePeriods, IPath)
plt.plot(timePeriods, RPath)
plt.plot(timePeriods, [2/β-1]*length)
plt.show()