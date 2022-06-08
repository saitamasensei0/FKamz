#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate the probability distribution (dumped into csvs)

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

list_of_names= ["Backpack","Jeans","Wall clock","Yoga Mat","Water bottle"]

for j in range(len(list_of_names)):
    dataset = []
    print(list_of_names[j])
    
    i=0
    
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
        curr.append(i)
        curr.append(Dict)
        dataset.append(curr)
        
    frame = pd.DataFrame(dataset, columns = ['Rank','Probability distn'])
    print(frame)
    frame.to_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_Prob dist.csv')

