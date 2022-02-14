from concurrent.futures import thread
from dataclasses import dataclass
import random
import handScorer
import formatAndPrint
import os

def createDeck():
    numbers=list(range(2,15))
    suits = ['H','S','C','D']
    deck = []
    for i in numbers:
        for s in suits:
            card = str(i)+s
            deck.append(card)
    return deck

def dealMyHand(deck):
    myHand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop(), 0]
    return myHand

def fillInDataMatrix(winPercentage, matrix, numOfHands, myHand):
    handType = formatAndPrint.occurrenceCounter(myHand, matrix)
    # occurrence percentage
    for i in range(0, len(matrix)):
        matrix[i][1] = ((matrix[i][0]/numOfHands) * 100)
    # [win percentages]
    listOfHandWins = matrix[handType][2]
    listOfHandWins.append(winPercentage)
    # avg win %
    for i in range(0, len(matrix)):
        if len(matrix[i][2]) > 0:
            matrix[i][3] = (int(matrix[i][2][0])/len(matrix[i][2]))

def driverFunction():
    if os.path.isfile('output.txt'):
        os.remove('output.txt')
    if os.path.isfile('output.csv'):
        os.remove('output.csv')

    numOfMyHands = 1000
    
    highCardPercentages = []
    onePairPercentages = []
    twoPairPercentages = []
    threeOAKPercentages = []
    straightPercentages = []
    flushPercentages = []
    fullHousePercentages = []
    fourOAKPercentages = []
    straighFlushPercentages = []
    royalFlushPercentages = []

    # [ occurrence of hand type, percentage of occurrence, [winPercentages], average Win percentages ]
    dataMatrix = [
        [0, 0, highCardPercentages, 0],
        [0, 0, onePairPercentages, 0],
        [0, 0, twoPairPercentages, 0],
        [0, 0, threeOAKPercentages, 0],
        [0, 0, straightPercentages, 0],
        [0, 0, flushPercentages, 0],
        [0, 0, fullHousePercentages, 0],
        [0, 0, fourOAKPercentages, 0],
        [0, 0, straighFlushPercentages, 0],
        [0, 0, royalFlushPercentages, 0]
    ]

    for i in range(0, numOfMyHands):
        numOfGames = 1000
        deck = createDeck()
        random.shuffle(deck)
        myHand = dealMyHand(deck)
        fullHouseInsteadOf2Pair = ['3C', '3D', '4H', '7H', '7C', 0]
        handScorer.score(myHand)
        winCounter = 0

        for i in range(0, numOfGames):
            random.shuffle(deck)

            player2 = [deck[-1], deck[-2], deck[-3], deck[-4], deck[-5], 0]
            player3 = [deck[-6], deck[-7], deck[-8], deck[-9], deck[-10], 0]
            player4 = [deck[-11], deck[-12], deck[-13], deck[-14], deck[-15], 0]
            player5 = [deck[-16], deck[-17], deck[-18], deck[-19], deck[-20], 0]
            player6 = [deck[-21], deck[-22], deck[-23], deck[-24], deck[-25], 0]

            handMatrix = [myHand, player2, player3, player4, player5, player6]
            for i in range(1, len(handMatrix)):
                handScorer.score(handMatrix[i])

            listOfScores = [handMatrix[0][-1], handMatrix[1][-1], handMatrix[2][-1], handMatrix[3][-1], handMatrix[4][-1], handMatrix[5][-1]]
            listOfScores = sorted(listOfScores)
            
            if myHand[-1] == listOfScores[-1] and listOfScores[-1] > listOfScores[-2]:
                winCounter += 1
            if myHand[-1] == listOfScores[-1] and listOfScores[-1] == listOfScores[-2]:
                winCounter += 0.5
        
        winPercentage = (winCounter/numOfGames * 100)

        fillInDataMatrix(winPercentage, dataMatrix, numOfMyHands, myHand)
        formatAndPrint.printCSV(handMatrix, winPercentage)

    formatAndPrint.printHandTypesAndPercents(dataMatrix)    

driverFunction()