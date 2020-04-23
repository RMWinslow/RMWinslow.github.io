# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:34:23 2020

@author: RobertWinslow
"""
import itertools

suits = ['C','S','M']
ranks = range(1,10)

pipcards = [suit+str(rank) for suit in suits for rank in ranks]

specialcards = ['WE','WN','WS','WW','DR','DG','DB',]
specialcards = ['WE','WN','WS','WW','WR','WG','WB',]

pokerdeck = [suit+str(rank) for suit in ['C','S','H','D'] for rank in [1,2,3,4,5,6,7,8,9,'T','J','Q','K']]

deck = (pipcards+specialcards)*4


#%% Poker Hand Counts

handTypeCount = {"5 of a kind": 0, "Straight Flush": 0, "4 of a kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "3 of a kind": 0, "2 pair": 0, "1 pair":0, "High card":0}

'''
For deck = pipcards+specialcards:, 
{ '5 of a kind':        0,
 'Straight Flush':      15,
 '4 of a kind':         0,
 'Full House':          216,
 'Flush':               363,                  
 'Straight':            1200,
 '3 of a kind':         3969,
 '2 pair':              9072,
 '1 pair':              103005,
 'High card':           160416,}         



For deck = (pipcards+specialcards)*4:, 
{ '5 of a kind':    7128,
 'Straight Flush':  15360,                    
 '4 of a kind':     553344,
 'Full House':      1146240,
 'Flush':           1114224,                  
 'Straight':        1228800,
 '3 of a kind':     14145984,
 '2 pair':          20542896,
 '1 pair':          156913152,
 'High card':       164265984,}           



For deck = (pipcards+specialcards)*4 when dragons and winds are counted as the same suit:, 
{ '5 of a kind':    7128,
 'Straight Flush':  15360,                    
 '4 of a kind':     553344,
 'Full House':      1146240,
 'Flush':           1206672, *                  
 'Straight':        1228800,
 '3 of a kind':     14140224, *
 '2 pair':          20529936, *
 '1 pair':          156860928, * 
 'High card':       164244480,  * }        



For deck = pokerdeck



there are people at harvard who are imaginitive but don't know any economics
take a model you know well and apply it for the people who cant get into the nitty gritty
'''

#%% Mahjong Hand Counts
'''
Pair = Two identical
Chow = flush run of three
Pung = three identical
kong = 4 identical
'''

MahjongHandTypeCount = {"Kong": 0, "Chow": 0, "Pair": 0, "Pung": 0, "Pair+Chow": 0, "Pair+Pung": 0, "2 Pair": 0, "High":0, "Pung+Chow":0, "2Pair+Chow":0}

'''Without duplicate tiles:
    {'2 Pair': 0,
 'Chow': 9225,
 'High': 269031,
 'Kong': 0,
 'Pair': 0,
 'Pair+Chow': 0,
 'Pair+Pung': 0,
 'Pung': 0,
 'Pung+Chow': 0}
    
    
    
    
    with duplicate tiles:
        {'2 Pair': 2576016,
 '2Pair+Chow': 9072,
 'Chow': 9446400,
 'High': 275487744,
 'Kong': 4488,
 'Pair': 70261248,
 'Pair+Chow': 972288,
 'Pair+Pung': 26928,
 'Pung': 1144896,
 'Pung+Chow': 4032}
        '''

#%% Check for various cards

def myInt(c):
    myDict = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'N':101, 'S':201, 'E':301, 'W':401, 'R':502, 'G':602, 'B':702, 'T':10, 'J':11, 'Q':12, 'K':13}
    return myDict[c]

def analyzePokerHand(c1,c2,c3,c4,c5):
    "Returns the highest poker hand type that matches"
    '''
    5 of a kind
    straight flush
    four of a kind
    full house
    flush
    straight
    3 of a kind
    two pair
    one pair
    high card
    '''
    flushTag = (c1[0]==c2[0]==c3[0]==c4[0]==c5[0])
    #ranks = sorted([c1[1],c2[1],c3[1],c4[1],c5[1],])
    #straightTag = (myInt(ranks[4])==myInt(ranks[3])+1==myInt(ranks[2])+2==myInt(ranks[1])+3==myInt(ranks[0])+4)
    ranks = sorted([myInt(c1[1]),myInt(c2[1]),myInt(c3[1]),myInt(c4[1]),myInt(c5[1]),])
    straightTag = (ranks[4]==ranks[3]+1==ranks[2]+2==ranks[1]+3==ranks[0]+4)
    countcounts = [0,0,0,0,0,0]
    for rank in set(ranks):
        countcounts[ranks.count(rank)] += 1
    
    
    if countcounts[5]:
        return "5 of a kind"
    elif flushTag and straightTag:
        return "Straight Flush"
    elif countcounts[4]:
        return "4 of a kind"
    elif countcounts[3] and countcounts[2]:
        return "Full House"
    elif flushTag:
        return "Flush"
    elif straightTag:
        return "Straight"
    elif countcounts[3]:
        return "3 of a kind"
    elif countcounts[2] == 2:
        return "2 pair"
    elif countcounts[2]:
        return "1 pair"
    else:
        return "High card"
    
    
    
    
def maxRun(listofnums):
    listofnums = sorted(listofnums)
    if len(listofnums) <= 1:
        return listofnums
    maxRun = [listofnums[0]]
    currentRun = maxRun = [listofnums[0]]
    for entry in listofnums[1:]:
        if entry == currentRun[-1] + 1:
            currentRun.append(entry)
            if len(currentRun) > len(maxRun):
                maxRun = currentRun
        elif entry == currentRun[-1]:
            continue
        else:
            currentRun = [entry]
    return maxRun
        
    
    
def analyzeMiniMahjongHand(c1,c2,c3,c4,c5):
    "Returns the highest poker hand type that matches"
    '''
    Pair = Two identical
    Chow = flush run of three
    Pung = three identical
    kong = 4 identical
    Pung+Chow
    Pair+Chow
    Pair+Pung
    2 Pair
    High
    '''
    #Check for straights
    coinRanks = []
    stringRanks  = []
    wanRanks = []
    for card in [c1,c2,c3,c4,c5]:
        if card[0]=='C':
            coinRanks.append(myInt(card[1]))
        elif card[0]=='S':
            stringRanks.append(myInt(card[1]))
        elif card[0]=='M':
            wanRanks.append(myInt(card[1]))
    coinRun = len(maxRun(coinRanks))    
    stringRun = len(maxRun(stringRanks))
    wanRun = len(maxRun(wanRanks))    
    
    runFlag = False
    if (coinRun >= 3 or stringRun >= 3 or wanRun >= 3):
        runFlag = True
    
    #check for identical sets
    countcounts = [0,0,0,0,0,0]
    cardset = set([c1,c2,c3,c4,c5])
    for card in cardset:
        countcounts[[c1,c2,c3,c4,c5].count(card)] += 1
        
        
    if countcounts[4]:
        return "Kong"
    elif countcounts[3]:
        if countcounts[2] == 1:
            return "Pair+Pung"
        if runFlag:
            return "Pung+Chow"
        return "Pung"
    elif runFlag:
        if countcounts[2] == 1:
            return "Pair+Chow"
        if countcounts[2] == 2:
            return "2Pair+Chow"
        listofchows.append([c1,c2,c3,c4,c5])
        return "Chow"
    elif countcounts[2] == 2:
        return "2 Pair"
    elif countcounts[2]:
        return "Pair"
    else:
        return "High"

#%% Lazy way to loop through possible combinations in canonical order


count = 0
listofchows = []

                           
for combo in itertools.combinations(deck, 5):  # 2 for pairs, 3 for triplets, etc
    handTypeCount[analyzePokerHand(*combo, )] += 1
    MahjongHandTypeCount[analyzeMiniMahjongHand(*combo, )] += 1
                    
'''for card in deck:    
    count = 0                
    for hand in listofchows:
        if card in hand:
            count += 1
    print(card,count) '''