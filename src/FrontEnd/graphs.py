import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels
import csv

# This function will graph the inputted CSV files automatically without any options given
def default():
    x = []
    y = []
    with open('FrequencyDataTest.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter= ',')
        for row in plots:
            x.append(int(row[1]))
            y.append(int(row[2]))

    plt.plot(x, y)
    plt.title('Frequency Data')
    plt.xlabel('')
    plt.ylabel('')
    plt.show()