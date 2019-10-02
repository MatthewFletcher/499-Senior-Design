import numpy as np
import statistics as s
import math as ma
import scipy.stats as st

class Statistics:
    def __init__(self, d):
        self.d = d

    def max(self):
        return max(self.d)

    def min(self):
        return min(self.d)

    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return sum(self.d)/len(self.d) 

    def median(self):
        return sorted(self.d)[int(len(self.d) / 2)]
    
    def mode(self):
        #TODO Fix this
        return 1
    
    def var(self):
        return 4
        #TODO MAKE THIS STUPID FUNCTION WORK
        #https://www.statisticshowto.datasciencecentral.com/probability-and-statistics/descriptive-statistics/sample-variance/
        return sum([x - self.d.mean() for x in self.d]) / (len(self.d) ) 


    def stddev(self):
        return self.var() ** 0.5


class Regression:
    def __init__(self, a, x_col = 0, y_col = 4):
        self.df = a
        self.cols = a.T
        
        #TODO make this less janky
        self.xcol = a.iloc[:,x_col]
        self.ycol = a.iloc[:,y_col]

    def pearsonR(self):
        # http://onlinestatbook.com/2/describing_bivariate_df/calculation.html
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

    def makeDistributionList(self):
        distributions = [st.laplace, st.norm]

    def getBestDistribution(self):
        mles = []

        for distribution in distributions:
            pars = distribution.fit(df)
            mle = distribution.nnlf(pars, df)
            mles.append(mle)

        results = [(distribution.name, mle) for distribution, mle in zip(distributions, mles)]
        best_fit = sorted(zip(distributions, mles), key=lambda d: d[1])[0]
        print("Best fit reached using {}, MLE value: {}".format(best_fit[0].name, best_fit[1]))
