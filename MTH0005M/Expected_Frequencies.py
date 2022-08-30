'''
This script will calculate the expected frequencies from a normal distribution.
'''

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
import pandas as pd

#Dataset and number of bins
x = pd.read_excel("Red_Admiral_Data.xlsx", usecols="C").to_numpy()
numberofbins = 5

#Calculate statistics
mu = np.mean(x)                #Calculate mean
variance = np.var(x)           #Calculate variance
sigma = math.sqrt(variance)    #Calculate standard deviation

#Produce bin limits
y = np.linspace(np.min(x),np.max(x),numberofbins+1)

#Calculate expected frequencies
expectedfrequencies = np.zeros((numberofbins, 2))                        #Produce array for inputting
expectedfrequencies[0,0]=y[0]                                            #Input first lower limit
expectedfrequencies[0,1]=stats.norm.cdf(y[1], mu, sigma) * len(x)        #Calculate first expected frequency

for i in range(1, numberofbins - 1):                                                              
   expectedfrequencies[i,0]=y[i]                                         #Input interior lower limits
   expectedfrequencies[i,1]=(stats.norm.cdf(y[i+1], mu, sigma) -  
                             stats.norm.cdf(y[i], mu, sigma)) * len(x)   #Calculate interior expected frequencies
   
expectedfrequencies[numberofbins-1,0]=y[numberofbins-1]                  #Input final lower limit
expectedfrequencies[numberofbins-1,1]=((1 - stats.norm.cdf(
                                       y[numberofbins-1], mu, sigma))
                                       * len(x))                         #Calculate final expected frequency

#Plotting the Expected Frequencies
width = y[2]-y[1]
plt.bar(expectedfrequencies[:,0], expectedfrequencies[:,1],width, align='edge', edgecolor='black')
plt.title('Expected Frequencies')
plt.xlabel('Wingspan / mm')
plt.ylabel('Frequency')
plt.style.use('ggplot')
plt.show()