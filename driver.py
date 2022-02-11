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
    numOfGames = 100
    deck = createDeck()
    random.shuffle(deck)
    myHand = dealMyHand(deck)
    print(myHand)

    myScore = handScorer.score(myHand)
    handScorer.labelHands(myHand)
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
        print(listOfScores)
        listOfScores = sorted(listOfScores)
        print(listOfScores)

        if myScore == listOfScores[-1] and listOfScores[-1] > listOfScores[-2]:
            winCounter += 1

        if myScore == listOfScores[-1] and listOfScores[-1] == listOfScores[-2]:
            winCounter += 0.5

        print(winCounter)
    winPercentage = (winCounter/numOfGames * 100)
    print(winPercentage)

driverFunction()