#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate heatmap at positions where repetitions were observed

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Baby wipes","Backpack","Bean bags","Bedsheet","Belt","Blanket","Coffee mugs","Desk","Detergent","Dumbbells and weights","Hand soap","Jackets","Jeans","Luggage","Mask","Mattresses","Pans","Paper Towel","Pens","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV stand","Wall clock","Wallet","Water bottle","Yoga Mat"]
# list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Kettle","Keyboard","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","TV","USB C Cable","Vacuum cleaner","Washing machine"]

data_list = []
data_list1 = []

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

# result = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]

for j in range(len(list_of_names)):
    currlist = []
    currlist.append(list_of_names[j])
    print(list_of_names[j])
    dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]
    ASINS = []    
        
    for k in range(len(dates)):
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')

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
        ASIN=''
        
        while i < 60:
            if int(int((df['Sponsored'][i])))==1 and int(int((df['PL'][i])))==1:
                flag = 0
                rank = 0
                count = 1
                first_pos=1000
#                 result[int((i%22)/1)][(i%22)%1] = 1
                for ind in df.index:
                    if int(int((df['Sponsored'][ind])))==0:
                        rank += 1
                    if df['asin'][i] == df['asin'][ind] and i != ind and int(int((df['Sponsored'][ind])))==1:
                        count += 1
                        ASIN = df['asin'][i]
                        flag=1
                        print('ind',ind)
                        result[int((ind%15)/1)][(ind%15)%1] += 1
                        if first_pos==1000:
                            first_pos = ind
                if flag==1:
                    print(ASIN,count,dates[k],i)
                    
            i += 1
        
        currlist.append(ASIN)
        currlist.append(count)
        
    data_list.append(currlist)
    
fig, ax = plt.subplots(figsize=(10,10))

# For 4 cols and 15 rows
ax.set_xticks(np.arange(4))
ax.set_yticks(np.arange(15))

ax.set_xticklabels([1,2,3,4])
ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])


# ax.set_xticks(np.arange(1))
# ax.set_yticks(np.arange(22))

# ax.set_xticklabels([1])
# ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])

for y in range(len(result)):
    for x in range(len(result[0])):
        plt.text(x, y, '%.0f' % result[y][x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
im = plt.imshow( result, interpolation = 'none' , cmap = 'Reds' )

plt.clim(0, 2) 
cbar = plt.colorbar(im)
cbar.set_ticks([0, 2])
cbar.set_ticklabels(["0", "2"])
plt.show()    

