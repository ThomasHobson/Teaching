import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Load data
df = pd.read_excel("Red_Admiral_Data.xlsx", sheet_name = 0, usecols="B, D").to_numpy().T
x = df[0,:]
y = df[1,:]

#Plot 
plt.plot(x,y,'x')                                            #Plot co-ordinates with 'x'
m, b = np.polyfit(x,y,1) 
print(m , b)                                    #Produce linear regression equation
plt.plot(x, m*x+b)                                           #Plot linear regression
plt.title('Scatter Plot')                                    #Add title
plt.xlabel('Wingspan within 24 hours of emergence (mm)')     #Add x label based on first header
plt.ylabel('Mass within 24 hours of emergence (g)')          #Add y label based on second header
plt.show()