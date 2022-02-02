import random
import handChecker

numbers=list(range(2,15))
suits = ['H','S','C','D']
deck = []
for i in numbers:
    for s in suits:
        card = str(i)+s
        deck.append(card)

random.shuffle(deck)

myCard1 = deck.pop()
myCard2 = deck.pop()
myCard3 = deck.pop()
myCard4 = deck.pop()
myCard5 = deck.pop()

myHand = [myCard1, myCard2, myCard3, myCard4, myCard5, 0]
# remove later; just for testing
print(myHand)

#change range to 500/1000 once everything is working correctly
for x in range(0, 2):
    random.shuffle(deck)
    player2 = [deck[-1], deck[-2], deck[-3], deck[-4], deck[-5], 0]
    player3 = [deck[-6], deck[-7], deck[-8], deck[-9], deck[-10], 0]
    player4 = [deck[-11], deck[-12], deck[-13], deck[-14], deck[-15], 0]
    player5 = [deck[-16], deck[-17], deck[-18], deck[-19], deck[-20], 0]
    player6 = [deck[-21], deck[-22], deck[-23], deck[-24], deck[-25], 0]

handChecker.threeOfAKind(myHand)
print(myHand)
