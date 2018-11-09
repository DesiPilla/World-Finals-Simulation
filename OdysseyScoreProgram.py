#long term, spontaneous, and style
import random
import numpy as np
from listsOfTeams import base

'''
class Odyssey():
    
    def __init__(self,name,long,spon,styl,penal,total,rank):
        self.name = name
        self.long = long
        self.spon = spon
        self.styl = styl 
        self.penal = penal
        self.total = total
        self.rank = rank

base=Odyssey("zero",0,0,0,0,0,0)
'''

#this changes team's raw long term scores to their final long term scores    
def changeLong(listOfTeams):
    highLong=0
    for team in listOfTeams:
        if team.long>highLong:
            highLong=team.long
    for team in listOfTeams:
        if team.long==highLong:
            team.long=200
        else:
            team.long=team.long/float(highLong)*200
        team.total+=team.long
            
#this changes team's raw spontaneous scores to their final spontaneous scores    
def changeSpon(listOfTeams):
    highSpon=0
    for team in listOfTeams:
        if team.spon>highSpon:
            highSpon=team.spon       
    for team in listOfTeams:
        if team.spon==highSpon:
            team.spon=100
        else:
            team.spon=team.spon/float(highSpon)*100
        team.total+=team.spon
            
#this changes team's raw style scores to their final style scores    
def changeStyl(listOfTeams):
    highStyl=0
    for team in listOfTeams:
        if team.styl>highStyl:
            highStyl=team.styl
    for team in listOfTeams:
        if team.styl==highStyl:
            team.styl=50     
        else:
            team.styl=team.styl/float(highStyl)*50
        team.total+=team.styl

#this adds all the parts to give the total final scores
def changeScores(listOfTeams):
    changeStyl(listOfTeams)
    changeLong(listOfTeams)
    changeSpon(listOfTeams)
    for team in listOfTeams:
        team.total-=team.penal
        
#this sorts the teams from highest to lowest by their final total scores
def sortTeams(listOfTeams):
    sortedTeams=[base]
    for team in listOfTeams:
        for spot in range(len(sortedTeams)):
            if team.total>sortedTeams[spot].total and team not in sortedTeams:
                sortedTeams=sortedTeams[:spot]+[team]+sortedTeams[spot:]
    del sortedTeams[len(sortedTeams)-1]
    for place in range(len(listOfTeams)):
        sortedTeams[place].rank = (place + 1)  
    return sortedTeams

#this sorts the teams from highest to lowest by their final long term scores
def sortLong(listOfTeams):
    sortedLong=[base]
    for team in listOfTeams:
        for spot in range(len(sortedLong)):
            if team.long>sortedLong[spot].long and team not in sortedLong:
                sortedLong=sortedLong[:spot]+[team]+sortedLong[spot:]
    del sortedLong[len(sortedLong)-1]
    return sortedLong

#this sorts the teams from highest to lowest by their final spontaneous scores
def sortSpon(listOfTeams):
    sortedSpon=[base]
    for team in listOfTeams:
        for spot in range(len(sortedSpon)):
            if team.spon>sortedSpon[spot].spon and team not in sortedSpon:
                sortedSpon=sortedSpon[:spot]+[team]+sortedSpon[spot:]
    del sortedSpon[len(sortedSpon)-1]
    return sortedSpon   

#this sorts the teams from highest to lowest by their final style scores
def sortStyl(listOfTeams):
    sortedStyl=[base]
    for team in listOfTeams:
        for spot in range(len(sortedStyl)):
            if team.styl>sortedStyl[spot].styl and team not in sortedStyl:
                sortedStyl=sortedStyl[:spot]+[team]+sortedStyl[spot:]
    del sortedStyl[len(sortedStyl)-1]
    return sortedStyl

# this checks for ties and changes the ranks accordingly
def checkTies(sortedList):  
    for i in range(len(sortedList)-1):
        if abs(sortedList[i].total - sortedList[i+1].total) < 1:
            for team in sortedList[i+1:]:
                team.rank -= 1
    
#this prints the rankings by total score nicely
def printNice(sortedList):
    print( "Rank" + '\t' + "Team        " + '\t' + "Total " + '\t' + "|   " +\
          "LT   " + '\t' + "Style" + '\t' + "Spontaneous")
    rank=0
    for team in sortedList:
        rank+=1
        print( str(rank) + '\t' + team.name + '\t' + str(round(team.total,2)) +\
              '\t' + "|   " + str(round(team.long,2)) + '\t' + \
              str(round(team.styl,2)) + '\t' + str(round(team.spon,2)))

#this prints the rankings by final long term nicely
def printLongNice(sortedLong):
    print( '\n' + "Rank" + '\t' + "Team     " + '\t' + "Long Term")
    rank=0
    for team in sortedLong:
        rank+=1
        print( str(rank) + '\t' + team.name + '\t' + str(round(team.long,2)))

#this prints the rankings by final spontaneous nicely
def printSponNice(sortedSpon):
    print( '\n' + "Rank" + '\t' + "Team     " + '\t' + "Spontaneous")
    rank=0
    for team in sortedSpon:
        rank+=1
        print( str(rank) + '\t' + team.name + '\t' + str(round(team.spon,2)))
        
#this prints the rankings by final style nicely
def printStylNice(sortedStyl):
    print( '\n' + "Rank" + '\t' + "Team     " + '\t' + "Style")
    rank=0
    for team in sortedStyl:
        rank+=1
        print( str(rank) + '\t' + team.name + '\t' + str(round(team.styl,2)))   

#this ranks the teams by total score, long term, spontaneous, and style
def rankTeams(listOfTeams):
    changeScores(listOfTeams)
    sortedList = sortTeams(listOfTeams)
    sortedLong = sortLong(sortedList)
    sortedSpon = sortSpon(sortedList)
    sortedStyl = sortStyl(sortedList)
    checkTies(sortedList)
    #printNice(sortedList)
    #printLongNice(sortedLong)
    #printSponNice(sortedSpon)
    #printStylNice(sortedStyl)
    return [sortedList, sortedLong, sortedSpon, sortedStyl]


'''
#2017 Division III Problem 5 Regionals
caravel = Odyssey("Caravel   ",167.01,10.5,39.66,0,0,0)
charterA = Odyssey("Charter A",159.68,41.00,43.67,2,0,0)
charterB = Odyssey("Charter B",163.66,97.5,43.33,3,0,0)
charterC = Odyssey("Charter C",155.34,25.25,33.66,15,0,0)
conrad = Odyssey("Conrad   ",165.33,69.00,44.66,3,0,0)
mot = Odyssey("MOT Charter",154.01,42,36.67,0,0,0)
chior = Odyssey("Chior Sch",149.99,42.25,40.01,0,0,0)
mckean = Odyssey("McKean  ",160.99,38.5,38,0,0,0)
river_region_2017 = [caravel,charterA,charterB,charterC,conrad,mot,chior,mckean]

#2015 Division II Problem 5 States?
cab = Odyssey("Cab Calloway",165,123,39.66,2,0,0)
conrad = Odyssey("Conrad   ",177.5,126.5,43.67,0,0,0)
hb = Odyssey("HB Dupont",146.75,127.25,36,10,0,0)
ps = Odyssey("PS Dupont",177,122.75,40.33,0,0,0)
skylineA = Odyssey("Skyline A",128.75,120,35,0,0,0)
skylineB = Odyssey("Skyline B",181.25,121.75,37.33,0,0,0)
springer = Odyssey("Springer",165.5,125.5,39.33,0,0,0)
states_2015 = [cab,conrad,hb,ps,skylineA,skylineB,springer]

#2018 Division III Problem 5 Ocean Regionals 
cape = Odyssey('Cape Henlopen',164.68,120,39.75,0,0,0)
smyrna = Odyssey('Smyrna       ', 165.34,101.5,44,0,0,0)
lakee = Odyssey('Lake Forest E',167.33,92.25,41.25,0,0,0)
lakef = Odyssey('Lake Forest F',167.67,94.75,38,0,0,0)
cr = Odyssey('Caesar Rodney',168.33,78.75,38.25,0,0,0)
poly = Odyssey('Polytech      ',135,86.25,24.75,0,0,0)
ocean_region_2018 = [cape,smyrna, lakee, lakef, cr, poly]

#2018 Division III Problem 5 River Regionals
conrad = Odyssey('Conrad   ',174,86.20,39.25,15,0,0)
mot = Odyssey('MOT Charter',167.33,82.60,32.50,0,0,0)
river_region_2018 = [conrad, mot]

"""
changeSpon(ocean_region_2018)
changeSpon(river_region_2018)
regional_winners_2018 = [cape,smyrna, lakee, lakef, conrad, mot]
for team in regional_winners_2018:
    team.total -= team.spon
"""

#2018 Division III Problem 5 State Finals
cape = Odyssey('Cape Henlopen',157.01,105.33,46.5,0,0,0)
smyrna = Odyssey('Smyrna       ',159.32,134.33,43,0,0,0)
lakee = Odyssey('Lake Forest E',154.99,98,38,0,0,0)
lakef = Odyssey('Lake Forest F',156.01,141.33,33,0,0,0)
conrad = Odyssey('Conrad   ',174.34,130.67,41,0,0,0)
mot = Odyssey('MOT Charter   ',161.35,121,45.5,0,0,0)
states_2018 = [cape,smyrna, lakee, lakef, conrad, mot]

#2018 Division II Problem 2 Regional Winners
conrad = Odyssey('Conrad   ',144,100,40,0,0,0)
hb = Odyssey('HB Dupont',117,78.95,43.32,0,0,0)
newark = Odyssey('Newark Charter',103,77.63,34.33,1,0,0)
lake = Odyssey('Lake Forest',144.5,100,39.25,0,0,0)
post = Odyssey('Postlehwait',110.75,87.71,34.75,0,0,0)
jb = Odyssey('J B Moore',78.75,54.30,30,0,0,0)
emoji_regional_winners = [conrad, hb, newark, lake, post, jb]

#2018 Division IV Problem 1 World Finals
ud = Odyssey('Univ of Del',123.64,100,30.34,0,0,0)
nanjing = Odyssey('Nanjing   ',125.68,81.94,33.99,4,0,0)
engsci = Odyssey('Eng & Sci    ',95.34,83.51,36,0,0,0)
jiao = Odyssey('Jiao Tong      ',78,90.58,34.67,4,0,0)
worlds_2018 = [ ud, nanjing, engsci, jiao]


#2018 Division III Problem 5 World Finals
nc = Odyssey('North Carolina',178,95.06,46.34,0,0,0)
sing = Odyssey('Singapore',173.75,100,44,0,0,0)
pol = Odyssey('Poland  ',166.75,95.31,46,1,0,0)
sing1 = Odyssey('Singapore',170.5,91.36,43,0,0,0)
ny = Odyssey('New York',168.25,92.59,42.67,0,0,0)
ga = Odyssey('Georigia',168.75,88.89,42.67,0,0,0)
pa = Odyssey('Pennsylvania',164,93.83,39.67,0,0,0)
tx = Odyssey('Texas      ',170,81.98,43.33,0,0,0)
va = Odyssey('Virginia',153.75,95.31,43.67,0,0,0)
pol1 = Odyssey('Poland   ',160.25,90.61,44.33,5,0,0)
az = Odyssey('Arizona       ',164,84.69,40,0,0,0)
ny1 = Odyssey('New York',165.75,89.87,35.66,5,0,0)
nj = Odyssey('New Jersey',160.5,95.31,31.34,0,0,0)
mi = Odyssey('Michigan',154.25,90.61,38.67,0,0,0)
fl = Odyssey('Florida     ',154.5,90.37,38,0,0,0)
nc1 = Odyssey('North Carolina',156.75,82.96,40,0,0,0)
sing2 = Odyssey('Singapore',155.25,86.91,37.68,0,0,0)
canada = Odyssey('Canada   ',156.25,91.61,30,0,0,0)
nj1 = Odyssey('New Jersey',148.75,91.36,36.67,0,0,0)
ca = Odyssey('California',161.25,79.01,35,0,0,0)
me = Odyssey('Maine     ',149.5,86.42,37.67,0,0,0)
va1 = Odyssey('Virginia',150.5,89.13,33,0,0,0)
ok = Odyssey('Oklahoma',153,85.43,32.67,0,0,0)
fl1 = Odyssey('Florida    ',150.25,80.5,40.33,1,0,0)
hk = Odyssey('Hong Kong',150,78.27,41,0,0,0)
fl2 = Odyssey('Florida    ',150.5,82.22,35.66,0,0,0)
pa1 = Odyssey('Pennsylvania',144.25,85.93,38.33,0,0,0)
ca1 = Odyssey('California',144,95.06,29.66,0,0,0)
de = Odyssey('---CONRAD---',150.75,85.19,31.67,0,0,0)
ch = Odyssey('China     ',149.25,83.95,34.33,0,0,0)
ky = Odyssey('Kentucky',143.5,95.80,28.99,0,0,0)
ga1 = Odyssey('Georgia  ',144.75,91.85,31,0,0,0)
mo = Odyssey('Missouri',149.25,85.68,32.01,0,0,0)
ar = Odyssey('Arkansas',145.75,86.42,33,0,0,0)
ch1 = Odyssey('China    ',153.25,81.98,27.67,0,0,0)
mi1 = Odyssey('Michigan',149.25,75.80,33,0,0,0)
mi2 = Odyssey('Michigan',144.75,76.05,35.68,0,0,0)
az1 = Odyssey('Arizona    ',140.5,76.54,38.01,0,0,0)
ar1 = Odyssey('Arkansas',139.25,77.78,34.68,0,0,0)
ch2 = Odyssey('China    ',146.25,79.01,30.67,5,0,0)
me1 = Odyssey('Maine     ',140.25,87.16,24.68,0,0,0)
wi = Odyssey('Wisconsin',140.75,74.81,35.01,0,0,0)
tx1 = Odyssey('Texas    ',139.75,74.57,35.01,0,0,0)
ia = Odyssey('Iowa     ',141.25,80.24,31.33,5,0,0)
sd = Odyssey('South Dakota',142,83.70,23.01,0,0,0)
ok1 = Odyssey('Oklahoma',141,77.28,28,0,0,0)
ky1 = Odyssey('Kentucky',140.75,84.94,20.66,0,0,0)
de1 = Odyssey('Delaware',146.75,67.41,29,0,0,0)
ar2 = Odyssey('Arkansas',132,83.46,28.33,0,0,0)
il = Odyssey('Illinois',140.5,72.35,30.66,1,0,0)
ks = Odyssey('Kansas  ',118.75,74.81,24.66,0,0,0)
kr = Odyssey('Korea   ',125.75,68.89,19.99,0,0,0)
hk1 = Odyssey('Hong Kong',137.50,78.52,20.66,30,0,0)
kr1 = Odyssey('Korea   ',137.50,33.83,26.34,5,0,0)
worlds_p5 = [nc, sing, pol, sing1, ny, ga, pa, tx, va, pol1, az, ny1, nj, mi, fl, nc1, sing2, canada, nj1, ca, me, va1, ok, fl1, hk, fl2, pa1, ca1, de, ch, ky, ga1, mo, ar, ch1, mi1, mi2, az1, ar1, ch2, me1, wi, tx1, ia, sd, ok1, ky1, de1, ar2, il, ks, kr, hk1, kr1]
'''
