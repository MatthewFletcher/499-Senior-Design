# #!/usr/vin/env python3


import statistics as s
import math as ma
import scipy.stats as st
from optparse import OptionParser
import inspect

import CSV_Wizard as c
import numpy as np
import Stats_Wizard as s
import pandas as pd

def main():
    df=c.openFile("TestData/FrequencyDataTest.csv")[0]
    print(df)
    print("------")
    vectorSplit(df)


def vectorSplit(df):
    '''
        Probelm: stat functions are design to take in a list e.g., [1, 2, 3, 4]
        Solutions: This should split dataframe into array of lists for easier management.
    '''

    headers = list(df.columns.values)
    xrow, ycol=df.shape
    '''
        Ever column is looped
    '''
    listarray=[]

    for x in range(ycol):     
        listarray.append(df[headers[x]])

    listarray=vectorS2I(listarray)

    print(listarray[1])
    ds=s.Statistics(listarray[1])
    print(ds.s_mean())
    print(ds.test_list())
    return listarray
def vectorS2I(listarray):
    '''
    Problem: String Numeric values are not taken into account for the stat functions
    Solution: This should convert them into int numerical values.
    '''
    '''
    Note: even if it is an int numerical value 
    '''
    for x in range(len(listarray)):
        check=listarray[x].astype(str).str.isnumeric() 
        if check.all():
            listarray[x]=listarray[x].astype(np.int64)
        '''Note: String non numerical value left alone. e.g., Sample 1, Sample 2, ..., etc. '''
    return listarray

main()