# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:04:15 2020

@author: RobertWinslow
"""


import numpy as np
import matplotlib.pyplot as plt

length = 100
timePeriods = range(0,length)


#%% Formula for individual risk 

def riskOfInfection(n,r):
    '''n is number of infectious neighbors.
    This function returns the chance of getting at least one success 
    (infection) on a bernoulli trial with probability r'''
    return (1-(1-r)**n)



#%% Parameters
ε = 0.001 #initial infected percentage
η = 20 #number of neighbors each person has
rate = 0.3  #chance that an I neighbor spreads to a S neighbor.

types = [1,2,3]  #Type 1 = extraverts, type2=intermediaries, type3 = introverts
N = {1: 1/3, 2: 1/3, 3: 1/3}   #Population mass of each group.
#Connections between groups in terms of number of neighbors. With equal mass it should be same both ways.
neighbors = {}
nieghbors[(1,1): 20,]




#%% Generate path
#simplified version that doesn't use actual rates of spread on network. "density dependent"
