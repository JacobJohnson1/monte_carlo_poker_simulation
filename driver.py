from concurrent.futures import thread
import random
import handScorer

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

def driverFunction():
    numOfMyHands = 10
    
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

    dataMatrix = [
        [0, highCardPercentages, 0],
        [0, onePairPercentages, 0],
        [0, twoPairPercentages, 0],
        [0, threeOAKPercentages, 0],
        [0, straightPercentages, 0],
        [0, flushPercentages, 0],
        [0, fullHousePercentages, 0],
        [0, fourOAKPercentages, 0],
        [0, straighFlushPercentages, 0],
        [0, royalFlushPercentages, 0]]


    for i in range(0, numOfMyHands):
        numOfGames = 1000
        deck = createDeck()
        random.shuffle(deck)
        myHand = dealMyHand(deck)
        print(myHand)
        myScore = handScorer.score(myHand)
        handCategory = handScorer.labelHands(myHand)
        winCounter = 0
        for i in range(0, numOfGames):
            random.shuffle(deck)
            player2 = [deck[-1], deck[-2], deck[-3], deck[-4], deck[-5], 0]
            player3 = [deck[-6], deck[-7], deck[-8], deck[-9], deck[-10], 0]
            player4 = [deck[-11], deck[-12], deck[-13], deck[-14], deck[-15], 0]
            player5 = [deck[-16], deck[-17], deck[-18], deck[-19], deck[-20], 0]
            player6 = [deck[-21], deck[-22], deck[-23], deck[-24], deck[-25], 0]
            Score2 = handScorer.score(player2)
            Score3 = handScorer.score(player3)
            Score4 = handScorer.score(player4)
            Score5 = handScorer.score(player5)
            Score6 = handScorer.score(player6)
            listOfScores = [myScore, Score2, Score3, Score4, Score5, Score6]
            listOfScores = sorted(listOfScores)
            if myScore == listOfScores[-1] and listOfScores[-1] > listOfScores[-2]:
                winCounter += 1
            if myScore == listOfScores[-1] and listOfScores[-1] == listOfScores[-2]:
                winCounter += 0.5
        winPercentage = (winCounter/numOfGames * 100)
       
        if handCategory == 1:
            dataMatrix[0][0] += 1
            highCardPercentages.append(winPercentage)
        if handCategory == 2:
            dataMatrix[1][0] += 1
            onePairPercentages.append(winPercentage)
        if handCategory == 3:
            dataMatrix[2][0] += 1
            twoPairPercentages.append(winPercentage)
        if handCategory == 4:
            dataMatrix[3][0] += 1
            threeOAKPercentages.append(winPercentage)
        if handCategory == 5:
            dataMatrix[4][0] += 1
            straightPercentages.append(winPercentage)
        if handCategory == 6:
            dataMatrix[5][0] += 1
            flushPercentages.append(winPercentage)
        if handCategory == 7:
            dataMatrix[6][0] += 1
            fullHousePercentages.append(winPercentage)
        if handCategory == 8:
            dataMatrix[7][0] += 1
            fourOAKPercentages.append(winPercentage)
        if handCategory == 9:
            dataMatrix[8][0] += 1
            straighFlushPercentages.append(winPercentage)
        if handCategory == 10:
            dataMatrix[9][0] += 1
            royalFlushPercentages.append(winPercentage)

driverFunction()

# MAKE SURE TO ACTUALLY IMPLEMENT THIS IN DRIVER FUNCTION SOMEWHERE
def addAvgs(dataMatrix):
    for i in dataMatrix:
        dataMatrix[i][2] = averageWin(dataMatrix[i][1])

def averageWin(winPercentages):
    total = 0
    for i in winPercentages:
        total += winPercentages[i]
    if len(winPercentages) > 0:
        avg = (total/len(winPercentages))
    return avg

# fakeHand = ['11C', '8S', '7D', '10S', '10D', 0]
# handScorer.fullHouse(fakeHand)
# print(fakeHand)