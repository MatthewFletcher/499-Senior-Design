#!/usr/bin/env python3

import numpy as np
import statistics as s
import math as ma
from optparse import OptionParser
import sys
import inspect

#import StatisticsFortran as sf

#Check which OS is being run
from sys import platform
if platform == "linux" or platform == "linux2":
    import StatisticsFortranLinux as sf
elif platform == "darwin":
    # OS X
    import StatisticsFortranMac as sf
elif platform == "win32":
    import StatisticsWindows as sf
    sys.stderr.write("Windows not supported yet.\n")
    sys.exit(1)


class Statistics:
    '''
        This class consists of all tests that require only 1 vector.
    '''
    def __init__(self, d):
        self.d = d

    def s_max(self):
        '''
        Calculates the variance of a vector of data 
        Parameters: None
        Returns: Number
        '''
        return max(self.d)

    def s_min(self):
        '''
        Calculates the min of a vector of data 
        Parameters: None
        Returns: Number
        '''
        return min(self.d)

    def s_range(self):
        '''
        Calculates the range of a vector of data 
        Parameters: None
        Returns: Number
        '''
        return self.s_max() - self.s_min()
    
    def s_mean(self):
        '''
        Calculates the mean of a vector of data 
        Implemented in FORTRAN
        Parameters: None
        Returns: Number
        '''
        return sf.mean(self.d)
        #return sum(self.d)/len(self.d) 

    def s_median(self):
        '''
        Calculates the median of a vector of data 
        Parameters: None
        Returns: Number
        '''
        return sorted(self.d)[int(len(self.d) / 2)]
    
    def s_mode(self):
        '''
        Calculates the mode of a vector of data 
        Parameters: None
        Returns: Number if a mode exists, otherwise returns None.
        '''
        return self.d.value_counts().idxmax() if self.d.value_counts().max()==1 else None
    
    def s_var(self):
        '''
        Calculates the variance of a vector of data 
        Implemented in FORTRAN
        Parameters: None
        Returns: Number
        '''
        #https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/descriptive-statistics/sample-variance/
<<<<<<< HEAD
        return sum([(x - self.d.mean())**2 for x in self.d]) / (len(self.d) ) 
        #return sf.var(self.d)
        
=======
        try:
            return sf.var(self.d)
        except AttributeError:
            return sum([(x - self.d.mean())**2 for x in self.d]) / (len(self.d) ) 
>>>>>>> master

    def s_stddev(self):
        '''
        Calculates the std deviation of a vector of data 
        Parameters: None
        Returns: Number
        '''
        #return sf.stddev(self.d)
        return self.s_var() ** 0.5

    def s_zscore(self):
        '''
        Calculates the z score of each item in the list 
        '''

        return list(sf.zscore(self.d))

    def test_list(self):
        '''
        Returns a list of all methods in the Statistics class
        Parameters: None
        Returns: List of tuples: (method_name, method)

        Exceptions: None
        '''
        return [m  for m in inspect.getmembers(self,predicate=inspect.ismethod) if m[0].startswith('s_')]



class Regression:
    '''
    This class consists of all tests that require 2 or more vectors.
    '''
    def __init__(self, a, x_col = 0, y_col = 1):
        self.df = a
        self.cols = a.T
        
        #TODO make this less janky
        self.xcol = a.iloc[:,x_col]
        self.ycol = a.iloc[:,y_col]

    def pearsonR(self):
        # http://onlinestatbook.com/2/describing_bivariate_df/calculation.html
        x = self.xcol
        y = self.ycol
        
        s1 = sf.pearson(self.xcol, self.ycol)
        return s1
        #^^^^^^^^^^^^^^^^^# 
        #FUNCTION ENDS HERE

        x_mean = np.mean(x)
        y_mean = np.mean(y)
        def num(x,y):
            numsum = 0
            for m,n in zip(x,y):
                numsum += ((m-np.mean(x)) * (n - np.mean(y)))
            return numsum

        def den(x,y):
            x_sum = 0
            y_sum = 0
            
            for m,n in zip(x,y):
                x_sum += (m - x_mean)**2
                y_sum += (n - y_mean)**2
            den = ma.sqrt(x_sum * y_sum)
            return den
    
        s2 =  num(x,y)/den(x,y)

        print(f"{s1}\t{s2}")

        return s1


    def r_linear(self):
        '''
        Calculates the line of best fit for 2 vectors of df
        Parameters: None
        Returns: Dictionary d
            d['slope'] = m
            d['y_int'] = b
            d['fit'] = score (TBD)

        # Reference: http://onlinestatbook.com/2/regression/intro.html
        '''

        #Save me some typing, set columns to single variables 
        x = self.xcol
        y = self.ycol

        try: 
            #Call subroutine
            out = sf.linear(x,y)
            d =  {'slope': out[1], 'y_int': out[0]}
            return d
        except AttributeError: 
            #Save more typing, calculate standard deviation
            x_std = np.std(self.xcol)
            y_std = np.std(self.ycol)
            
            #Calculate the y intercept
            b = self.pearsonR() * y_std / x_std

            #Calculate the slope
            m = self.mean(y) - b * self.mean(x)
            d['slope'] = m
            d['y_int'] = b
            return d 

    def r_normal(self):
        '''
        Calculates the normal distribution for the data
        '''
        pass
   
    def signtest(self):
        '''
        Runs a sign test on the data. 
        Returns: Boolean
                True:  Significant difference
                False: No significant difference
        '''
        z =  sf.signtest(self.xcol, self.ycol)

        #https://www.youtube.com/watch?v=K1RYSyAu7Hg
        #Everything in this comes from this video 
        #To whatever heavenly deity reads this, please let the video be correct
        crit_val = 1.96
        
        #If computed z is within critical value, fail to reject the null hypothesis
        return (abs(z) < crit_val)

    def spearman(self):
        '''
        Calculates spearman rank correlation coefficient
        Parameters: none
        Returns: value
        return sf.spearman(self.xcol, self.ycol)
        '''
        return sf.spearman(self.xcol, self.ycol)

    def makeDistributionList(self):
        return [m  for m in inspect.getmembers(self,predicate=inspect.ismethod)
                if m[0].startswith('r_')]

    def getBestDistribution(self):
        mles = []

        for distribution in distributions:
            pars = distribution.fit(df)
            mle = distribution.nnlf(pars, df)
            mles.append(mle)

        results = [(distribution.name, mle) for distribution, mle in zip(distributions, mles)]
        best_fit = sorted(zip(distributions, mles), key=lambda d: d[1])[0]
        print("Best fit reached using {}, MLE value: {}".format(best_fit[0].name, best_fit[1]))
