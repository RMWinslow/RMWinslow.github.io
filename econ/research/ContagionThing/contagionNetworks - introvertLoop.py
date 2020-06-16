# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:59:58 2020

@author: RobertWinslow
"""

import random
import time
import matplotlib.pyplot as plt
import numpy as np

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

#Should these be global? No, probably not.
coordsToAgent = dict()
agentSet = set()
agentList = []


class agentObject:

    def __init__(self, coords, infectionChance=globalInfectionChance):
        "Initialize Susceptible agent "
        self.sirState = 'S'
        self.recoveryRate = globalRecoveryRate
        self.infectionChance = infectionChance
        self.coordinates = coords
        self.type = 'introvert'
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
                
    
#Initialize loop of agents, each connected to nearest neighbors
#Unlike the grid, coords are one dimensional and modulo. y coord is set to 0.
#ringSize is number of agents in the loop
#A radius of 2 means the agent is connected to the adjacent agents and the agents adjacent to those.
def initializeRing(ringSize, radiusOfAgentConnections, infectionChance, extraverts=False):
    coordsToAgent.clear()
    agentSet.clear()
    for position in range(ringSize):
        newAgent = agentObject(position,infectionChance)
        agentSet.add(newAgent)
        agentList.append(newAgent)
        coordsToAgent[position] = newAgent
    #After building the ring, go back through and make connections.
    for position in range(ringSize):
        for distance in range(1,radiusOfAgentConnections+1):
            currentAgent = coordsToAgent[position]
            newNeighbor = coordsToAgent[(position+distance)%ringSize]
            connectAgents(currentAgent,newNeighbor)
    if extraverts:
        addExtraverts()
    
def getExtraverts():
    return [agent for location, agent in coordsToAgent.items() if agent.type=="extravert"]

def addExtraverts():
    extraverts = []
    for position in coordsToAgent:
        #if position % 5 == 0:
        if position <20:
            extraverts.append(coordsToAgent[position])
    random.shuffle(extraverts)
    for i in range(len(extraverts)):
        extraverts[i].type = 'extravert'
        connectAgents(extraverts[i], extraverts[(i+1)%len(extraverts)])
            

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
        
def displayRing():           
    for position in coordsToAgent:
        #print(coordsToAgent[(x,y)].sirState, end='')
        print(stateToBlock[coordsToAgent[position].sirState], end='')
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


def runSilentTrial(population,radius,infectionRate, extraverts=False):
    initializeRing(population,radius,infectionRate,extraverts)
    coordsToAgent[0].sirState = 'I'
    timeElapsed = 0
    while checkForInfected():
        advanceTime()
        timeElapsed += 1
    numRecovered = len([agent for agent in agentSet if agent.sirState=='R'])
    portionRecovered = numRecovered / population
    return timeElapsed, portionRecovered
        
        
def runVisibleTrial(population,radius,infectionRate, extraverts=False):
    initializeRing(population,radius,infectionRate, extraverts)
    coordsToAgent[0].sirState = 'I'
    displayRing()
    while checkForInfected():
        advanceTime()
        displayRing()
        time.sleep(0.05)
          

#Run multiple trials
def runMultipleTrials(population,radius,infectionRate,numTrials, extraverts=False):
    timeData = []
    rateData = []
    for _ in range(numTrials):
        timeDatum, rateDatum = runSilentTrial(population,radius,infectionRate,extraverts)
        timeData.append(timeDatum)
        rateData.append(rateDatum)
    return timeData, rateData



#%%

def infectionHistogram(population,radius,infectionRate,numTrials, extraverts=False):
    timeData, rateData = runMultipleTrials(population,radius,infectionRate,numTrials,extraverts)
    
    #plot the times it takes to do stuff
    plt.hist(timeData, range(max(timeData)+1))
    plt.title("timeHist n="+str(population)+" rad="+str(radius)+" rate="+str(infectionRate)+"extraverts="+str(extraverts))
    plt.savefig('img/timeHist_n='+str(population)+" rad="+str(radius)+" rate="+str(infectionRate)+" extraverts="+str(extraverts)+'.png')
    plt.show()
    
    #plot the portion of people who go infected
    plt.hist(rateData, 60)
    plt.title("rateHist n="+str(population)+" rad="+str(radius)+" rate="+str(infectionRate)+"extraverts="+str(extraverts))
    plt.savefig('img/rateHist_n='+str(population)+" rad="+str(radius)+" rate="+str(infectionRate)+" extraverts="+str(extraverts)+'.png')
    plt.show()
    

    
def plotMultipleIRates(population,radius,numTrials, extraverts=False):
    "Iterate through infection rates and plot the average portion of the population infected."
    rateRange = np.linspace(0,1,11) #x axis
    trialResults = dict()
    for infectionRate in rateRange:
        timeData, rateData = runMultipleTrials(population,radius,infectionRate,numTrials, extraverts)
        trialMean = sum(rateData)/len(rateData)
        trialResults[infectionRate] = trialMean
        
    #make the graph
    resultData = [outcome for rate,outcome in trialResults.items()]
    plt.plot(rateRange,resultData)
    plt.title("trial results: n="+str(population)+" rad="+str(radius))
    if extraverts:
        plt.title("extravert trial results: n="+str(population)+" rad="+str(radius))
    plt.xlabel("infection rate")
    plt.ylabel("percent of population infected")
    if extraverts:
        plt.savefig('img/extravert results_n='+str(population)+" rad="+str(radius)+'.png')
    else:
        plt.savefig('img/results_n='+str(population)+" rad="+str(radius)+'.png')
    plt.show()
        
        

#plotMultipleIRates(120,3,1000,False)

runVisibleTrial(120,2,0.6,True)













               
