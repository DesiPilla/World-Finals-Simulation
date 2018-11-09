import random
import numpy
import matplotlib.pyplot as plt
from listsOfTeams import *
from OdysseyScoreProgram import *
from OdysseySimulation import *

''' assumes ud is the team running simulation on '''

# this randomly assigns every team in a list a long term score within a certain range
def assignLong(listOfTeams,low, high):
    for team in listOfTeams:
        long = random.randint(low,high)
        team.long = long
        
# this randomly assigns every team in a list a spontaneous score within a certain range
def assignSpon(listOfTeams, low, high):
    for team in listOfTeams:
        spon = random.randint(low,high)
        team.spon = spon

# this randomly assigns every team in a list a style score within a certain range      
def assignStyl(listOfTeams, low, high):
    for team in listOfTeams:
        styl = random.randint(low,high)
        team.styl = styl

# this will call the random assignment functions
def randomAssign(listOfTeams, lowLong, highLong, lowSpon, highSpon, lowStyl, highStyl):
    assignLong(listOfTeams, lowLong, highLong)
    assignSpon(listOfTeams, lowSpon, highSpon)
    assignStyl(listOfTeams, lowStyl, highStyl)         
            
# this will simulate the final scores of a tournament. The first team in the list can get a different scoring range for each category.
def simulateScore(listOfTeams, lowLongOne, highLongOne, lowSponOne, highSponOne, lowStylOne, highStylOne, lowLongOther, highLongOther, lowSponOther, highSponOther, lowStylOther, highStylOther):
    other = listOfTeams[1:]
    randomAssign([ud], lowLongOne, highLongOne, lowSponOne, highSponOne, lowStylOne, highStylOne)
    randomAssign(other, lowLongOther, highLongOther, lowSponOther, highSponOther, lowStylOther, highStylOther)
    changeScores(listOfTeams);
    return sortTeams(listOfTeams)

# this will simulate a World Finals tournament with the same ranges n times.
def simulateWorldsRand(n, listOfTeams, lowLongOne, highLongOne, lowSponOne, highSponOne, lowStylOne, highStylOne, lowLongOther, highLongOther, lowSponOther, highSponOther, lowStylOther, highStylOther):
    udRanks = []
    udTotals = []
    numTies = 0
    for simulation in range(n):
        sortedList = simulateScore(listOfTeams, lowLongOne, highLongOne, lowSponOne, highSponOne, lowStylOne, highStylOne, lowLongOther, highLongOther, lowSponOther, highSponOther, lowStylOther, highStylOther)
        if checkTies(sortedList):
            numTies += 1      
        udRanks += [ud.rank]
        udTotals += [ud.total]
        clearScores(listOfTeams)
    places = numPlaces(udRanks)
    n350s = num350s(udTotals)
    #print('In ' + str("{:,}".format(n)) + ' simulations:')
    #printPlaces(n, numpy.divide(places,float(n)))
    #printTies(n, numTies)
    #print350s(n, n350s)
    return [numpy.divide(places,float(n)), numTies, n350s];
     
def simRandPlot(numSimulations,listOfTeams,lowLong1,highLong1):
    xLong = []
    yFirst = []
    ySecond = []
    yThird = []
    yTop3 = []
    for n in range(lowLong1,highLong1):
        print('Running ' + str(n))
        winPercents = simulateWorldsRand(numSimulations,listOfTeams,n,n,85,100,40,50,100,180,70,100,30,45)
        xLong = xLong + [n];
        yFirst = yFirst + [winPercents[0][0]];
        ySecond = ySecond + [winPercents[0][1]];
        yThird = yThird + [winPercents[0][2]];
        yTop3 = yTop3 + [1-winPercents[0][3]];
    plt.figure(num=None, figsize=(8, 6), dpi=150, facecolor='w', edgecolor='k')
    plt.plot(xLong,yFirst,'#FFD700',xLong,ySecond,'#C0C0C0',xLong,yThird,'#CD5B45',xLong,yTop3,'#228B22')
    plt.xlabel('Long Term Raw Score')
    plt.ylabel('Total Score')
    plt.title('World Final Simulation (Random Simulation)');
    return [xLong, yFirst, ySecond, yThird, yTop3]


'''
5
In 10000 simulations:
UD placed first 32% of the time.
UD placed second 34% of the time.
UD placed third 24% of the time.
UD placed fourth 10% of the time.
''''''
for n in range(110,130):
    print('For a score of ',n)
    simulateWorldsRand(10000,worlds_2018,n,n,85,100,40,50,100,180,70,100,30,45)
    print('\n')
'''