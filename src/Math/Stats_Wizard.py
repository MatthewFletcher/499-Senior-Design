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
#print(f"Platform: {platform}")
if platform == "linux" or platform == "linux2":
    import StatisticsFortranLinux as sf
elif platform == "darwin":
    # OS X
    import StatisticsFortranMac as sf
elif platform == "win32":
    import StatisticsFortranWindows as sf
else:
    sys.stderr.write("ERROR: Unsupported platform\\n")
    sys.exit(1)

'''
HOW TO USE:

    So this is a hair confusing but it seems like the best way to implement
    this. 
    For all 1D arrays: Instantiate an instance of the Statistics class. 
        s = Statistics(dataVector)

        To use a test, use:

        foo = s_testName(s) #From the statistics class instantiated above

        foo.name returns the name
        foo.func() returns the value of the test
    Please don't shoot me. This is like the 8th thing I've tried. 

'''

class Statistics:
    '''
        This class consists of all tests that require only 1 vector.
    '''
    def __init__(self, d):
        if not hasattr(d, '__iter__'):
            print(f"Type of data: {type(d)} is not list-like")
            sys.stderr.write('Invalid Data type entered\n')
            sys.exit(1)
        else:
            self.d = d

class s_max(Statistics):
    '''
    Calculates the variance of a vector of data 
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Max Value"
    def func(self):
        return sf.maximum(self.d)
    def __call__(self):
        return self.func()


class s_min(Statistics):
    '''
    Calculates the min of a vector of data 
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Min"
    def func(self):    
        return sf.minimum(self.d)
    def __call__(self):
        return self.func()


class s_range(Statistics):
    '''
    Calculates the range of a vector of data 
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Range"
    def func(self):
        return sf.range(self.d)
    def __call__(self):
        return self.func()

class s_mean(Statistics):
    '''
    Calculates the mean of a vector of data 
    Implemented in FORTRAN
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Mean"
    def func(self):
        return sf.mean(self.d)
    def __call__(self):
        return self.func()

class s_median(Statistics):
    '''
    Calculates the median of a vector of data 
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Median"
    def func(self):
        return sorted(self.d)[int(len(self.d) / 2)]
    def __call__(self):
        return self.func()

class s_mode(Statistics):
    '''
    Calculates the mode of a vector of data 
    Parameters: None
    Returns: Number if a mode exists, otherwise returns None.
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Mode"
    def func(self):
        return self.d.value_counts().idxmax() if self.d.value_counts().max()==1 else None

    def __call__(self):
        return self.func()

class s_var(Statistics):
    '''
    Calculates the variance of a vector of data 
    Implemented in FORTRAN
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Variance"
    #https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/descriptive-statistics/sample-variance/
    def func(self):
            return sf.var(self.d)
    def __call__(self):
        return self.func()

class s_stddev(Statistics):
    '''
    Calculates the std deviation of a vector of data 
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Standard Deviation"
    def func(self):
        return sf.stddev(self.d)
    def __call__(self):
        return self.func()

class s_varcoeff(Statistics):
    '''
    Calculates the coefficient of variation of a vector
    Parameters: None
    Returns: Number
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Coefficient of Variance"
    def func(self):
        return sf.stddev(self.d)
    def __call__(self):
        return self.func()

class s_zscore(Statistics):
    '''
    Calculates the z score of each item in the list 
    '''
    def __init__(self,d):
        super().__init__(d)
        self.name = "Z Score"
    def func(self):
        return list(sf.zscore(self.d))
    def __call__(self):
        return self.func()

#def test_list(self):
#    '''
#    Returns a list of all methods in the Statistics class
#    Parameters: None
#    Returns: List of tuples: (method_name, method)
#
#    Exceptions: None
#    '''
#    return [m  for m in inspect.getmembers(self,predicate=inspect.ismethod) if m[0].startswith('s_')]
#

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

class r_pearsonR(Regression):
    '''
    Calculates Pearson Regression correlation coefficient
    '''
    def __init__(self,a):
        super().__init__(a)
        self.name = "Pearson Regression Coefficient"
    def func(self):
        # http://onlinestatbook.com/2/describing_bivariate_df/calculation.html
        x = self.xcol
        y = self.ycol
        return sf.pearson(self.xcol, self.ycol)
    def __call__(self):
        return self.func()

class r_linear(Regression):
    '''
    Calculates the line of best fit for 2 vectors of df
    Parameters: None
    Returns: Dictionary d
        d['slope'] = m
        d['y_int'] = b
        d['equation'] = 'm*x + b'
    # Reference: http://onlinestatbook.com/2/regression/intro.html
    '''

    def __init__(self,a):
        super().__init__(a)
        self.name = "Line of Best Fit"
    def func(self):
        #Save me some typing, set columns to single variables 
        x = self.xcol
        y = self.ycol

        #Call subroutine
        out = sf.linear(x,y)
        d =  {'slope': out[1], 'y_int': out[0], 'equation': f"{out[1]}*x + {out[0]}"}
        return d

    def __call__(self):
        return self.func()

class r_signtest(Regression):
    '''
    Runs a sign test on the data. 
    Returns: Boolean
            True:  Significant difference
            False: No significant difference
    '''
    def __init__(self,a):
        super().__init__(a)
        self.name = "Line of Best Fit"
    def func(self):
        z =  sf.signtest(self.xcol, self.ycol)

        #https://www.youtube.com/watch?v=K1RYSyAu7Hg
        #Everything in this comes from this video 
        #To whatever heavenly deity reads this, please let the video be correct
        crit_val = 1.96
        
        #If computed z is within critical value, fail to reject the null hypothesis
        return (abs(z) < crit_val)
    def __call__(self):
        return self.func()

class r_spearman(Regression):
    '''
    Calculates spearman rank correlation coefficient
    Parameters: none
    Returns: value
    return sf.spearman(self.xcol, self.ycol)
    '''
    def __init__(self,a):
        super().__init__(a)
        self.name = "Spearman Correlation"
    def func(self):
        return sf.spearman(self.xcol, self.ycol)
    def __call__(self):
        return self.func()
