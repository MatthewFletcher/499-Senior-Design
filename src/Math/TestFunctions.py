import pandas as pd
import numpy as np
import sys


def mean(a):
    #dont use function literally add and divide
    #b=np.sum(a.iloc[:,:])
    print("inside mean function")
    xrow,ycol=a.shape
    labels=a.columns
    print(a.shape)
    test=a
    
    

    
    print(test)
    print("\n\ntype: "+ str(type(test)))

    # a=a.iloc[:,1]
    # look=np.sum(a.iloc[:])

    return a
def median(a):
    return np.median(a)
def var(a):
    return np.var(a)
def stdev(a):
    return np.std(a)
    
# #Testing Data**
print("Starting...\n")
fn="TestData/FrequencyDataTest.csv"
#fn="TestData/IntervalDataTest.csv"
#fn="TestData/OrdinalDataTest.csv"
f = open(fn)
myinfo = pd.read_csv(f)
print(myinfo)

print("\n\ntype: "+ str(type(myinfo)))
print("modify-----\n\n\n")

#Jada plans to use list var.
#[row, col]
ptA=[3,1]#default pointA
ptB=[5,2]#default pointB ...todo remove later

#if 1-to specify data
#else-use all data so no change
#test=selection(myinfo, 1, ptA, ptB)
test=mean(myinfo)



print(test)
print("\n\ntype: "+ str(type(test)))
print("End--\n")
# #**Testing Data