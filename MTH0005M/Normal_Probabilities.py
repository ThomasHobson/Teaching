'''
This script will produce probabilities for normal distributed data in three different cases.
'''

import numpy as np
import scipy.stats as stats
import math
import pandas as pd
import statistics

#Read Excel data
x = pd.read_excel("Red_Admiral_Data.xlsx", usecols="D").to_numpy().T
x=x[0,:]

#Calculate statistics
mu = np.mean(x)                #Calculate mean
variance = np.var(x)           #Calculate variance
sigma = math.sqrt(variance)    #Calculate standard deviation
print(sigma)
print(np.std(x))
print(statistics.stdev(x))
print(statistics.pstdev(x))

#Calculate P(X<x)
def lessthan(x):
    probabilitylessthan = stats.norm.cdf(x, mu, sigma)
    return(probabilitylessthan) 

#Calculate P(X>x)
def morethan(x):
    probabilitymorethan = 1 - lessthan(x)
    return(probabilitymorethan)

#Calculate P(x1<X<x2)
def between(x1, x2):
    if x1>=x2:
        print("x1 should be lower than x2")
    else:
      probabilitybetween = lessthan(x2) - lessthan(x1)
      return(probabilitybetween) 