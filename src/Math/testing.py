#!/usr/bin/env python3

import CSV_Wizard as c
import numpy as np
import Stats_Wizard as s
import pandas as pd
import matplotlib.pyplot as plt 
import sys



df = c.openFile("TestData/sat.csv")[0]

#r = s.Regression(df, x_col = 0, y_col = 4)
ds = s.Statistics(df['high_GPA'])

#x = df['high_GPA']
#y = df['univ_GPA']


'''
plt.scatter(x,y, c="blue", s = 0.5)

x = np.linspace(min(x), max(x), 1000)
d = r.r_linear()
y = [d['slope'] * i + d['y_int'] for i in x]
plt.scatter(x,y, color='orange', s = 0.5)


plt.show()
'''


