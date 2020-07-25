# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 22:12:20 2020

@author: RobertWinslow
"""

import numpy as np
import matplotlib.pyplot as plt


#%% First, a discrete form

#initial mass of each type
I_1 = 1
I_2 = 1
I = I_1+I_2

#nieghbor connectsion and transmission rate
n_11 = 12
n_21 = 0
n_12 = 0
n_22 = 6
r=1

for timeperiod in range(100):
    new_I_1 = r*( I_1*n_11 + I_2*n_21 )
    new_I_2 = r*( I_1*n_12 + I_2*n_22 )
    I_1 = new_I_1
    I_2 = new_I_2
    #print("I_1:",I_1,"I_2:",I_2, "Φ_1:", I_1/(I_1+I_2))
    print("Φ_1:", I_1/(I_1+I_2))
    
    
