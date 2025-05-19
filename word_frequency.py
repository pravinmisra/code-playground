# -*- coding: utf-8 -*-
"""
Created on Sun May 18 12:31:46 2025

@author: Admin
"""

user_input = input("enter text of your choice for which you want to know the word frequency: ")

def word_frequency(text):
    """
    calculates word frequency.

    Parameters
    ----------
    text : a string (text).

    Returns
    -------
    a dictionary containing words (in the text) as keys and their number of occurrences as values.

    """
    
    words = text.split()
    # print(type(words))
    # print(words)
    
    word_counts = {}
    
    for word in words:
        word = word.strip('.,!?"').lower()
        if word:
            word_counts[word] = word_counts.get(word,0)+1
        
    return word_counts
            
        
    
frequency_dict = word_frequency(user_input)

print(frequency_dict)