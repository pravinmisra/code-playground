# -*- coding: utf-8 -*-
"""
Created on Thu May 22 18:47:31 2025

@author: Admin
"""

import pandas as pd

df = pd.read_excel("C:\\code-playground\\test_data\\score_data_1.xlsx")

no_of_students = df.shape[0]

no_of_columns = df.shape[1]

df['Total'] = df['Maths']+df['Physics']+df['Chemistry']+df['English']+df['Hindi']
df['Division'] = None

for i in range(0, df['Total'].shape[0]):
    if df['Total'][i] >= 425:
        df['Division'][i] = 'Outstanding'
    elif 400 <= df['Total'][i] < 425:
        df['Division'][i] = 'Excellent'
    elif 350 <= df['Total'][i] < 400:
        df['Division'][i] = 'Good'
    else:
        df['Division'][i] = 'Needs improvement'
  
df.to_excel("C:\\code-playground\\test_data\\score_data_2.xlsx")







        





