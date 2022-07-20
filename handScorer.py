from pickle import TRUE
import re
from ctypes import sizeof
from tkinter import N
from formatAndPrint import handLabeler

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
    numVals = set(numVals)
    numVals = list(numVals)
    if triple:
        if triple[0] in numVals:
            numVals.remove(triple[0])
        if len(numVals) == 2:
            handList[-1] += threeOAKConst + triple[0] + min(numVals)/1000 + max(numVals)/100


def straight(handList):
    straightConst = 60
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    span = (numVals[-1] - numVals[0])
    setSize = set(numVals)
    if span == 4 and setSize == 5:
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
        handList[-1] += (flushConst + numVals[0]/100000 + numVals[1]/10000 + numVals[2]/1000 + numVals[3]/100 + numVals[4])

def fullHouse(handList):
    fullHouseConst = 90
    numVals = convertLists(handList)
    numValSet = set(numVals)
    if len(numValSet) == 2:
        triple = []
        double = []
        for i in numVals:
            if numVals.count(i) == 3:
                triple.append(i)
        size_of_numVals = len(numVals)
        for i in numVals:
            while i < size_of_numVals:
                if (triple) and (numVals[i] != triple[0]):
                    double.append(i)
                if len(double) == 2:
                    handList[-1] += (fullHouseConst + triple[0] + double[0]/100)

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
    if currentHand[-1] == 0:
        pairCheck(currentHand)
        threeOfAKind(currentHand)
    if currentHand[-1] == 0:
        highCardTieBreaker(currentHand)
