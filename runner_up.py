# -*- coding: utf-8 -*-
"""
Created on Tue May 13 19:52:33 2025

@author: Admin
"""

user_input = input("Enter list of scores separated by commas: ")

#print(type(user_input))

list_of_values = user_input.split(',')

int_list_of_val = []

for x in list_of_values:
    int_list_of_val.append(int(x))

#print(type(list_of_values))

def find_runner_up_score(scores):
    '''Finds runner up score from the list of scores'''
    scores_set = set(scores)
    #print(type(scores_set))
    print(scores_set)
    
    if len(scores_set) < 2:
        return None

    scores_set.remove(max(scores_set))
    runner_up_score = max(scores_set)
    return runner_up_score

print(find_runner_up_score(int_list_of_val))

#print(find_runner_up_score.__doc__)
        