import numpy as np
import scipy.stats as stats
import math
import pandas as pd

#Datasets
df = pd.read_excel("Red_Admiral_Data.xlsx", sheet_name = 0, usecols="B, D").to_numpy().T
x = df[0,:]
y = df[1,:]

#Calculate r
r=stats.spearmanr(x,y)

print("r=",r[0])