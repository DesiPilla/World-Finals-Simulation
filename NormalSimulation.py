import random
import numpy
import matplotlib.pyplot as plt
from listsOfTeams import *
from OdysseyScoreProgram import *
from OdysseySimulation import *

# this assigns every team in a list a long term score with using a normal distribution
def assignLong(listOfTeams, mean, std):
    if not listOfTeams:
        return
    else:
        long = random.gauss(mean, std)
        if (long >= 0 and long<= 200):
            listOfTeams[0].long = long
            assignLong(listOfTeams[1:], mean, std)
        else:
            assignLong(listOfTeams, mean, std)
        
# this assigns every team in a list a spontaneous score with using a normal distribution
def assignSpon(listOfTeams, mean, std):
    if not listOfTeams:
        return
    else:
        spon = random.gauss(mean, std)
        if (spon >= 0 and spon<= 100):
            listOfTeams[0].spon = spon
            assignSpon(listOfTeams[1:], mean, std)
        else:
            assignSpon(listOfTeams, mean, std)

# this assigns every team in a list a style score with using a normal distribution     
def assignStyl(listOfTeams, mean, std):
    if not listOfTeams:
        return
    else:
        styl = random.gauss(mean, std)
        if (styl >= 0 and styl<= 50):
            listOfTeams[0].styl = styl
            assignStyl(listOfTeams[1:], mean, std)
        else:
            assignStyl(listOfTeams, mean, std)

# this will call the random assignment functions
def normalAssign(listOfTeams, meanLong, stdLong, meanSpon, stdSpon, meanStyl, stdStyl):
    assignLong(listOfTeams, meanLong, stdLong)
    assignSpon(listOfTeams, meanSpon, stdSpon)
    assignStyl(listOfTeams, meanStyl, stdStyl)         
            
# this will simulate the final scores of a tournament. The first team in the list can get a different scoring range for each category.
def simulateScore(listOfTeams, meanLongOne, stdLongOne, meanSponOne, stdSponOne, meanStylOne, stdStylOne, meanLongOther, stdLongOther, meanSponOther, stdSponOther, meanStylOther, stdStylOther):
    other = listOfTeams[1:]
    normalAssign([ud], meanLongOne, stdLongOne, meanSponOne, stdSponOne, meanStylOne, stdStylOne)
    normalAssign(other, meanLongOther, stdLongOther, meanSponOther, stdSponOther, meanStylOther, stdStylOther)
    changeScores(listOfTeams);
    return sortTeams(listOfTeams)

# this will simulate a World Finals tournament with the same ranges n times.
def simulateWorldsNorm(n, listOfTeams, meanLongOne, stdLongOne, meanSponOne, stdSponOne, meanStylOne, stdStylOne, meanLongOther, stdLongOther, meanSponOther, stdSponOther, meanStylOther, stdStylOther):
    udRanks = []
    udTotals = []
    numTies = 0
    for simulation in range(n):
        sortedList = simulateScore(listOfTeams, meanLongOne, stdLongOne, meanSponOne, stdSponOne, meanStylOne, stdStylOne, meanLongOther, stdLongOther, meanSponOther, stdSponOther, meanStylOther, stdStylOther)
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
    #print(str(round(n350s/n,2)))
    return [numpy.divide(places,float(n)), numTies, n350s];
    

def simNormPlot(numSimulations,listOfTeams,lowLong1,highLong1,stdevLong1):
    xLong = []
    yFirst = []
    ySecond = []
    yThird = []
    yTop3 = []
    for n in range(lowLong1,highLong1):
        print('Running ' + str(n))
        winPercents = simulateWorldsNorm(numSimulations,listOfTeams,n,stdevLong1,94,3,44,2,130,20,85,6,40,4) 
        xLong = xLong + [n];
        yFirst = yFirst + [winPercents[0][0]];
        ySecond = ySecond + [winPercents[0][1]];
        yThird = yThird + [winPercents[0][2]];
        yTop3 = yTop3 + [1-winPercents[0][3]];
    plt.figure(num=None, figsize=(8, 6), dpi=150, facecolor='w', edgecolor='k')
    plt.plot(xLong,yFirst,xLong,ySecond,'#C0C0C0',xLong,yThird,'#CD5B45',xLong,yTop3,'#228B22')
    plt.xlabel('Long Term Raw Score')
    plt.ylabel('Total Score')
    plt.title('World Final Simulation (Normal Distribution)');
    return [xLong, yFirst, ySecond, yThird, yTop3]


#simNormPlot(7500,worlds_2018,110,160,15)
    
'''
simulateWorlds(10000,worlds_2018,132,15,94,3,44,2,130,20,85,6,40,4) 
In 10,000 simulations:
UD placed first 43% of the time.
UD placed second 32% of the time.
UD placed third 18% of the time.
UD placed fourth 7% of the time.
There was a tie 12% of the time.
UD scored a 350 11% of the time.

''''''

str(round(places[i]*/n,2))          # i = 0, 1, 2 
str(round(1-(places[3]/n),2))
str(round(n350s/n,2))

''''''

for long in range(110,170):
    #print('For a score of ',long)
    simulateWorldsNorm(10000,worlds_2018,long,0,94,3,44,2,130,20,90,10,40,4)
    #print('\n')

'''