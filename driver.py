import random
import handChecker

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

def dealOponentHand(deck):
    random.shuffle(deck)
    playerHand = [deck.pop(), deck.pop(), deck.pop(), deck.pop(), deck.pop(), 0]
    return playerHand

# fakeHand = ['14H', '14S', '14D', '14C', '13H', 0]
# fakeHand = ['12H', '13H', '11H', '10H', '9H', 0]
# print(fakeHand)
# handChecker.flush(fakeHand)
# print(fakeHand)

def driverFunction():
    deck = createDeck()
    random.shuffle(deck)
    myHand = dealMyHand(deck)
    print(myHand)
    # while a boolean is not false, keep asking to do new hand

    # change to 1000 soon
    for i in range(0, 1):
        winCounter = 0
        player2 = dealOponentHand(deck)
        player3 = dealOponentHand(deck)
        player4 = dealOponentHand(deck)
        player5 = dealOponentHand(deck)
        player6 = dealOponentHand(deck)

        myScore = handChecker.score(myHand)
        Score2 = handChecker.score(player2)
        Score3 = handChecker.score(player3)
        Score4 = handChecker.score(player4)
        Score5 = handChecker.score(player5)
        Score6 = handChecker.score(player6)

        listOfScores = [myScore, Score2, Score3, Score4, Score5, Score6]
        print(listOfScores)
        listOfScores = sorted(listOfScores)
        print(listOfScores)

        if myScore == listOfScores[-1] and listOfScores[-1] > listOfScores[-2]:
            winCounter += 1

        if myScore == listOfScores[-1] and listOfScores[-1] == listOfScores[-2]:
            winCounter += 0.5

        print(winCounter)

        # handChecker.printingTextFile(myHand)

driverFunction()