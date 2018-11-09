import matplotlib.pyplot as plt

# this resets every teams scores in a list of teams
def clearScores(listOfTeams):
    for team in listOfTeams:
        team.long = 0
        team.spon = 0
        team.styl = 0
        team.total = 0
        team.rank = 0
        
# this checks for ties and changes the ranks accordingly
def checkTies(sortedList):  
    for i in range(len(sortedList)-1):
        if abs(sortedList[i].total - sortedList[i+1].total) < 1:
            for team in sortedList[i+1:]:
                team.rank -= 1
            return 1          
        
# this counts the number of first, second, third, and fourth place finishes for UD in a simulation.          
def numPlaces(udRanks):
    numFirst = 0;
    numSecond = 0;
    numThird = 0;
    numFourth = 0;
    for i in udRanks:
        if i == 1:
            numFirst += 1
        elif i == 2:
            numSecond += 1
        elif i == 3:
            numThird += 1
        elif i == 4:
            numFourth += 1
    return [numFirst, numSecond, numThird, numFourth]

# this counts the number of 350 scores UD receives in a simulation.
def num350s(udTotals):
    num350s = 0;
    for i in udTotals:
        if i == 350:
            num350s += 1;
    return num350s

# this prints the number of first, second, and third place finishes for UD in a simulation.
def printPlaces(n, places):
    print('UD placed first ' + str(round(places[0]*100,1)) + '% of the time.' + '\n' + 'UD placed second ' + str(round(places[1]*100,1)) + '% of the time.' + '\n' + 'UD placed third ' + str(round(places[2]*100,1)) + '% of the time.' + '\n' + 'UD placed Top 3 ' + str(100 - round(places[3]*100,1)) + '% of the time.')


# this prints the number of ties there were in a simulation.
def printTies(n, numTies):
    print('There was a tie ' + str(round(numTies/n*100)) + '% of the time.')
    
    
# this prints the number of 350 score finishes for UD in a simulation.
def print350s(n, n350s):
    print('UD scored a 350 ' + str(round(n350s/n*100)) + '% of the time.')
    
# this prints a list of stats as a column so it can be pasted into excel
def printExcel(listOfStats):
    for item in listOfStats:
        print(item)

    
