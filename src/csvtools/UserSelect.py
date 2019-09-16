import pandas as pd
import numpy as np
import sys

def selection(df,choice, pointA, pointB):
    if(choice==1):
        newDF=modify(df,pointA, pointB)
        return newDF
    else:
        return df

#modify the size of the data based on user. 
def modify(df, pointA, pointB):
    ptA, ptB=testPT(pointA, pointB)
    
    #get data specified
    row=[i for i in np.arange(ptA[0],ptB[0]+1)]
    col=[i for i in np.arange(ptA[1],ptB[1]+1)]
    newDF=myinfo.iloc[row,col]
    return newDF


def testPT(ptA,ptB):
    #test to put point higher in case of inversion
    if(ptA[0]>ptB[0]):
        ptA[0], ptB[0]=ptB[0],ptA[0]
    if(ptA[1]>ptB[1]):
        ptA[1],ptB[1]=ptB[1],ptA[1]
    return ptA, ptB
    
# #Testing Data**
# print("Starting...\n")
# fn="TestData/FrequencyDataTest.csv"
# #fn="TestData/IntervalDataTest.csv"
# #fn="TestData/OrdinalDataTest.csv"
# f = open(fn)
# myinfo = pd.read_csv(f)
# print(myinfo)

# print("\n\ntype: "+ str(type(myinfo)))
# print("modify-----\n\n\n")

# #Jada plans to use list var.
# #[row, col]
# ptA=[3,1]#default pointA
# ptB=[5,2]#default pointB ...todo remove later

# #if 1-to specify data
# #else-use all data so no change
# test=selection(myinfo, 1, ptA, ptB)

# print(test)
# print("\n\ntype: "+ str(type(test)))
# print("End--\n")
# #**Testing Data