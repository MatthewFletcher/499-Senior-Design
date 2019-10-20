import math as m

def mean(arr):
    return sum(arr)/len(arr)

def var(arr):
    return sum([(x - mean(arr))**2 for x in arr]) / (len(arr) )

def stddev(arr):
    return m.sqrt(var(arr))

