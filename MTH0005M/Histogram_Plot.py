'''
This script will produce a histogram of the data provided.
'''

import matplotlib.pyplot as plt
import pandas as pd

#Read Excel data
x = pd.read_excel("Red_Admiral_Data.xlsx", usecols="C").to_numpy()

#Produce histogram plot
plt.hist(x, bins = 5, edgecolor='black') 
plt.title('Distribution of Wingspan Data') 
plt.xlabel('Wingspan/mm') 
plt.ylabel('Frequency')
plt.style.use('ggplot')
plt.show()
