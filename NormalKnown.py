import random
from OdysseyScoreProgram import worlds_2018     # List of Teams you're running simulation on
from OdysseyScoreProgram import changeScores
from OdysseyScoreProgram import sortTeams
from OdysseySimulation import checkTies
from OdysseySimulation import clearScores
from OdysseySimulation import numPlaces
from OdysseySimulation import num350s
from OdysseySimulation import printExcel
from OdysseySimulation import printPlaces
from OdysseySimulation import printTies
from OdysseySimulation import print350s
#from NormalSimulation import assignLong
#from NormalSimutation import assignSpon
#from NormalSimulation import assignStyl
from NormalSimulation import normalAssign
from NormalSimulation import sortTeams

def simulateScore(listOfTeams, knownLong, knownStyl, sponUD, guessLong1, guessStyl1, guessLong2, guessStyl2, guessLong3, guessStyl3, stdevLong, stdevStyl, guessSpon, stdevSpon):
    normalAssign([listOfTeams[0]], knownLong, 0, sponUD, stdevSpon, knownStyl, 0)
    normalAssign([listOfTeams[1]], guessLong1, stdevLong, guessSpon, stdevSpon, guessStyl1, stdevStyl)
    normalAssign([listOfTeams[2]], guessLong2, stdevLong, guessSpon, stdevSpon, guessStyl2, stdevStyl)
    normalAssign([listOfTeams[3]], guessLong3, stdevLong, guessSpon, stdevSpon, guessStyl3, stdevStyl)
    changeScores(listOfTeams)
    return sortTeams(listOfTeams)

def simulateWorlds(n, listOfTeams, knownLong, knownStyl, sponUD, guessLong1, guessStyl1, guessLong2, guessStyl2, guessLong3, guessStyl3, stdevLong, stdevStyl, guessSpon, stdevSpon):
    udRanks = []
    udTotals = []
    numTies = 0
    avgLoss = 0
    for simulation in range(n):
        sortedList = simulateScore(listOfTeams, knownLong, knownStyl, sponUD, guessLong1, guessStyl1, guessLong2, guessStyl2, guessLong3, guessStyl3, stdevLong, stdevStyl, guessSpon, stdevSpon)
        if checkTies(sortedList):
            numTies += 1      
        udRanks += [listOfTeams[0].rank]
        udTotals += [listOfTeams[0].total]
        avgLoss += listOfTeams[0].total-sortedList[0].total
        clearScores(listOfTeams)
    places = numPlaces(udRanks)
    n350s = num350s(udTotals)
    print('In ' + str("{:,}".format(n)) + ' simulations:')
    printPlaces(n, places)              # simulation standard output
    printTies(n, numTies)               # simulation standard output
    print350s(n, n350s)                 # simulation standard output
    #print(str(round(avgLoss/n,2)))      # for printing specific stats

simulateWorlds(10000, worlds_2018, 123.08, 30.34, 94, 135, 33, 118, 38, 77, 41, 10, 5, 90, 5) 