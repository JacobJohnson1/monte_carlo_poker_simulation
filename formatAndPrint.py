import os

def occurrenceCounter(handList, dataMatrix):
    score = handList[-1]
    handType = 0
    if (score > 15) and (score < 30):
        handType = 1
    if (score > 30) and (score < 45):
        handType = 2
    if (score > 45) and (score < 60):
        handType = 3
    if (score > 60) and (score < 75):
        handType = 4
    if (score > 75) and (score < 89):
        dataMatrix[5][0] += 1
        handType = 5
    if (score > 90) and (score < 117):
        handType = 6
    if (score > 118) and (score < 133):
        handType = 7
    if (score > 133) and (score < 147):
        handType = 8
    if (score == 147):
        handType = 9
    dataMatrix[handType][0] += 1
    return handType

def handLabeler(category):
    handLabelStr = ''
    if category == 0:
        handLabelStr = 'High Card'
    elif category == 1:
        handLabelStr = '1 Pair'
    elif category == 2:
        handLabelStr = '2 Pair'
    elif category == 3:
        handLabelStr = '3 of a Kind'
    elif category == 4:
        handLabelStr = 'Straight'
    elif category == 5:
        handLabelStr = 'Flush'
    elif category == 6:
        handLabelStr = 'Full House'
    elif category == 7:
        handLabelStr = '4 of a Kind'
    elif category == 8:
        handLabelStr = 'Straight Flush'
    elif category == 9:
        handLabelStr = 'Royal Flush'
    return handLabelStr

def printHandTypesAndPercents(matrix):
    outputFile = open('output.txt','a')
    for i in range(0, len(matrix)):
        handType = handLabeler(i)
        outputFile.write('The occurrence of a %s is %s%%\n' % (handType, matrix[i][1]))
        outputFile.write('The win percentage of %s is %s%%\n' % (handType, matrix[i][3]))

def printCSV(matrix, winPercent):
    csvFile = open('output.csv', 'a')
    csvFile.write('Card 1, Card 2, Card 3, Card 4, Card 5, Score, Win Percentage\n')
    csvFile.write('%s, %s%%  \n' % (matrix[0], winPercent))