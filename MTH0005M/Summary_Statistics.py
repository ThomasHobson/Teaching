'''
This script will calculate six summary statistics;
arithmetic mean, median, mode, range, standard deviation, interquartile range
'''

import scipy.stats as stats
import numpy as np
import pandas as pd

#Load Excel data
data = pd.read_excel("Red_Admiral_Data.xlsx", usecols="B").to_numpy()

#Calculate summary statistics
mean = np.mean(data)
median = np.median(data)
mode = stats.mode(data)
range = np.amax(data) - np.amin(data)
stdev = np.std(data)
iqr = np.percentile(data,75) - np.percentile(data,25)

#Print summary stastics
print("mean=", mean)
print("median=", median)
print("mode=", mode)
print("range=", range)
print("stdev=", stdev)
print("iqr=", iqr)
