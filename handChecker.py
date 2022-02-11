from pickle import TRUE
import re
from ctypes import sizeof

# def printingTextFile(myHand):
#     f = open("output.txt", "a")

#     convertLists(myHand)
#     f.write(myHand)
#     f.close

# def printingCSVFile():
#     do stuff

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
    twoPairConst = 30
    numVals = convertLists(handList)
    pairs = []
    for i in numVals:
        if numVals.count(i) == 2:
            pairs.append(i)
            numVals.remove(i)
    # REMOVE ANYTHING IN PAIRS[] FROM NUMERICALVALS[]
    if len(pairs) == 1:
        handList[-1] += (pairs[0] + max(numVals))
    if len(pairs) == 2:
        numVals = sorted(numVals,reverse=True)
        handList[-1] += twoPairConst + max(pairs) + min(pairs)/100 + numVals[0]/1000

def threeOfAKind(handList):
    threeOAKConst = 45 #DON'T THINK THIS IS THE RIGHT VALUE
    numVals = convertLists(handList)
    triple = []
    for i in numVals:
        if numVals.count(i) == 3:
            triple.append(i)
            numVals.remove(i)
    # REMOVE ANYTHING IN TRIPLE[] FROM NUMERICALVALS[]
    if triple:
        handList[-1] += threeOAKConst + triple[0] + max(numVals) + min(numVals)/1000

def straight(handList):
    straightScore = 0
    lowStraightConst = 13
    straightConst = 49 #DON'T THINK THIS IS THE RIGHT VALUE
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    span = (numVals[-1] - numVals[0])
    lowStraightConst = 13
    if span == 4:
        for i in range(0, len(numVals)):
            straightScore += numVals[i]
        handList[-1] += (straightScore + straightConst)
    elif numVals == [2,3,4,5,14]:
        for i in range(0, len(numVals)):
            straightScore += numVals[i]
        handList[-1] += (straightScore - lowStraightConst + straightConst)

# SCORING NEEDS TO BE FIXED HERE
def flush(handList):
    flushConst = 75 #ish
    straightFlushScoring = 0
    onlySuits = isolateSuits(handList)
    numVals = convertLists(handList)
    numVals = sorted(numVals)
    span = (numVals[-1] - numVals[0])
    if ((len(set(onlySuits)) == 1) and (span == 4)):
        for i in range(0, len(numVals)):
            straightFlushScoring += numVals[i]
        handList[-1] += (straightFlushScoring)
    elif len(set(onlySuits)) == 1 and numVals == [2,3,4,5,14]:
        for i in range(0, len(numVals)):
            straightFlushScoring += numVals[i]
        handList[-1] += (straightFlushScoring)
    elif len(set(onlySuits)) == 1:
        handList[-1] += max(numVals) + flushConst

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
    fourOAKConst = 221 #WRONG
    numVals = convertLists(handList)
    quads = []
    for i in numVals:
        if numVals.count(i) == 4:
            quads.append(i)
            numVals = list(set(numVals))
            numVals.remove(i)
            handList[-1] += (quads[0] + fourOAKConst)
            numVals = [str(i) for i in numVals]
            numVals.append(handList[-1])
            max(numVals)
            handList[-1] = numVals[-1]
            numVals = convertLists(numVals)
            handList[-1] += numVals[0]

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