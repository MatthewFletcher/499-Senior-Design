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
import inspect

#class: ds, function
class DataframeFunction:
    def __init__(self, d):
        self.d = self.vectorSplit(d)
        #ds=s.Statistics(listarray[1])

    def vectorSplit(self,df):
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
        listarray=self.vectorS2I(listarray)
        return listarray
    def vectorS2I(self,listarray):
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
            
                #listarray[x]=listarray[x].astype(np.int64)
        
            '''Note: String non numerical value left alone. e.g., Sample 1, Sample 2, ..., etc. '''

        return listarray

    def getFunctionsStat(self,listFunc):
        #listofdata d
        print("getfuncstat")
       
        for x in range(len(self.d)):
            
            check=self.d[x].astype(str).str.isnumeric()
            if(check.all()):
                print(self.d[x])
                for y in range(len(listFunc)):
                    clssObj=s.Statistics(self.d[x])
                    method=listFunc[y]
                    name=method[0]
                    addr=method[1]
                    method_to_call=getattr(clssObj,name)
                    result=method_to_call()
                    print(name, result)
        
           
        



def main():
    df=c.openFile("TestData/FrequencyDataTest.csv")[0]
    print(df)
    print("------")
    test=DataframeFunction(df)
    #if gui side needs to receive the testlist this(below) need to happen

    ds=s.Statistics(0)
    funcpath=ds.test_list()    
    test.getFunctionsStat(funcpath)
    

main()