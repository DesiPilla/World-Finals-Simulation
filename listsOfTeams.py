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