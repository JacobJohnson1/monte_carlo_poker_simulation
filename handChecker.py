from pickle import TRUE
import re
from ctypes import sizeof

# RENAME: THIS IS JUST FOR PRINTING OUT?
# def checkHands(myHand, hand2, hand3, hand4, hand5, hand6):
#     f = open("output.txt", "w")
#     f.write(myHand)
#     f.close

def convertLists(listOfStrings):
    listOfInts = []
    convertibleStr = ''
    for i in range(0, len(listOfStrings)-1):
        convertibleStr += (listOfStrings[i] + " ")
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

def highCard(handList):
    numericalVals = convertLists(handList)
    highest = numericalVals[0]
    for i in range(1, len(numericalVals)):
        if numericalVals[i] > highest:
            highest = numericalVals[i]
    handList[-1] += highest

def pairCheck(handList):
    onePairConst = 13
    twoPairConst = 23
    numericalVals = convertLists(handList)
    pairs = []
    for i in numericalVals:
        if numericalVals.count(i) == 2:
            pairs.append(i)
            numericalVals.remove(i)
    if len(pairs) == 1:
        handList[-1] += (pairs[0] + onePairConst)
    if len(pairs) == 2:
        handList[-1] += (pairs[0] + pairs[1] + twoPairConst)

def threeOfAKind(handList):
    threeOAKConst = 49
    numericalVals = convertLists(handList)
    triple = []
    for i in numericalVals:
        if numericalVals.count(i) == 3:
            triple.append(i)
            numericalVals.remove(i)
    if triple:
        handList[-1] += (triple[0] + threeOAKConst)

def straight(handList):
    straightScore = 0
    straightConst = 49
    numericalVals = convertLists(handList)
    numericalVals = sorted(numericalVals)
    span = (numericalVals[-1] - numericalVals[0])
    lowStraightConst = 13
    if span == 4:
        for i in range(0, len(numericalVals)):
            straightScore += numericalVals[i]
        handList[-1] += (straightScore + straightConst)
    elif lowStraight(numericalVals):
        for i in range(0, len(numericalVals)):
            straightScore += numericalVals[i]
        handList[-1] += (straightScore - lowStraightConst + straightConst)

def lowStraight(numericalVals):
    numericalVals = sorted(numericalVals)
    if numericalVals == [2, 3, 4, 5, 14]:
        return TRUE

def flush(handList):
    flushConst = 104
    straightFlushConst = 234
    straightFlushScoring = 0
    onlySuits = isolateSuits(handList)
    numericalVals = convertLists(handList)
    numericalVals = sorted(numericalVals)
    span = (numericalVals[-1] - numericalVals[0])
    highest = numericalVals[0]
    for i in range(1, len(numericalVals)):
        if numericalVals[i] > highest:
            highest = numericalVals[i]
    if ((len(set(onlySuits)) == 1) and (span == 4)):
        for i in range(0, len(numericalVals)):
            straightFlushScoring += numericalVals[i]
        handList[-1] += (straightFlushScoring + straightFlushConst)
    elif len(set(onlySuits)) == 1 and lowStraight(numericalVals):
        for i in range(0, len(numericalVals)):
            straightFlushScoring += numericalVals[i]
        handList[-1] += (straightFlushScoring + straightFlushConst)
    elif len(set(onlySuits)) == 1:
        handList[-1] += (highest + flushConst)

def fullHouse(handList):
    fullHouseConst = 100
    numericalVals = convertLists(handList)
    pair = []
    for i in numericalVals:
        if numericalVals.count(i) == 2:
            pair.append(i)
            numericalVals.remove(i)
    triple = []
    for i in numericalVals:
        if numericalVals.count(i) == 3:
            triple.append(i)
            numericalVals.remove(i)
    if triple and pair:
        handList[-1] += ((triple[0] * 8) + pair[0] + fullHouseConst)

def fourOfAKind(handList):
    fourOAKConst = 221 #maybe take away 13 from this #?
    numericalVals = convertLists(handList)
    quads = []
    for i in numericalVals:
        if numericalVals.count(i) == 4:
            quads.append(i)
            numericalVals = list(set(numericalVals))
            numericalVals.remove(i)
            handList[-1] += (quads[0] + fourOAKConst)
            numericalVals = [str(i) for i in numericalVals]
            numericalVals.append(handList[-1])
            highCard(numericalVals)
            handList[-1] = numericalVals[-1]

# create a function to keep checking for next highest card in case of tie

def score(myHand):
    flush(myHand)
    straight(myHand)
    fourOfAKind(myHand)
    fullHouse(myHand)
    threeOfAKind(myHand)
    pairCheck(myHand)
    highCard(myHand)
    print(myHand)