# -*- coding: utf-8 -*-
"""
Created on Thu May 29 19:56:25 2025

@author: Admin
"""

import datetime, random

#print(datetime.__file__)

#print(random.__file__)

num_rand = int(input("enter the number of random birth dates you want this program to generate==>  "))
year = int(input("enter the year in YYYY format for which you want to generate these birth dates==> "))

def getBirthDays(numOfBirthDays):
    
    birthDays = []
    
    for i in range(numOfBirthDays):
    
        startOfYear = datetime.date(year,1,1)
        
        randomBirthDate = startOfYear + datetime.timedelta(random.randint(0, 364))
        
        birthDays.append(randomBirthDate)
        
    return birthDays

randomBirthDays = getBirthDays(num_rand)
randomBrithDaysInStr = []

#print(randomBirthDays)

def getBirthDaysInStr():
    for dte in randomBirthDays:
        fdte = dte.strftime("%Y-%m-%d")
        randomBrithDaysInStr.append(fdte)
    return randomBrithDaysInStr

print(getBirthDaysInStr())
    
    

    
    

