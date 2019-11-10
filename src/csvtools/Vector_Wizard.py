# #!/usr/vin/env python3


import statistics as s
import math as ma
import scipy.stats as st
from optparse import OptionParser
import sys, os
import numpy as np
from pathlib import Path
#TODO: GET A BETTER FIX
#setting the working directory vs code
sys.path.append(str(Path(os.getcwd()).joinpath("./src/Math").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("./src/csvtools").resolve()))

sys.path.append(str(Path(os.getcwd()).joinpath("../Math").resolve()))
sys.path.append(str(Path(os.getcwd()).joinpath("../csvtools").resolve()))

import CSV_Wizard as c
import Stats_Wizard as s
import pandas as pd
import inspect

#class: ds, function
class DataOneVector:
    def __init__(self, d):
        self.d = self.vectorSplit(d)

    def vectorSplit(self,df):
        '''
        Probelm: stat functions are design to take in a list e.g., [1, 2, 3, 4]
        Solutions: This should split dataframe into array of lists for easier management.
        '''
        '''
        Ever column is looped
        '''
        listarray=[]
        for column in df:
            listarray.append(df[column])
        listarrar=self.vectorS2I(listarray)
       
        return listarray
    def vectorS2I(self,listarray):
        '''
        Problem: String Numeric values are not taken into account for the stat functions
        Solution: This should convert them into int numerical values.
        '''
        '''
        Note: even if it is an int numerical value 
        '''
        for column in listarray:
            check=column.astype(str).str.isnumeric()
            if check.all():
                column=column.astype(np.int64)
       
        '''Note: String non numerical value left alone. e.g., Sample 1, Sample 2, ..., etc. '''

        return listarray

    def getFunctionsStat(self,listFunc):
        #listofdata d
        print("getfuncstat")
        #item i in list:
        #python best practice
        #for row in self.d:
        #TODO: CHANGE FOR LOOP FOR BETTER USE OF PYTHON--DONE
      
        dictlist=[]
        testdictlist={}

        for data in self.d:
            check=data.astype(str).str.isnumeric()
            if(check.all()):
                dic={}
                dic2=[]
                
                for func in listFunc:
                    clssObj=s.Statistics(data)
                    name=func[0]
                    addr=func[1]
                    method_to_call=getattr(clssObj,name)
                    result=method_to_call()

                    dic.update({name:result})
                    dic2.append(tuple((name,result)))
                
                dictlist=np.append(dictlist,dic)
                testdictlist.update({data.name: dic2})

        #dictionary list of dictionarys
        print(dictlist,'\n')
        print(dictlist[0])
        test=dictlist[0]
        print(test['s_max'])

        #dictionary list of tuples
        print('-------')
        print(testdictlist,'\n')
        print(testdictlist[' Expected Freq.'])
        test=testdictlist[' Expected Freq.']
        print(test[0])
        test2=test[0]
        print(test2[1])
        
        return testdictlist
  

'''
#dictionary list of tuples row {mean: 0}
cola {mean:0} {max: 0}
colb {etc..}
'''     
class DataTwoVector():
    def __init__(self, d):
        self.d = d
    def Running(self):
        print('inside')
        r=s.Regression(self.d)
        print(r.makeDistributionList())
        r.r_linear()

#'''
def main():
    df=c.openFile("TestData/FrequencyDataTest.csv")[0]
    print(df)
    print("------")
    test=DataOneVector(df)#----
    #if gui side needs to receive the testlist this(below) need to happen
    ds=s.Statistics(0)
    funcpath=ds.test_list()
    #ds.test_list() 
    #gui-testlist is changed based on user choice   
    #test.getFunctionsStat(funcpath)#-----
    test2=DataTwoVector(df)
    test2.Running()
    
#'''
main()