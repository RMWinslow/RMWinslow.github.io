# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 02:08:17 2020

@author: RobertWinslow
"""

import numpy as np
import matplotlib.pyplot as plt

timePeriods = range(0,100)

#%% Parameters

ε = 0.001 #initial infected percentage
n_ee = 19  #You are extravert. How many extravert neighbors do you have?
n_ei = 1  #You are extravert. How many introvert neighbors do you have?
n_ie = 1  #You are introvert. How many extravert neighbors do you have?
n_ii = 0  #You are introvert. How many introvert neighbors do you have?
rate = 0.09 #chance that an I neighbor spreads to a S neighbor.
#β = rate*η #average number of potential infection events per person.



#%% Generate path
#simplified version that doesn't use actual rates of spread on network. "density dependent"

#percentages of people in each state:
SPath_extraverts = [1-ε] 
IPath_extraverts = [ε]
RPath_extraverts = [0]
SPath_introverts = [1-ε] 
IPath_introverts = [ε]
RPath_introverts = [0]


for t in timePeriods[1:]:
    S_e = SPath_extraverts[-1]
    I_e = IPath_extraverts[-1]
    R_e = RPath_extraverts[-1]
    S_i = SPath_introverts[-1]
    I_i = IPath_introverts[-1]
    R_i = RPath_introverts[-1]
    
    newR_e = R_e + I_e
    newI_e = S_e*rate*(n_ee*I_e + n_ei*I_i) #term in parens is num of infected neighbors
    newS_e = S_e - newI_e
    
    newR_i = R_i + I_i
    newI_i = S_i*rate*(n_ie*I_e + n_ii*I_i)
    newS_i = S_i - newI_i

    SPath_extraverts.append(newS_e)
    IPath_extraverts.append(newI_e)
    RPath_extraverts.append(newR_e)
    SPath_introverts.append(newS_i)
    IPath_introverts.append(newI_i)
    RPath_introverts.append(newR_i)
    
#%%Aggregate over types

SPath = [e + i for e, i in zip(SPath_extraverts, SPath_introverts)] 
IPath = [e + i for e, i in zip(IPath_extraverts, IPath_introverts)] 
RPath = [e + i for e, i in zip(RPath_extraverts, RPath_introverts)] 
    
#%% Plot Results

plt.plot(timePeriods, SPath)
plt.plot(timePeriods, IPath)
plt.plot(timePeriods, RPath)
plt.show()

plt.plot(timePeriods, SPath_extraverts)
plt.plot(timePeriods, IPath_extraverts)
plt.plot(timePeriods, RPath_extraverts)
plt.show()


plt.plot(timePeriods, SPath_introverts)
plt.plot(timePeriods, IPath_introverts)
plt.plot(timePeriods, RPath_introverts)
plt.show()


