# -*- coding: utf-8 -*-
"""
Created on Wed May 21 23:15:47 2025

@author: Admin
"""

user_input = input("Enter a value or 'None': ")

if user_input.lower() == 'none':
    value = None
else:
    try:
        value = int(user_input)
    except ValueError:
        try:
            value = float(user_input)
        except ValueError:
            value = user_input
            
print("you entered: ", value)
print("type of value is: ",type(value))
        

