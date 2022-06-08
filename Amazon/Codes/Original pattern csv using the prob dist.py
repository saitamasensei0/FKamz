#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate the original pattern csv using the probability distribution

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Jeans","Wall clock","Yoga Mat","Water bottle"]

for j in range(len(list_of_names)):
    dataset = []
    csv_dataset = []
    print(list_of_names[j])
    
    i=0
    
    f_asins = []
    
    while i<40:
        Dict = {}
        curr = []
        dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]
        for k in range(len(dates)):
            df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')
            if df['asin'][i] in Dict.keys():
                Dict[df['asin'][i]] += 1
            else:
                Dict[df['asin'][i]] = 1
        
        for key in Dict:
            Dict[key] = float(Dict[key]/20)
        
        i += 1
        
        Dict = dict(sorted(Dict.items(), key=lambda item: item[1], reverse = True))
        
        curr.append(i)
        curr.append(Dict)
        dataset.append(curr)
        
        for key in Dict:
            if (key not in f_asins):
                f_asins.append(key)
                break
    
    for i in f_asins:
        csv_curr = []
        flag = 0
        dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]
        for k in range(len(dates)):
            df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')
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
                    csv_dataset.append(csv_curr)
                    flag = 1
                    break
            if flag == 1:
                break
    
    frame = pd.DataFrame(dataset, columns = ['Rank','Probability distn'])
    frame1 = pd.DataFrame(csv_dataset, columns = ['asin','title','brand','Sponsored','Best Seller',"Amazon's Choice",'Price','Rating','NoofRatings','Discount','Delivery','Prime Delivery','base'])
    print(frame1)
    print(frame)
    print(f_asins)
    print(len(f_asins))
    frame1.to_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist.csv')

