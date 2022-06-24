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






path = 'C:/Users/yashwanth/Desktop/btp/selects/'
dest = 'C:/Users/yashwanth/Desktop/btp/survey_csv/'
# qh = ['backpacks_clothesAndApparell_data','jeans_clothesAndApparell_data','water bottles_Kitchen_data','wall clock_homeDecor_data']
qh = ['water bottles_Kitchen_data','wall clock_homeDecor_data']
qv = ['washing machines']
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver1 = webdriver.Chrome(ChromeDriverManager().install())
url = "https://www.flipkart.com"

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

if __name__ == '__main__':
	for q in os.listdir(path) : 
		p = path + q 
		df = pd.read_csv(p)
		print('here')
		df['Images'] = '-'
		df['F-Description'] = '-'
		sd = ''
		for i in df.index :
			url = df['Link'][i]
			driver.get(url)
			soup = BeautifulSoup(driver.page_source, 'html.parser')
			images = None
			while images == None :
				try : 
					images = soup.find_all('meta',{'name': 'og_image'})
					image_url = str(images[0]).split('=')[1].split('"')[1]
					print(image_url)
				except : 
					time.sleep(10)
					images = None
					driver.refresh()
					time.sleep(10)
			df['Images'][i] = image_url
			if df['Ad'][i] == 1 :
				df['Ad'][i] = 'Advertisement'
			if df['Pvt'][i] == 1 : 
				df['Pvt'][i] = 'Private'
			description = 'SKU : ' + str(df['Data-id'][i]) + '\n' + 'Brand : ' + str(df['Brand'][i]) 
			# if df['F-assured'][i] == 1 :
			# 	sd = df['Description'][i]  +' '+ '<img class="alignnone wp-image-2672 size-full" src="http://65.0.75.99/wp-content/uploads/2022/04/f-assured-e1650201274159.png" alt="" width="100" height="27" />'
			# df['Description'][i] = sd
			df['F-Description'][i] = description
			name = 'C:/Users/yashwanth/Desktop/btp/survey_csv/' + str(q) + '.csv'
			df.to_csv(name)
			


	#	commenting out ---------------------------> 


	# for q in qv : 
	# 	p = path + 'vertical/' + q + '.csv'
	# 	df = pd.read_csv(p)
	# 	print('here')
	# 	df['Images'] = '-'
	# 	df['F-Description'] = '-'
	# 	for i in df.index :
	# 		url = df['Link'][i]
	# 		driver.get(url)
	# 		soup = BeautifulSoup(driver.page_source, 'html.parser')
	# 		images = soup.find_all('meta',{'name': 'og_image'})
	# 		image_url = str(images[0]).split('=')[1].split('"')[1]
	# 		df['Images'][i] = image_url
	# 		if df['Ad'][i] == 1 :
	# 			df['Ad'][i] = 'Advertisement'
	# 		if df['Pvt'][i] == 1 : 
	# 			df['Pvt'][i] = 'Private'
	# 		description = 'SKU : ' + str(df['Data-id'][i]) + '\n' + 'Brand : ' + str(df['Brand'][i]) 
	# 		if df['F-assured'][i] == 1 :
	# 			sd = df['Description'][i]  +' '+ '<img class="alignnone wp-image-2672 size-full" src="http://65.0.75.99/wp-content/uploads/2022/04/f-assured-e1650201274159.png" alt="" width="100" height="27" />'
	# 		df['Description'][i] = sd
	# 		df['F-Description'][i] = description
	# 		name = 'C:/Users/yashwanth/Desktop/btp/survey_csv/' + str(q) + '.csv'
	# 		df.to_csv(name)


	#	commenting out --------------------------->
