#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate heatmaps for products having rating>4

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

for j in range(len(list_of_names)):
    print(list_of_names[j])
    dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]
      
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
        
    for k in range(len(dates)):
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')

        i=0
        data = []

        # here 60 is the number of products in the first page
        while i < 60:
            col = []
            if int(int((df['Rating'][i])))>=4:
                col.append(1)
            else:
                col.append(0)
            if int(int((df['Rating'][i+1])))>=4:
                col.append(1)
            else:
                col.append(0)
            if int(int((df['Rating'][i+1])))>=4:
                col.append(1)
            else:
                col.append(0)
            if int(int((df['Rating'][i+1])))>=4:
                col.append(1)
            else:
                col.append(0)
            # Here 4 is the number of columns in each row
            i+=4
            data.append(col)

        for m in range(len(data)):
            for n in range(len(data[0])):
                result[m][n] += data[m][n]

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
    plt.clim(0, 20) 
    cbar = plt.colorbar(im)
    cbar.set_ticks([0, 20])
    cbar.set_ticklabels(["0", "20"])
    plt.show()

