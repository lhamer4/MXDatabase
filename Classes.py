# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 14:43:02 2021

@author: LUKAS
"""

        

    
class vehicle:
    def __init__(self,name,clas):
        self.name=name
        self.clas=clas
        
class cities:
    def __init__(self,name,pop)    :
        self.name=name
        self.pop=pop
        
class location(cities,list):
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.notes=[]
    
class lifeform(list):
    def __init__(self,name,mintl):
        self.name=name
        self.mintl=mintl
        self.strength=[]
        self.weaknesses=[]
        self.notes=[]

class person(lifeform,list):
    def __init__(self,title,prename,familyname,lifeform,size,userrights,threatlevel):
        self.title=title
        self.prename=prename
        self.familyname=familyname
        self.lifeform=lifeform
        self.size=size
        self.userrights=userrights
        self.threatlevel=threatlevel
        self.notes=[]
        
class tatoos:
    def __init__(self,form,color,connection):
        self.form=form
        self.color=color
        self.connection=connection
        
class organisation:
    def __init__(self,name):
        self.name=name
    
class password(organisation):
    def __init__(self,organisation,code):
        self.organisation=organisation
        self.code=code

class transactions:
    def __init(self,cost,notes):
        self.cost=cost
        self.notes=notes