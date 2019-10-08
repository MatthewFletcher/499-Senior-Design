import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels
import csv
import CSV_Wizard
import UserSelect

# This function will graph the data imported by default
# without any restrictions.
def graph(df):
    x = df[" Expected Freq."]
    y = df[" Actual Freq."]
    plt.title("Frequency Data")
    plt.xlabel("Expected Frequency")
    plt.ylabel("Actual Frequency")

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    myinfo = CSV_Wizard.openFile("../../TestData/FrequencyDataTest.csv")
    #contains numpy array
    d = myinfo[0]
    graph(d)