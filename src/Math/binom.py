import numpy as np
import matplotlib.pyplot as plt
import math as m
from decimal import Decimal

def binom(x):
    mu = 0
    sigma = 1
    return m.exp((-(x-mu)**2) / 2*sigma**2) / m.sqrt(2*m.pi * sigma**2)

def lin(x):
    return 2*x

def integrate(fn, start, end, delta):
    total = 0
    area = 0
    for x in np.arange(start,end,delta):
        a = fn(x)
        b = fn(x+delta)
        area = delta * (a+b)/2
        total += area
    return total

def main():
    a = -5
    b = 5
    delta = 0.01
   
    yvals = []
    for b in np.arange(a+delta, b+delta,delta):
        val = integrate(binom, a,b,delta)
        yvals.append(val)
    

   
    xvals = np.arange(a,b,delta) 
    if True:
        outfile = "zscore.txt"
        with open(outfile, "w") as f:
            for x,y in zip(xvals, yvals):
                f.write(f"{x:.2f},{y:.20f}\n")
    plt.plot(xvals,yvals)
    plt.grid()
    #plt.show()
if __name__ == "__main__":
    main()
