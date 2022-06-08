#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Code for image extraction from csv's

import selenium
from selenium import webdriver
import pandas as pd
import time
import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import statistics
from scipy.stats import spearmanr
from scipy import stats
from selenium.webdriver.common.keys import Keys

PATH = "C:/Users/Nikita/Downloads/chromedriver_win32 (1)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()
driver.get("https://www.amazon.in")
driver.implicitly_wait(2)

list_of_names= ["Yoga Mat","Backpack","Jeans","Wall clock","Water bottle"]

for j in range(len(list_of_names)):
    print(list_of_names[j])
    df = pd.read_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist.csv')
    df['image url'] = ""
    
    for ind in df.index:
        x = str(df['asin'][ind])
        print(x)
        search_input = driver.find_element_by_id("twotabsearchtextbox")
        search_input.clear()
        search_input.send_keys(x)
        search_input.send_keys(Keys.ENTER)
        
        try:
            img = driver.find_element_by_class_name('s-image-square-aspect').find_element_by_tag_name('img').get_attribute('src')
        except:
            img=""
            print(img)
        df['image url'][ind] = img
        print('img '+img,df['image url'][ind])

    print(df)
    df.to_csv("C:/Users/Nikita/Amazon_"+list_of_names[j]+'_after_Prob dist_original.csv')

