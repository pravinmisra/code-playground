# -*- coding: utf-8 -*-
"""
Created on Tue May 27 19:39:53 2025

@author: Admin
"""

import random

NUM_DIGITS = 3
TOTAL_GUESSES = 10

def main():
    guesses = 0
    while guesses < TOTAL_GUESSES:
        global secret_num
        secret_num = get_secret_num()
        print((secret_num))        
        if get_clues() == 1:
            break
        guesses += 1
    else:
        print("You have exhausted max number of attempts.")
    
def get_secret_num():
    secret_number = ''
    num_list = list('0123456789')
    random.shuffle(num_list)
    for i in range(NUM_DIGITS):
        secret_number += str(num_list[i])
    return secret_number

def get_clues():
    guessed_correctly = [1,1,1]
    guess = input("enter a guess: ")    
    
    for i in range(NUM_DIGITS):
        if guess[i] == secret_num[i]:
            print("Fermi..")
        elif guess[i] in secret_num:
            print("Pico..")
            guessed_correctly[i] = 0
        else:
            print("bagel..")
            guessed_correctly[i] = 0
    if guessed_correctly == [1,1,1]:
        print("you guessed it right")
        return 1
            
if __name__ == '__main__':
    main()
            
            
        
        
        
    
    


        
    
    