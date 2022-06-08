#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate the Heatmaps showing Organic ranking of Sponsored products (Vertical)

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Kettle","Keyboard","Microwave","Monitor mount","Mouse","Mouse Pad","Phone case","TV","USB C Cable","Vacuum cleaner","Washing machine"]
# "Nintendo switch case",

for j in range(len(list_of_names)):
    print(list_of_names[j])
    dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]
    result = []
    
    for k in range(len(dates)):
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')

        i=0

        while i < 22:
            if int(int((df['Sponsored'][i])))==1:
                flag = 0
                rank = 0
                for ind in df.index:
                    if int(int((df['Sponsored'][ind])))==0:
                        rank += 1
                    if df['asin'][i] == df['asin'][ind] and i != ind:
                        result.append(rank)
                        flag = 1
                        break
                if flag == 0:
                    result.append(450)
            i += 1
    
    result = np.reshape(result, (20, 6))
    result = result.T
    
    fig, ax = plt.subplots(figsize=(10,5))

    ax.set_xticks(np.arange(20))
    ax.set_yticks(np.arange(6))

    ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    ax.set_yticklabels([1,2,3,4,5,6])


    for y in range(len(result)):
        for x in range(len(result[0])):
            if result[y][x]==450:
                plt.text(x, y, "NA",
                         horizontalalignment='center',
                         verticalalignment='center', fontsize = 10
                         )
            else:
                plt.text(x, y, '%.0f' % result[y][x],
                         horizontalalignment='center',
                         verticalalignment='center', fontsize = 10
                         )
    im = plt.imshow( result, interpolation = 'none' , cmap = 'Reds' )
    # Here 7 is the number of queries
    plt.clim(0, 350) 
    cbar = plt.colorbar(im)
    cbar.set_ticks([0, 350])
    cbar.set_ticklabels(["0", "350"])
    plt.xlabel("Snapshots")
    plt.ylabel("Sponsored Rank")
    plt.show()

