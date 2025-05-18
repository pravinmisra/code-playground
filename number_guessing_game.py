# -*- coding: utf-8 -*-
"""
Created on Sun May 18 22:49:29 2025

@author: Admin
"""

import random

print("Hi, Welcome to the number guessing game. \nYou have 7 chances to guess this number. Let's start")

lower_bound = int(input("enter the lower bound: "))
upper_bound = int(input("enter the upper bound: "))

num = random.randint(lower_bound, upper_bound)

ch = 7
gc = 0


while ch > gc:
    gc += 1
    guess = int(input("make a guess: "))
    if guess == num:
        print(f"congratulations, you guessed it correctly, it's {num}")
        break
    elif guess > num:
        print("you guess it too high")
    elif guess < num:
        print("you guessed it too low")
else:
    print("you have exhausted your chances, better luck next time!")
    
    



