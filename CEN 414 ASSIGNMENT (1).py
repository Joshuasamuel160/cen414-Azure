#!/usr/bin/env python
# coding: utf-8

# In[4]:



import numpy as np
import pandas as pd
import matplotlib.pyplot as m
import pylab
import csv

with open('C:\\AFRICANDATA .csv') as File:  
    Line_reader = csv.reader(File)
    
x = []
y = []


  
with open('C:\\AFRICANDATA .csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    df=pd.DataFrame(reader)
    
Years=[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    
for i in range(4, 14, 1):
        x=list(df.iloc[:,0])
        y=df.iloc[:,i].astype(float)
        
        
        
        fig, ax = m.subplots(figsize=(15, 9))
        font1 = {'family':'serif','color':'black','size':15}
        font2 = {'family':'serif','color':'black','size':14}
        font3 = {'family':'serif','color':'black','size':14}
        m.bar(x, y, color = 'g', width = 0.72, label = "Public Expenditure")
        m.xticks(rotation = 90)
        m.yticks(rotation = 0)
        m.xlabel('COUNTRIES', fontdict = font2)
        m.ylabel('PERCENTAGES', fontdict = font3)
        m.title(f'PUBLIC EXPENDITURE ON EDUCATION PER PUPIL AS A PERCENTAGE OF GDP PER CAPITA BY LEVEL OF EDUCATION FOR {Years[i-4]}', fontdict = font1)
        m.legend()
        m.show()
        fig.savefig(f'.\static\imagesDATA{i}.png')

  

df = pd.read_csv('C:\\AFRICANDATA .csv')
print("\nFOR 2010")
print("Standard Deviation:") 
print(df['4.496590137'].std())
print("VARIANCE:")
print(df['4.496590137'].var())
print("RANGE:")
print((df['4.496590137'].max())-(df['4.496590137'].min()))

print("\nFOR 2011")
print("Standard Deviation:") 
print(df['4.385980129'].std())
print("VARIANCE:")
print(df['4.385980129'].var())
print("RANGE:")
print((df['4.385980129'].max())-(df['4.385980129'].min()))

print("\nFOR 2012")
print("Standard Deviation:") 
print(df['5.509039879'].std())
print("VARIANCE:")
print(df['5.509039879'].var())
print("RANGE:")
print((df['5.509039879'].max())-(df['5.509039879'].min()))

print("\nFOR 2013")
print("Standard Deviation:") 
print(df['4.621734858'].std())
print("VARIANCE:")
print(df['4.621734858'].var())
print("RANGE:")
print((df['4.621734858'].max())-(df['4.621734858'].min()))

print("\nFOR 2014")
print("Standard Deviation:") 
print(df['4.916950226'].std())
print("VARIANCE:")
print(df['4.916950226'].var())
print("RANGE:")
print((df['4.916950226'].max())-(df['4.916950226'].min()))

print("\nFOR 2015")
print("Standard Deviation:") 
print(df['5.079005003'].std())
print("VARIANCE:")
print(df['5.079005003'].var())
print("RANGE:")
print((df['5.079005003'].max())-(df['5.079005003'].min()))



print("\nFOR 2016")
print("Standard Deviation:") 
print(df['4.881084919'].std())
print("VARIANCE:")
print(df['4.881084919'].var())
print("RANGE:")
print((df['4.881084919'].max())-(df['4.881084919'].min()))

print("\nFOR 2017")
print("Standard Deviation:") 
print(df['5.02312994'].std())
print("VARIANCE:")
print(df['5.02312994'].var())
print("RANGE:")
print((df['5.02312994'].max())-(df['5.02312994'].min()))

print("\nFOR 2018")
print("Standard Deviation:") 
print(df['4.951634884'].std())
print("VARIANCE:")
print(df['4.951634884'].var())
print("RANGE:")
print((df['4.951634884'].max())-(df['4.951634884'].min()))

print("\nFOR 2019")
print("Standard Deviation:") 
print(df['4.719299793'].std())
print("VARIANCE:")
print(df['4.719299793'].var())
print("RANGE:")
print((df['4.719299793'].max())-(df['4.719299793'].min()))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




