# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 21:28:54 2021

@author: LUKAS
"""

from Classes import person,vehicle,lifeform,organisation,cities,location,transactions
tl=[]
tl.append('alpha')
tl.append('beta')
tl.append('gamma')
tl.append('delta')
tl.append('epsilon')
tl.append('zeta')
tl.append('eta')
tl.append('theta')
tl.append('iota')
tl.append('kappa')

v=[]

c=[]
c.append(cities('Stray City',5000000))

l=[]
l.append(location('Anwesen','Stray City'))
l.append(location('Hive','Stray City'))
l.append(location('The golden Black','Stray City'))
l.append(location('Stray City Gefängnis','Stray City'))

lf=[]
lf0=lifeform('Human',0)
lf.append(lf0)

lf1=lifeform('Rakashan',2)
lf1.strength.append('Verstärkte Klauen (tl+1)')
lf1.notes.append('Raubkatzenähnlicher Humanoider')
lf.append(lf1)

lf2=lifeform('Rakasaurie',2)
lf2.strength.append('Verstärkte Haut (tl+1)')
lf2.strength.append('Verstärkte Klauen (tl+1)')
lf2.notes.append('größere Humanoide mit Echsenhaut')
lf.append(lf2)

lf3=lifeform('Genosianer',0)
lf3.weaknesses.append('klein')
lf3.strength.append('sechs Arme')
lf3.notes.append('Insektoide Lebensform fast humanoide Größe')
lf.append(lf3)

lf4=lifeform('Koalarama',0)
lf4.weaknesses.append('sehr klein')
lf4.notes.append('Fünfäugiger Koala')
lf.append(lf4)
          

lf5=lifeform('Twilek',0)
lf5.notes.append('humanoider mit farbiger Haut und zwei "Tentakeln"')
lf.append(lf5)
          
lf6=lifeform('Hydra',3)
lf6.weaknesses.append('Feuer')
lf6.strength.append('Regeneration')
lf.append(lf6)

lf7=lifeform('Aurax',0)
lf7.notes.append('dunkle Haut')
lf7.notes.append('farbige Augen')
lf.append(lf7)

lf8=lifeform('Quillianer',0)
lf8.notes.append('Humanoider Insektoid')
lf.append(lf8)

lf9=lifeform('Gundabard',0)
lf9.notes.append('orkischer Humanoider')
lf9.notes.append('albino Haut')
lf.append(lf9)


lf10=lifeform('Quilehan',1)
lf10.notes.append('Humanoid mit 2 Hörnern auf dem Kopf')
lf10.notes.append('farbige Haut')
lf10.strength.append('Telepatische + Telekenetische Kräfte (tl+1)')
lf10.weaknesses.append('Fast ausgestorbene Rasse')
lf.append(lf10)

lf11=lifeform('Aquari',0)
lf11.notes.append('Hörner')
lf.append(lf11)


org=[]
org.append(organisation('Polizei'))
org.append(organisation('CyberPunX'))
org.append(organisation('Creaters In Black'))
org.append(organisation('Interplanetarische Diplomatencore'))

    
p=[]
p.append(person('Lord','Trevor','Belmont',lf[0],1.89,'Erbauer',lf[0].mintl))
p.append(person("",'Briff',"",lf[0],1.6,'none',lf[0].mintl))    
p.append(person('','Wurmerdinger','',lf[0],1.7,'none',lf[0].mintl))
p.append(person('Mr','Rakor','',lf[1],1.95,'subjekt',lf[1].mintl))
p.append(person('','Trexx','',lf[2],1.8,'beschützenswert',lf[2].mintl))
p.append(person('Mr','Smokey',"",lf[0],0.597,'none',lf[0].mintl))
p.append(person("Squirm",'Gonoga','Nacohh',lf[7],1.70,'beschützenswert',lf[7].mintl))
p.append(person('Der Verschlinger','Agent','Smith',lf[8],1.6,'none',lf[8].mintl))
p.append(person('Governeur','','Mcaffy',lf[0],999,'none',lf[0].mintl))
p.append(person('','','Timmothy',lf[9],1.8,'none',lf[9].mintl))
p.append(person('','ShaVi','',lf[10],1.75,'none',lf[10].mintl))
p.append(person('Kommando 7','','',lf[0],1.8,'none',lf[0].mintl+2))
p[8].notes.append('Agent der CIB')
p.append(person('','Jared','Conners',lf[0],999,'none',lf[0].mintl+1))
t=[]

#wunsch nach feure upgrade

def raceoutput (race):
    a=0
    while a < len(lf): 
        if lf[a].name==race:
            print('Rasse: \t {}'.format(lf[a].name))
            if lf[a].notes !=[]:
                print('Äußeres:')
                for n in lf[a].notes:
                    print(n)
            if lf[a].strength !=[]:
                print('Stärken:')
                for s in lf[a].strength:
                    print(s)
            if lf[a].weaknesses !=[]:
                print('Schwächen:')
                for w in lf[a].weaknesses:
                    print(w)
            a=len(lf)
        else:
            a=a+1
            
#raceoutput('Aurax')
def informationoutput (name):
    for p1 in p:
        if p1.prename==name or p1.familyname==name:
            print('Titel:\t {}'.format(p1.title))
            print('Vorname:\t {}'.format(p1.prename))
            print('Nachname\t {}'.format(p1.familyname))
            raceoutput(p1.lifeform.name)
            print('Größe:\t {}'.format(p1.size))
            print('Benutzerrechte:\t {}'.format(p1.userrights))
            print('Bedrohungsstufe: \t {}'.format(p1.threatlevel))
            if p1.notes!=[]:
                print('Bemerkungen:')
                for n in p1.notes:
                    print(n)
            
            

informationoutput('Trevor')
            