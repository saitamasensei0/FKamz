#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This code generates the positions of sponsored products for vertical arrangmenet

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Kettle","Keyboard","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","TV","USB C Cable","Vacuum cleaner","Washing machine"]

result = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]

for j in range(len(list_of_names)):
    print(list_of_names[j])
    df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'1.csv')
            
    i=0
    data = []
    
    # here 21 is the number of products in the first page
    while i <= 21:
        col = []
        col.append(int(int((df['Sponsored'][i]))))
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
plt.clim(0, 20) 
cbar = plt.colorbar(im)
cbar.set_ticks([0, 20])
cbar.set_ticklabels(["0", "20"])
plt.show()

