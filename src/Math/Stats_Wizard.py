import numpy as np
import statistics as s
import math as ma

class Regression:
    def __init__(self, a, x_col = 0, y_col = 4):
        self.data = a
        self.cols = a.T
        
        #TODO make this less janky
        self.xcol = a.iloc[:,x_col]
        self.ycol = a.iloc[:,y_col]

    def range(self):
        return [np.amax(col) - np.amin(col) for col in self.data.T]
    
    def mean(self):
        return np.avg(self.data)

    def mode(self):
        pass

    def median(self):
        return np.median(self.data)

    def var(self):
        return np.var(self.data)

    def stddev(self):
        return np.std(self.data)        

    def pearsonR(self):
        # http://onlinestatbook.com/2/describing_bivariate_data/calculation.html
        x = self.xcol
        y = self.ycol
        
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
                y_sum += (m - y_mean)**2
            den = ma.sqrt(x_sum * y_sum)
            return den
        

        return num(x,y)/den(x,y)


    def linear(self):
        '''
        Calculates the line of best fit for 2 vectors of data
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

        #Save more typing, calculate standard deviation
        x_std = np.std(self.ycol)
        y_std = np.std(self.ycol)
        
        #Calculate the y intercept
        b = self.pearsonR() * y_std / x_std

        #Calculate the slope
        m = np.mean(y) - b * np.mean(x)
    
        #Creation of dictionary for returning
        d = {}
        d['slope'] = m
        d['y_int'] = b

        return d 
    
    def normal(self):
        pass


