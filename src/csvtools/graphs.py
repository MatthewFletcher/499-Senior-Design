import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels
import csv
import CSV_Wizard
import UserSelect

# This function will graph the functional or interval data with no restrictions
def graph(df):
    headers = list(df.columns.values)
    print(df)

    #for title in headers:

    x = df[headers[1]]
    y = df[headers[2]]
    plt.title("Frequency Data")
    plt.xlabel(headers[1])
    plt.ylabel(headers[2])

    # Plot the points using matplotlib
    plt.plot(x, y)
    plt.show()

# This function will graph the ordinal data with no restriction
def ordinal(df):
    headers = list(df.columns.values)
    # Remove the Question # column
    headers.pop(0)
    x = headers
    y = []
    for header in headers:
        y.append(df[header].sum())

    plt.bar(x, y)
    plt.show()
    print(y)

if __name__ == '__main__':
    myinfo = CSV_Wizard.openFile("../../TestData/OrdinalDataTest.csv")
    #contains numpy array
    d = myinfo[0]
    ordinal(d)