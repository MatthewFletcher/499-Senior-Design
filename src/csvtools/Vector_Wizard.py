#!/usr/vin/env python3


import statistics as s
import math as ma
import scipy.stats as st
from optparse import OptionParser
import inspect

import CSV_Wizard as c
import numpy as np
#import Stats_Wizard as s
import pandas as pd

def main():
    df=c.openFile("TestData/FrequencyDataTest.csv")[0]
    print(df)
    print("------")
    vectortest(df)

def vectortest(df):
    '''
        This should split dataframe into 1 vector for stats_wizard
    '''

    headers=list(df.columns.values)
    xrow, ycol=df.shape
    '''
        Ever column is looped
    '''
    for x in range(ycol):
        #print(df[headers[x]])
        #ds=s.Statistics(df[headers[x]])
    #way to collect every column and return    
        

    print('forloopend')
    print(len(df))
    print(df[headers[1]])
    print(sum(df[headers[1]])/len(df))

main()