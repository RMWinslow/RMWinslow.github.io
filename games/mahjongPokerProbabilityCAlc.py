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

pokerdeck = [suit+str(rank) for suit in ['C','S','H','D'] for rank in [1,2,3,4,5,6,7,8,9,'T','J','Q','K']]

deck = (pipcards+specialcards)
deck = [suit+str(rank) for suit in suits for rank in range(1,5)]
deck = pokerdeck


#%% Poker Hand Counts

handTypeCount = {"5 of a kind": 0, "Straight Flush": 0, "4 of a kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "3 of a kind": 0, "2 pair": 0, "1 pair":0, "High card":0}

'''
For deck = pipcards+specialcards:, 
{ '5 of a kind':        117,
 'Straight Flush':      499
 '4 of a kind':         10956,
 'Full House':          17463,
 'Flush':               43693,                  !!!
 'Straight':            18632,
 '3 of a kind':         220069,
 '2 pair':              258201,
 '1 pair':              1882858,
 'High card':           1999608,}         



For deck = (pipcards+specialcards)*4:, 
{ '5 of a kind':    22970048,
 'Straight Flush':  244840,                    !!!
 '4 of a kind':     13366628,
 'Full House':      20845041,
 'Flush':           22970048,                  
 'Straight':        18171572,
 '3 of a kind':     264790047,
 '2 pair':          299230109,
 '1 pair':          2388575191,
 'High card':       2730503184,}              



For deck = pokerdeck
'''

#%% Mahjong Hand Counts
'''
Pair = Two identical
Chow = flush run of three
Pung = three identical
kong = 4 identical
'''

MahjongHandTypeCount = {"Kong": 0, "Chow": 0, "Pair": 0, "Pung": 0, "Pair+Chow": 0, "Pair+Pung": 0, "2 Pair": 0, "High":0, "Pung+Chow":0}

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
        print(c1,c2,c3,c4,c5)
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
            coinRanks.append(int(card[1]))
        elif card[0]=='S':
            stringRanks.append(int(card[1]))
        elif card[0]=='M':
            wanRanks.append(int(card[1]))
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
        return "Chow"
    elif countcounts[2] == 2:
        return "2 Pair"
    elif countcounts[2]:
        return "Pair"
    else:
        return "High"

#%% Lazy way to loop through possible combinations in canonical order

count = 0


'''for i1, c1 in enumerate(deck[:len(deck)-5]):
    for i2, c2 in enumerate(deck[i1+1:len(deck)-4]):
        for i3, c3 in enumerate(deck[i2+1:len(deck)-3]):
            for i4, c4 in enumerate(deck[i3+1:len(deck)-2]):
                for i5, c5 in enumerate(deck[i4+1:len(deck)-1]):
                    for i6, c6 in enumerate(deck[i5+1:]):
                        count += 1'''
                        
'''for i1, c1 in enumerate(deck[:len(deck)-4]):
    for i2, c2 in enumerate(deck[i1+1:len(deck)-3]):
        for i3, c3 in enumerate(deck[i1+i2+2:len(deck)-2]):
            for i4, c4 in enumerate(deck[i1+i2+i3+3:len(deck)-1]):
                for i5, c5 in enumerate(deck[i1+i2+i3+i4+4:len(deck)-0]):
                    handTypeCount[analyzePokerHand(c1,c2,c3,c4,c5)] +=1
                    #MahjongHandTypeCount[analyzeMiniMahjongHand(c1,c2,c3,c4,c5)] +=1
                    #print(c1,c2,c3,c4,c5)'''
                    




#%% Everything above is borked so I am starting over

count = 0

handTypeCount = {"5 of a kind": 0, "Straight Flush": 0, "4 of a kind": 0, "Full House": 0, "Flush": 0, "Straight": 0, "3 of a kind": 0, "2 pair": 0, "1 pair":0, "High card":0}

pokerdeck = [suit+str(rank) for suit in ['C','S','H','D'] for rank in [1,2,3,4,5,6,7,8,9,'T','J','Q','K']]
                           
for combo in itertools.combinations(deck, 5):  # 2 for pairs, 3 for triplets, etc
    handTypeCount[analyzePokerHand(*combo)] += 1
                    
                    