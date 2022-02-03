# import dealHandsAndShuffle
import re
from ctypes import sizeof

# RENAME: THIS IS JUST FOR PRINTING OUT?
def checkHands(myHand, hand2, hand3, hand4, hand5, hand6):
    f = open("output.txt", "w")
    f.write(myHand)
    f.close

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
    numericalVals = convertLists(handList)
    pairs = []
    for i in numericalVals:
        if numericalVals.count(i) == 2:
            pairs.append(i)
            numericalVals.remove(i)
    if len(pairs) == 1:
        handList[-1] += (pairs[0] + 13)
    if len(pairs) == 2:
        handList[-1] += (pairs[0] + pairs[1] + 23)

def threeOfAKind(handList):
    numericalVals = convertLists(handList)
    triple = []
    for i in numericalVals:
        if numericalVals.count(i) == 3:
            triple.append(i)
            numericalVals.remove(i)
    handList[-1] += (triple[0] + 49)

# HOW TO HANDLE LOWEST STRAIGHT: A-2-3-4-5???
def straight(handList):
    numericalVals = convertLists(handList)
    numericalVals = sorted(numericalVals)
    span = (numericalVals[-1] - numericalVals[0])
    straightScore = 0
    if span == 4:
        for i in range(0, len(numericalVals)):
            straightScore += numericalVals[i]
        handList[-1] += (straightScore + 44)

def flush(handList):
    onlySuits = isolateSuits(handList)
    numericalVals = convertLists(handList)
    highest = numericalVals[0]
    for i in range(1, len(numericalVals)):
        if [i] > numericalVals:
            highest = numericalVals[i]
    if (len(set(onlySuits)) == 1) and is-a-straight and are royals:
        # royal flush scoring
    elif (len(set(onlySuits)) == 1) and is-a-straight:
        # straight flush scoring
    elif len(set(onlySuits)) == 1:
        # BASIC FLUSH
        handList[-1] += (highest + 98)

def fullHouse(handList):
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
    # REMOVE LATER
    print(triple)
    print(pair)
    handList[-1] += ((triple[0] * 8) + pair[0] + 94)

def fourOfAKind(handList):
    numericalVals = convertLists(handList)
    quads = []
    for i in numericalVals:
        if numericalVals.count(i) == 4:
            quads.append(i)
            numericalVals = list(set(numericalVals))
            numericalVals.remove(i)
            handList[-1] += ((quads[0] + 13) + 202)
            numericalVals = [str(i) for i in numericalVals]
            numericalVals.append(handList[-1])
            highCard(numericalVals)
            handList[-1] = numericalVals[-1]