import numpy as np
import scipy.stats as stats
import math
import pandas as pd

#Datasets
dataset1 = pd.read_excel("Red_Admiral_Data.xlsx", usecols="B").to_numpy()
dataset2 = pd.read_excel("Red_Admiral_Data.xlsx", usecols="C").to_numpy()

#Calculate statistics
differences = np.subtract(dataset1,dataset2)    #Calculate differences
mu = np.mean(differences)                       #Calculate mean
variance = np.var(differences)                  #Calculate variance
sigma = math.sqrt(variance)                     #Calculate standard deviation
sqrtn = math.sqrt(len(differences))             #Calculate sqrt of n
t = (mu*sqrtn)/sigma                            #Calculate t

#Print statistics
print("mu=", mu)
print("stdev=", sigma)
print("t=",t)