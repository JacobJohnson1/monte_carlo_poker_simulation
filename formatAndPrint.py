# def categorizeHands(handList):
#     score = handList[-1]
#     if (score < 15):
#         print('High Card with a score of: %s' % score)
#     if (score > 15) and (score < 30):
#         print('1 Pair with a score of: %s' % score)
#     if (score > 30) and (score < 45):
#         print('2 Pair with a score of: %s' % score)
#     if (score > 45) and (score < 60):
#         print('3 of a Kind with a score of: %s' % score)
#     if (score > 60) and (score < 75):
#         print('Straight with a score of: %s' % score)
#     if (score > 75) and (score < 89):
#         print('Flush with a score of: %s' % score)
#     if (score > 90) and (score < 117):
#         print('Full House with a score of: %s' % score)
#     if (score > 118) and (score < 133):
#         print('4 of a Kind with a score of: %s' % score)
#     if (score > 133) and (score < 147):
#         print('Straight Flush with a score of: %s' % score)
#     if (score == 147):
#         print('Royal Flush with a score of: %s' % score)

import os


def occurrenceCounter(handList, dataMatrix):
    score = handList[-1]
    if (score > 15) and (score < 30):
        # print('1 Pair with a score of: %s' % score)
        dataMatrix[1][0] += 1
    if (score > 30) and (score < 45):
        # print('2 Pair with a score of: %s' % score)
        dataMatrix[2][0] += 1
    if (score > 45) and (score < 60):
        print('3 of a Kind with a score of: %s' % score)
        dataMatrix[3][0] += 1
    if (score > 60) and (score < 75):
        # print('Straight with a score of: %s' % score)
        dataMatrix[4][0] += 1
    if (score > 75) and (score < 89):
        # print('Flush with a score of: %s' % score)
        dataMatrix[5][0] += 1
    if (score > 90) and (score < 117):
        # print('Full House with a score of: %s' % score)
        dataMatrix[6][0] += 1
    if (score > 118) and (score < 133):
        # print('4 of a Kind with a score of: %s' % score)
        dataMatrix[7][0] += 1
    if (score > 133) and (score < 147):
        # print('Straight Flush with a score of: %s' % score)
        dataMatrix[8][0] += 1
    if (score == 147):
        # print('Royal Flush with a score of: %s' % score)
        dataMatrix[9][0] += 1
    else:
        dataMatrix[0][0] += 1

def printHandTypesAndPercents(matrix):
    outputFile = open('output.txt','w')
    for i in range(0, len(matrix)):
        outputFile.write('The occurrence of a %s is %s\n' % (matrix[i][0], matrix[i][1]))
        outputFile.write('The win percentage of %s is %s\n' % (matrix[i][0], matrix[i][3]))
    # A summary showing the percentage of hands falling 
    # into each rank, and the overall win percentage for 
    # each rank, as a ‘normal’ text file. Don’t just 
    # list the percentages; add enough text to make 
    # it reader-friendly. 

def printCSV(matrix, winPercent):
    csvFile = open('output.csv', 'w')
    csvFile.write('Card 1, Card 2, Card 3, Card 4, Card 5, Score, Win Percentage\n')
    csvFile.write('%s, %s  \n' % (matrix[0], winPercent))
        # A session log output as a CSV file, with each 
        # hand on a separate line. For each hand: the cards 
        # in the hand; what the hand was evaluated as; and 
        # its winning percentage. 


