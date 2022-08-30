import numpy as np
import scipy.stats as stats
import math
import pandas as pd

#Datasets
dataset1 = pd.read_excel("Red_Admiral_Data.xlsx", sheet_name = 0, usecols="B").to_numpy()
dataset2 = pd.read_excel("Red_Admiral_Data.xlsx", sheet_name = 1, usecols="B").to_numpy()

#Calculate statistics
mu_1 = np.mean(dataset1)                             #Calculate mean of dataset 1
var_1 = np.var(dataset1)                             #Calculate variance of dataset 1
n_1 = len(dataset1)                                  #Calculate n in set 1
mu_2 = np.mean(dataset2)                             #Calculate mean of dataset 2
var_2 = np.var(dataset2)                             #Calculate variance of dataset 2
n_2 = len(dataset2)                                  #Calculate n in set 2
t = (mu_1-mu_2)/np.sqrt(((var_1/n_1)+(var_2/n_2)))   #Calculate t

#Print statistics
print("mu_1=", mu_1, "mu_2=", mu_2)
print("var_1=", var_1, "var_2=", var_2)
print("n_1=", n_1, "n_2=", n_2)
print("t=",t)