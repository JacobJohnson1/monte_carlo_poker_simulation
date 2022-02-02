# import dealHandsAndShuffle
import re
from ctypes import sizeof


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
    for x in range(0, len(handList)):


# def straight(handList):
#     for x in range(0, len(handList)):

# def flush(handList):
#     for x in range(0, len(handList)):
                          
# def fullHouse(handList):
#     for x in range(0, len(handList)):
  

# Append numerical score to the end of list (hand) as string