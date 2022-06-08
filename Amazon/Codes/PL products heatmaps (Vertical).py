#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code generates heatmaps for vertically arranged products

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Kettle","Keyboard","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","TV","USB C Cable","Vacuum cleaner","Washing machine"]
# list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Keyboard","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","USB C Cable","Vacuum cleaner"]
# list_of_names= ["Kettle","Microwave","TV","Washing machine"]

result = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]

for j in range(len(list_of_names)):
    print(list_of_names[j])
    df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'1.csv')
    # here I have added the PL column to dataset
    df['PL'] = 0
    
    for ind in df.index:
        x = str(df['title'][ind]).find('Amazon')
        y = str(df['brand'][ind]).find('Amazon')
        x1 = str(df['title'][ind]).find('Presto')
        y1 = str(df['title'][ind]).find('Solimo')
        x2 = str(df['title'][ind]).find('Vedaka')
        y2 = str(df['title'][ind]).find('Symbol')
        x3 = str(df['brand'][ind]).find('Presto')
        y3 = str(df['brand'][ind]).find('Solimo')
        x4 = str(df['brand'][ind]).find('Vedaka')
        y4 = str(df['brand'][ind]).find('Symbol')
        if x==-1 and y==-1 and x1==-1 and y1==-1 and x2==-1 and y2==-1 and x3==-1 and y3==-1 and x4==-1 and y4==-1:
            df['PL'][ind] = 0
        else:
            df['PL'][ind] = 1
            
    i=0
    data = []
    
    # here 22 is the number of products in the first page
    while i < 22:
        col = []
        col.append(int(int((df['PL'][i]))))
        # Here 1 is the number of columns in each row
        i+=1
        data.append(col)

#     print(data)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] += data[i][j]

print(result)
a = np.array(result)

fig, ax = plt.subplots(figsize=(10,10))

ax.set_xticks(np.arange(1))
ax.set_yticks(np.arange(22))

ax.set_xticklabels([1])
ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])


for y in range(len(result)):
    for x in range(len(result[0])):
        plt.text(x, y, '%.0f' % result[y][x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
im = plt.imshow( result, interpolation = 'none' , cmap = 'Reds' )
# Here 7 is the number of queries
plt.clim(0, 4) 
cbar = plt.colorbar(im)
cbar.set_ticks([0, 4])
cbar.set_ticklabels(["0", "4"])
plt.show()

