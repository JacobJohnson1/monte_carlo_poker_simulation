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

# fakeHand = ['14H', '2H', '3H', '4H', '5H', 0]
# print(fakeHand)
# handChecker.flush(fakeHand)
# print(fakeHand)

def driverFunction():
    deck = createDeck()
    random.shuffle(deck)
    myHand = dealMyHand(deck)

    # while a boolean is not false, keep asking to do new hand

    # change to 1000 soon
    for i in range(0, 1):
        player2 = dealOponentHand(deck)
        player3 = dealOponentHand(deck)
        player4 = dealOponentHand(deck)
        player5 = dealOponentHand(deck)
        player6 = dealOponentHand(deck)

        handChecker.score(myHand)
    
    


driverFunction()