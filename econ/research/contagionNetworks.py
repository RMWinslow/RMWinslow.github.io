# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:59:58 2020

@author: RobertWinslow
"""

import random
import time

def chance(p):
    "Returns True with probability p"
    if random.random() <= p:
        return True
    else:
        return False

#%% Description of problem

#People have
#-a position in space, which is the unique identifier
#-Connections in the social graph
#-state which is S, I, or R for Susceptible, Infected, or Recovered

#Each time period:
'''
TODO:
    -Put entire simulation into a class. Advancement/display as a method
    -add diagonal connections
    -create alternate graph where head of row connects to everybody
    -Create alternate graph with local simplices connected into larger simplex
'''

globalInfectionChance = 0.7
globalRecoveryRate = 1
globalWidth = 50
globalHeight = 10

#%% DATA - Keep track of repeated trials in these data structures


#%% MODEL - Build the underlying graph of agents


coordsToAgent = dict()
agentSet = set()


class agent:

    def __init__(self, x, y):
        "Initialize Susceptible agent "
        self.sirState = 'S'
        self.recoveryRate = globalRecoveryRate
        self.infectionChance = globalInfectionChance
        self.xCoord = x
        self.yCoord = y
        self.neighbors = set()

    def riskInfection(self):
        "This triggers when consumer is exposed to someone who is ill."
        if self.sirState == 'S':
            if chance(self.infectionChance):
                self.sirState = 'I'
                
    def recoverAttempt(self):
        "This triggers each period when consumer is ill. Enables them to recover."
        if self.sirState == 'I':
            if chance(self.recoveryRate):
                self.sirState = 'R'
                
                
def connectAgents(agent1,agent2):
    "Adds each agent to the neighbors of the other"
    agent1.neighbors.add(agent2)
    agent2.neighbors.add(agent1)
                
          
#Initialize grid of agents connected to their orthoganal neighbors
def initializeGrid():
    coordsToAgent.clear()
    agentSet.clear()
    for y in range(globalHeight):
        for x in range(globalWidth):
            newAgent = agent(x,y)
            agentSet.add(newAgent)
            coordsToAgent[(x,y)] = newAgent
            if x > 0:
                connectAgents(newAgent,coordsToAgent[(x-1,y)])
            if y > 0:
                connectAgents(newAgent,coordsToAgent[(x,y-1)])
    #Seed initial infection
    coordsToAgent[(1,1)].sirState = 'I'
    
    
def checkForInfected():
    "returns True if anyone is currently infected."
    infectedFlag = False
    for agent in agentSet:
        if agent.sirState == 'I':
            infectedFlag = True
            break
    return infectedFlag


    
            
#%%  VIEW -  Display for the grid of agents
 
stateToBlock = {'S': '░', 'I': '█', 'R': '▓'}

def displayGrid():           
    for y in range(globalHeight):
        for x in range(globalWidth):
            #print(coordsToAgent[(x,y)].sirState, end='')
            print(stateToBlock[coordsToAgent[(x,y)].sirState], end='')
            
        print()
        
                
#%%CONTROL -  Advance time, propogate the disease, etc.

def advanceTime():
    #Get list of current infected
    currentInfected = []
    for agent in agentSet:
        if agent.sirState == 'I':
            currentInfected.append(agent)
    #Give them a chance to be cured
    for agent in currentInfected:
        agent.recoverAttempt()
    #Get list of neighbors of infected and try to infect them
    for agent in currentInfected:
        for neighbor in agent.neighbors:
            neighbor.riskInfection()


#%%LOOPS           


def runSilentTrial():
    initializeGrid()
    while checkForInfected:
        advanceTime()
        
        
def runVisibleTrial():
    initializeGrid()
    displayGrid()
    while checkForInfected():
        advanceTime()
        displayGrid()
        print()
        time.sleep(0.5)
          
























               
