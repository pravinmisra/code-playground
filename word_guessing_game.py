# -*- coding: utf-8 -*-
"""
Created on Mon May 19 20:23:16 2025

@author: Admin
"""

import random

words = ['apple','banana','cat','dog','elephant','fox','guerilla','habilitation']

word = random.choice(words)

name = input("what is your name? ")

print(f"Welcome {name}!")

guesses = ""
turns = 12

while turns > 0:    
    failed = 0
    guess = input("Guess a character of the word: ")
    guesses += guess
    for ch in word:        
        if ch in guesses:
            print(ch)
            guesses += ch
        else:
            print("_")
            failed += 1
            
    if(failed == 0):
        print(f"you win, the word is {word}")
        break
    else:
        turns -= 1
else:
    print("you have exhausted your chances! better luck next time..")
    

    


        