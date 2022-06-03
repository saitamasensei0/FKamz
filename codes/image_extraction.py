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






path = 'C:/Users/yashwanth/Desktop/DATA/feb_08_1pm/'
dest = 'C:/Users/yashwanth/Desktop/btp/survey_csv/'
# qh = ['backpacks_clothesAndApparell_data','jeans_clothesAndApparell_data','water bottles_Kitchen_data','wall clock_homeDecor_data']
qh = ['yoga mat_Sports_data']
qv = ['washing machines_Appliances_data']
 
driver = webdriver.Chrome(ChromeDriverManager().install())
# driver1 = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.flipkart.com"

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

if __name__ == '__main__':
	for q in qh : 
		p = path + 'horizontal/' + q + '.csv'
		df = pd.read_csv(p)
		print('here')
		df['Images'] = '-'
		df['F-Description'] = '-'
		for i in df.index :
			url = df['Link'][i]
			try : 
				driver.get(url)
			except : 
				driver.quit()
				time.sleep(5)
				driver = webdriver.Chrome(ChromeDriverManager().install())
				time.sleep(5)
				driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			images = None
			while images == None :
				try : 
					images = soup.find_all('meta',{'name': 'og_image'})
					image_url = str(images[0]).split('=')[1].split('"')[1]
				except : 
					image_url = '---'
			df['Images'][i] = str(image_url)
			if df['Ad'][i] == 1 :
				df['Ad'][i] = 'Advertisement'
			if df['Pvt'][i] == 1 : 
				df['Pvt'][i] = 'Private'
			description = 'SKU : ' + str(df['Data-id'][i]) + '\n' + 'Brand : ' + str(df['Brand'][i]) 
			if df['F-assured'][i] == 1 :
				sd = str(df['Description'][i])  +' '+ '<img class="alignnone wp-image-2672 size-full" src="http://65.0.75.99/wp-content/uploads/2022/04/f-assured-e1650201274159.png" alt="" width="100" height="27" />'
			df['Description'][i] = sd
			df['F-Description'][i] = description
			name = 'C:/Users/yashwanth/Desktop/btp/survey_csv' +'sdkgfyusfdh'+ str(q) + '.csv'
			df.to_csv(name)