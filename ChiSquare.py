# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:58:20 2019

@author: kdandebo
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
ChiSquare = pd.ExcelFile('C:/Users/kdandebo/Desktop/Models/DS training/Yogesh data sets/Bahaman.xlsx')
ChiSquare = ChiSquare.parse("Sheet1")
print(ChiSquare.columns)
conv_arr= ChiSquare.values

ps = pd.Series([tuple(i) for i in conv_arr])
counts = ps.value_counts()
print(counts)

obs = np.array([[183,179,175,178], [17,21,25,22]])
print(chi2_contingency(obs))