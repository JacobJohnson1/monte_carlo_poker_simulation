from pickle import TRUE
import re
from ctypes import sizeof

def convertLists(listOfStrings):
    listOfInts = []
    convertibleStr = ''
    for i in range(0, len(listOfStrings)-1):
        convertibleStr += (str(listOfStrings[i]) + " ")
    listOfInts = (re.findall(r'\d+', convertibleStr))
    listOfInts = [int(i) for i in listOfInts]
    return listOfInts

def isolateSuits(handList):
    listOfSuits = []
    convertibleStr = ''
    for i in range(0, len(handList)-1):
        convertibleStr += (handList[i])
    listOfSuits = (re.findall(r'\D', convertibleStr))
    return listOfSuits

def highCardTieBreaker(handList):
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    handList[-1] += (numVals[0]/100000 + numVals[1]/10000 + numVals[2]/1000 + numVals[3]/100 + max(numVals))

def pairCheck(handList):
    onePairConst = 14
    twoPairConst = 30
    numVals = convertLists(handList)
    pairs = []
    for i in numVals:
        if numVals.count(i) == 2:
            pairs.append(i)
            numVals.remove(i)
    notPairs = [x for x in numVals if x not in pairs]
    sorted(notPairs)
    if len(pairs) == 1:
        handList[-1] += (onePairConst + pairs[0] + notPairs[0]/10000 + notPairs[1]/1000 + notPairs[2]/100)
    if len(pairs) == 2:
        numVals = sorted(numVals)
        handList[-1] += (twoPairConst + max(pairs) + min(pairs)/100 + notPairs[0]/1000)

def threeOfAKind(handList):
    threeOAKConst = 45
    numVals = convertLists(handList)
    triple = []
    for i in numVals:
        if numVals.count(i) == 3:
            triple.append(i)
            numVals.remove(i)
    notPairs = [x for x in numVals if x not in triple]
    if triple:
        handList[-1] += threeOAKConst + triple[0] + max(notPairs)/100 + min(notPairs)/1000

def straight(handList):
    straightConst = 60
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    span = (numVals[-1] - numVals[0])
    if span == 4:
        handList[-1] += (max(numVals) + straightConst)
    elif numVals == [2,3,4,5,14]:
        handList[-1] += (numVals[3] + straightConst)

def flush(handList):
    flushConst = 75
    straightFlushConst = 58
    onlySuits = isolateSuits(handList)
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    span = (numVals[-1] - numVals[0])
    if ((len(set(onlySuits)) == 1) and (span == 4)):
        handList[-1] += (max(numVals) + flushConst + straightFlushConst)
    elif len(set(onlySuits)) == 1 and numVals == [2,3,4,5,14]:
        handList[-1] += (numVals[3] + flushConst + straightFlushConst)
    elif len(set(onlySuits)) == 1:
        handList[-1] += (max(numVals) + flushConst)

def fullHouse(handList):
    fullHouseConst = 90
    numVals = convertLists(handList)
    pair = []
    for i in numVals:
        if numVals.count(i) == 2:
            pair.append(i)
            numVals.remove(i)
    triple = []
    for i in numVals:
        if numVals.count(i) == 3:
            triple.append(i)
            numVals.remove(i)
    if triple and pair:
        handList[-1] += (triple[0] + pair[0] + fullHouseConst)

def fourOfAKind(handList):
    fourOfAKindConst = 118
    numVals = convertLists(handList)
    quads = []
    for i in numVals:
        if numVals.count(i) == 4:
            quads.append(i)
            remainingCard = [x for x in numVals if x not in quads]
            handList[-1] += (fourOfAKindConst + quads[0] + remainingCard[0]/100)

def score(currentHand):
    flush(currentHand)
    straight(currentHand)
    fourOfAKind(currentHand)
    fullHouse(currentHand)
    threeOfAKind(currentHand)
    pairCheck(currentHand)
    if currentHand[-1] == 0:
        highCardTieBreaker(currentHand)
    return(currentHand[-1])