#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate the zigzag pattern csv using the original pattern csv

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Backpack","Jeans","Water bottle","Wall clock","Yoga Mat"]

for j in range(len(list_of_names)):
    print(list_of_names[j])
    PL = []
    TP = []
    df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist.csv')

#     df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'1.csv')
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

    while i < 40:
        if df['PL'][i] == 1:
            PL.append(df['asin'][i])
        else:
            TP.append(df['asin'][i])
        i += 1

    i=0
    randomcsv = []
    csv_dataset = []
    tpi = 0
    pli = 0
    plranks = [1,4,14,21,24,34]
    
    while i<40: 
        value = random()
        if (i+1 in plranks):
            randomcsv.append(PL[pli])
            pli += 1
        else : 
            randomcsv.append(TP[tpi])
            tpi += 1
        i += 1
    
    for i in randomcsv:
        csv_curr = []
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist_original.csv')
        for ind in df.index:
            if df['asin'][ind] == i:
                csv_curr.append(df['asin'][ind])
                csv_curr.append(df['title'][ind])
                csv_curr.append(df['brand'][ind])
                csv_curr.append(df['Sponsored'][ind])
                csv_curr.append(df['Best Seller'][ind])
                csv_curr.append(df["Amazon's Choice"][ind])
                csv_curr.append(df['Price'][ind])
                csv_curr.append(df['Rating'][ind])
                csv_curr.append(df['NoofRatings'][ind])
                csv_curr.append(df['Discount'][ind])
                csv_curr.append(df['Delivery'][ind])
                csv_curr.append(df['Prime Delivery'][ind])
                csv_curr.append(df['base'][ind])
                csv_curr.append(df['image url'][ind])
                csv_dataset.append(csv_curr)
                break
    
    frame = pd.DataFrame(csv_dataset, columns = ['asin','title','brand','Sponsored','Best Seller',"Amazon's Choice",'Price','Rating','NoofRatings','Discount','Delivery','Prime Delivery','base','image url'])
    print(frame)
    frame.to_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist_zigzag.csv')

