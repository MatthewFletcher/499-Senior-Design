import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

 #dont use function literally add and divide
 #list vector
def mean(df):
    #test=np.mean(df) Check: match
    #print(test)
    #Add each columns values total
    #newDF=df.append(df.sum(numeric_only=True)/len(df),ignore_index=True)  #newDF=pd.DataFrame(df.sum(numeric_only=True)/len(df))
    #retrive the last row which is the mean result.
    #newDF=newDF[len(newDF)-1:]
    #newDF=sum(self.df)/len(self.df) #Issue: passing as Dataframe right?
    newDF=df.sum()/len(df)
    # xrow, ycol=np.shape(df)
    # for x in ycol:
    #     print('l')

    return newDF

def median(df):
    sortdf=np.sort(df) #sort low to high

    num=((len(df)-1)/2)
    #if odd find the middle value
    if(len(df)%2!=0):
        df=sortdf[num]
    else:
        df=(sortdf[num]+sortdf[num+1])/2
    return df
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
myinfo=np.array([100, 50, 81,40])
test=mean(myinfo)
print(test)

# headers = list(test.columns.values)
# print("----------@")
# print(headers)

# # #for title in headers:

# x = test[headers[1]]
# y = test[headers[2]]
# print(x)
# print(y)
# plt.scatter(30,30)
# plt.scatter(20,70)
# plt.scatter(x,y)
# plt.show()



print("\n\ntype: "+ str(type(test)))
print("End--\n")
# #**Testing Data