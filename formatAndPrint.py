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

def labelHands(handList):
    score = handList[-1]
    category = 0
    if (score < 15):
        print('High Card with a score of: %s' % score)
        category = 1
    if (score > 15) and (score < 30):
        print('1 Pair with a score of: %s' % score)
        category = 2
    if (score > 30) and (score < 45):
        print('2 Pair with a score of: %s' % score)
        category = 3
    if (score > 45) and (score < 60):
        print('3 of a Kind with a score of: %s' % score)
        category = 4
    if (score > 60) and (score < 75):
        print('Straight with a score of: %s' % score)
        category = 5
    if (score > 75) and (score < 89):
        print('Flush with a score of: %s' % score)
        category = 6
    if (score > 90) and (score < 117):
        print('Full House with a score of: %s' % score)
        category = 7
    if (score > 118) and (score < 133):
        print('4 of a Kind with a score of: %s' % score)
        category = 8
    if (score > 133) and (score < 147):
        print('Straight Flush with a score of: %s' % score)
        category = 9
    if (score == 147):
        print('Royal Flush with a score of: %s' % score)
        category = 10
    return category

def printHandTypesAndPercents(matrix):
    outputFile = open('output.txt','w')
    for i in range(0, 9):
        outputFile.write('The occurrence of a %s is %s' % (matrix[i][0], matrix[i][1]))
        outputFile.write('The win percentage of %s is %s' % (matrix[i][0], matrix[i][3]))
    # A summary showing the percentage of hands falling 
    # into each rank, and the overall win percentage for 
    # each rank, as a ‘normal’ text file. Don’t just 
    # list the percentages; add enough text to make 
    # it reader-friendly. 

def printCSV():
    csvFile = open('output.csv', 'w')
    # A session log output as a CSV file, with each 
    # hand on a separate line. For each hand: the cards 
    # in the hand; what the hand was evaluated as; and 
    # its winning percentage. 


