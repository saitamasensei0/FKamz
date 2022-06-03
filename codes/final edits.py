from cmath import nan
import csv
import pandas as pd
import time
import os
import parsers
import midend
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests



# 
# Final cosmetic changes to the CSVs
# 

dest = 'C:/Users/yashwanth/Desktop/btp/survey_csv_final/'
path = 'C:/Users/yashwanth/Desktop/btp/survey_csv/'
queries = ['backpacks_clothesAndApparell_data','jeans_clothesAndApparell_data','water bottles_Kitchen_data','wall clock_homeDecor_data''washing machines']
spl = '<img class="alignnone wp-image-2672 size-full" src="http://65.0.75.99/wp-content/uploads/2022/04/f-assured-e1650201274159.png" alt="" width="100" height="27" />'


def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

if __name__ == '__main__':
    for q in os.listdir(path) :
        print(q)
        df = pd.read_csv(path+str(q))
        df['cat'] = q.split('_')[0]
        df = df.drop('Unnamed: 0', 1)
        for i in df.index :
            sd = df['Description'][i]
            sd = sd.split(spl)[0]
            if df['Ad'][i] == 'Advertisement' :
                YES = 1
                # sd = '<span style="font-size: 10pt; color: #999999;">Advertisement</span>'+'\n'+sd
            # if not df['Rating'][i] == '-' :
            #     sd = sd +'\n' + '<span style="color: #fff; background: #008000;">  4.3 ♣  </span>' 
            #     if not df['#Ratings'][i] == '-' :
            #         ratings = df['#Ratings'][i]
            #         sd = sd+' ' + '<span style="color: #808080;">'+str(ratings)+' </span>' 
            #         if df['F-assured'][i] == 1 :
            #             sd = sd+' ' + spl
            else :
                if df['F-assured'][i] == 1 :
                    sd = sd 
            if sd == '- ' : 
                sd =''
            d = 'SKU : ' + str(df['Data-id'][i])
            if df['Data-id'][i] == 'BAGFMC3ZKNRGUFJK' :
                print(df['Brand'][i])
            if pd.isna(df['Brand'][i]) :
                nothing = 1
            else : 
                d += '\n'+'Brand : ' + str(df['Brand'][i]) 
            df['Description'][i] = sd 
            df['F-Description'][i] = d
        name = dest + str(q) + '.csv'
        df.to_csv(name)
                
