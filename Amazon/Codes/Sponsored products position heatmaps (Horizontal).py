#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code generates the positions of sponsored products for horizontal arrangmenet

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Baby wipes","Backpack","Bean bags","Bedsheet","Belt","Blanket","Coffee mugs","Desk","Detergent","Dumbbells and weights","Hand soap","Jackets","Jeans","Luggage","Mask","Mattresses","Pans","Paper Towel","Pens","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV stand","Wall clock","Wallet","Water bottle","Yoga Mat"]

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
    
    i=0
    data = []
    
    # here 60 is the number of products in the first page
    while i < 60:
        col = []
        col.append(int(int((df['Sponsored'][i]))))
        col.append(int(int((df['Sponsored'][i+1]))))
        col.append(int(int((df['Sponsored'][i+2]))))
        col.append(int(int((df['Sponsored'][i+3]))))
        # Here 4 is the number of columns in each row
        i+=4
        data.append(col)
    
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] += data[i][j]

print(result)
a = np.array(result)

fig, ax = plt.subplots(figsize=(10,10))

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
# Here 14 is the number of queries
plt.clim(0, 41) 
cbar = plt.colorbar(im)
cbar.set_ticks([0, 41])
cbar.set_ticklabels(["0", "41"])
plt.show()

