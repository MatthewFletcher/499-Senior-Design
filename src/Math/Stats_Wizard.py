import numpy as np
import statistics as s


class Regression:
    def __init__(self, a):
        self.data = a
        self.cols = a.T

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
        

        return 1


    def linear(self):
        '''takes in a set of xy coordinates and calculates linear regression
        model 
        Parameters: None
        Returns: Dictionary d
            d['slope'] = m
            d['y_int'] = b
            d['fit'] = score (TBD)

        # Reference: http://onlinestatbook.com/2/regression/intro.html
        '''
        pass 

        
    
    def normal(self):
        pass


