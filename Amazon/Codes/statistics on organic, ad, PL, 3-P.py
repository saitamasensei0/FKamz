#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code to generate statistics on organic/ad/PL/3-P percentages, category wise and overall.

import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from random import random

dates= ["7 Feb_1","7 Feb_2","8 Feb_1","8 Feb_2","9 Feb_1","9 Feb_2","10 Feb_1","10 Feb_2","11 Feb_1","11 Feb_2","12 Feb_1","12 Feb_2","13 Feb_1","13 Feb_2","14 Feb_1","14 Feb_2","15 Feb_1","15 Feb_2","16 Feb_1","16 Feb_2"]

PL_O_S = []
PL_S = []
PL_O = []
Sp_PL = []
Or_PL = []

for k in range(len(dates)):
    list_of_names= ["Baby wipes","Backpack","Bean bags","Bedsheet","Belt","Blanket","Coffee mugs","Desk","Detergent","Dumbbells and weights","Hand soap","Jackets","Jeans","Luggage","Mask","Mattresses","Pans","Paper Towel","Pens","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV stand","Wall clock","Wallet","Water bottle","Yoga Mat"]
#     list_of_names= ["AAA batteries","Apple charger","Baby wipes","Backpack","Battery","Bean bags","Bedsheet","Belt","Blanket","Blender","Camera","Coffee mugs","Desk","Detergent","Display port to HDMI Cable","Dumbbells and weights","Gaming headset","Hand soap","HDMI Cable","Jackets","Jeans","Kettle","Keyboard","Luggage","Mask","Mattresses","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Pans","Paper Towel","Pens","Phone case","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV","TV stand","USB C Cable","Vacuum cleaner","Wall clock","Wallet","Washing machine","Water bottle","Yoga Mat"]
#     list_of_names= ["Baby wipes","Detergent","Hand soap","Paper Towel","Tissue paper","Toilet paper","Towel"]
#     list_of_names= ["Table lamp","Trimmer"]
#     list_of_names= ["Backpack","Bedsheet","Belt","Jackets","Jeans","Luggage","Mask","Rain cover for backpack","Shoes","Socks","Sweaters","T-shirts for men","T-shirts for women","Wallet"]
#     list_of_names= ["Desk","Mattresses","Shoe rack"]
#     list_of_names= ["Blanket","Pens","Shower curtain","TV stand"]
#     list_of_names= ["Bean bags","Pillows","Wall clock"]
#     list_of_names= ["Coffee mugs","Pans","Water bottle"]
#     list_of_names= ["Dumbbells and weights","Skipping rope","Sports gloves","Sports shoes","Yoga Mat"]

    C_Total = 0
    C_Total_PL = 0
    C_Total_Sp = 0
    C_Total_Or = 0
    C_Total_Sp_PL = 0
    C_Total_Or_PL = 0

# For horizontally arranged products in same category
    
    for j in range(len(list_of_names)):
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')
        df['PL'] = 0
#         print(dates[k],list_of_names[j])

        for ind in df.index:
            x = str(df['title'][ind]).find('Amazon')
            y = str(df['brand'][ind]).find('Amazon')
            x1 = str(df['title'][ind]).find('Presto')
            y1 = str(df['title'][ind]).find('Solimo')
            y2 = str(df['title'][ind]).find('Symbol')
            x3 = str(df['brand'][ind]).find('Presto')
            y3 = str(df['brand'][ind]).find('Solimo')
            y4 = str(df['brand'][ind]).find('Symbol')
            if x==-1 and y==-1 and x1==-1 and y1==-1 and y2==-1 and x3==-1 and y3==-1 and y4==-1:
                df['PL'][ind] = 0
            else:
                df['PL'][ind] = 1
        
#         i=0
        i=180
        
        while i<df.index[-1]:
#         while i<180:
            C_Total += 1
            if (int(df['PL'][i])) == 1:
                C_Total_PL += 1
            if (int(df['Sponsored'][i])) == 1:
                C_Total_Sp += 1
            if (int(df['Sponsored'][i])) == 0:
                C_Total_Or += 1
            if (int(df['Sponsored'][i])) == 1 and (int(df['PL'][i])) == 1:
                C_Total_Sp_PL += 1
            if (int(df['Sponsored'][i])) == 0 and (int(df['PL'][i])) == 1:
                C_Total_Or_PL += 1
            i += 1

# For vertically arranged products in same category
            
#     list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Keyboard","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","USB C Cable","Vacuum cleaner"]
#     list_of_names= ["Kettle","Microwave","TV","Washing machine"]
    list_of_names= ["AAA batteries","Apple charger","Battery","Blender","Camera","Display port to HDMI Cable","Gaming headset","HDMI Cable","Kettle","Keyboard","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Phone case","TV","USB C Cable","Vacuum cleaner","Washing machine"]
    
    for j in range(len(list_of_names)):
        df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_'+dates[k]+'.csv')
        df['PL'] = 0
#         print(dates[k],list_of_names[j])

        for ind in df.index:
            x = str(df['title'][ind]).find('Amazon')
            y = str(df['brand'][ind]).find('Amazon')
            x1 = str(df['title'][ind]).find('Presto')
            y1 = str(df['title'][ind]).find('Solimo')
            y2 = str(df['title'][ind]).find('Symbol')
            x3 = str(df['brand'][ind]).find('Presto')
            y3 = str(df['brand'][ind]).find('Solimo')
            y4 = str(df['brand'][ind]).find('Symbol')
            if x==-1 and y==-1 and x1==-1 and y1==-1 and y2==-1 and x3==-1 and y3==-1 and y4==-1:
                df['PL'][ind] = 0
            else:
                df['PL'][ind] = 1
        
#         i=0
        i=16*22
#         print(df.index[-1])
        
#         while i<11*22:
#         while i<66:
        while i<df.index[-1]:
            C_Total += 1
            if (int(df['PL'][i])) == 1:
                C_Total_PL += 1
            if (int(df['Sponsored'][i])) == 1:
                C_Total_Sp += 1
            if (int(df['Sponsored'][i])) == 0:
                C_Total_Or += 1
            if (int(df['Sponsored'][i])) == 1 and (int(df['PL'][i])) == 1:
                C_Total_Sp_PL += 1
            if (int(df['Sponsored'][i])) == 0 and (int(df['PL'][i])) == 1:
                C_Total_Or_PL += 1
            i += 1
#         print(C_Total,C_Total_PL,C_Total_Sp, C_Total_Or,C_Total_Sp_PL,C_Total_Or_PL )
    
    PL_O_S.append((C_Total_PL/C_Total)*100)
    if C_Total_Sp>0:
        PL_S.append((C_Total_Sp_PL/C_Total_Sp)*100)
    PL_O.append((C_Total_Or_PL/C_Total_Or)*100)
    if C_Total_PL>0:
        Sp_PL.append((C_Total_Sp_PL/C_Total_PL)*100)
        Or_PL.append((C_Total_Or_PL/C_Total_PL)*100)
        
print("%.2f" % statistics.mean(PL_O_S),"%.2f" % statistics.mean(PL_S),"%.2f" % statistics.mean(PL_O),"%.2f" % statistics.mean(Sp_PL),"%.2f" % statistics.mean(Or_PL))
print("%.2f" % statistics.stdev(PL_O_S),"%.2f" % statistics.stdev(PL_S),"%.2f" % statistics.stdev(PL_O),"%.2f" % statistics.stdev(Sp_PL),"%.2f" % statistics.stdev(Or_PL))

