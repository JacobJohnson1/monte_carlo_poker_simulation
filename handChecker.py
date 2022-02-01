# import dealHandsAndShuffle


import re
from ctypes import sizeof


def checkHands(myHand, hand2, hand3, hand4, hand5, hand6):
    
    f = open("output.txt", "w")

    f.write(myHand)
    f.close

# FUNCTIONS:
def highCard(handList):
    numericalValues = []
    handListStr = (handList[0] + " " + handList[1] + " " + handList[2] + " " + handList[3] + " " + handList[4])
    numericalValues = (re.findall(r'\d+', handListStr))
    numericalValues = [int(i) for i in numericalValues]
    highest = numericalValues[0]
    for i in range(1,4):
        if numericalValues[i] > highest:
            highest = numericalValues[i]
    handList[5] += highest

# def onePair(handList):
#     pairBool = None
#     for x in range(0, len(handList)):
#         # do something
#     return pairBool
        
# def twoPair(handList):
#     for x in range(0, len(handList)):
        
# def threeOfAKind(handList):
#     for x in range(0, len(handList)):


# def straight(handList):
#     for x in range(0, len(handList)):

# def flush(handList):
#     for x in range(0, len(handList)):
                          
# def fullHouse(handList):
#     for x in range(0, len(handList)):
  

# Append numerical score to the end of list (hand) as string