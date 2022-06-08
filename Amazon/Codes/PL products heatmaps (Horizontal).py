#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code generates heatmaps for horizontally arranged products

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Baby wipes","Backpack","Bean bags","Bedsheet","Belt","Blanket","Coffee mugs","Desk","Detergent","Dumbbells and weights","Hand soap","Jackets","Jeans","Luggage","Mask","Mattresses","Pans","Paper Towel","Pens","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV stand","Wall clock","Wallet","Water bottle","Yoga Mat"]
# list_of_names= ["Baby wipes","Detergent","Hand soap","Paper Towel","Tissue paper","Toilet paper","Towel"]
# list_of_names= ["Table lamp","Trimmer"]
# list_of_names= ["Backpack","Bedsheet","Belt","Jackets","Jeans","Luggage","Mask","Rain cover for backpack","Shoes","Socks","Sweaters","T-shirts for men","T-shirts for women","Wallet"]
# list_of_names= ["Desk","Mattresses","Shoe rack"]
# list_of_names= ["Blanket","Pens","Shower curtain","TV stand"]
# list_of_names= ["Bean bags","Pillows","Wall clock"]
# list_of_names= ["Coffee mugs","Pans","Water bottle"]
# list_of_names= ["Dumbbells and weights","Skipping rope","Sports gloves","Sports shoes","Yoga Mat"]

# Result is the no. of rows and cols in the first page
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
         ]

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
    
    # here 60 is the number of products in the first page
    while i < 60:
        col = []
        col.append(int(int((df['PL'][i]))))
        col.append(int(int((df['PL'][i+1]))))
        col.append(int(int((df['PL'][i+2]))))
        col.append(int(int((df['PL'][i+3]))))
        # Here 4 is the number of columns in each row
        i+=4
        data.append(col)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] += data[i][j]

print(result)
a = np.array(result)

fig, ax = plt.subplots(figsize=(10,10))

# For 4 cols and 15 rows
ax.set_xticks(np.arange(4))
ax.set_yticks(np.arange(15))

ax.set_xticklabels([1,2,3,4])
ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

for y in range(len(result)):
    for x in range(len(result[0])):
        plt.text(x, y, '%.0f' % result[y][x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
im = plt.imshow( result, interpolation = 'none' , cmap = 'Reds' )
# Here 13 is the number of queries
plt.clim(0, 2) 
cbar = plt.colorbar(im)
cbar.set_ticks([0, 2])
cbar.set_ticklabels(["0", "2"])
plt.show()

