#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Amazon Scraper Code

import pandas as pd
import time
import os
import sys
import json
from importlib import reload
reload(sys)
# sys.setdefaultencoding('utf8')
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import date
from datetime import datetime
import traceback
import os
from os import listdir
from os.path import isfile, join
import random
#import requests
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime

def search(query, driver):
	driver.get('https://www.amazon.in/')
	time.sleep(3)
	search_input = driver.find_element_by_id("twotabsearchtextbox")
	search_input.clear()
	time.sleep(2)
	search_input.send_keys(query)
	time.sleep(3)
	
	search_input.send_keys(Keys.ENTER)
	time.sleep(3)
	page_num = 0
	truth = True
	alldetails=[]
	while truth:
		if page_num != 0:
			next.click()
		time.sleep(5)
		page_num += 1
		print(query+'	'+str(page_num))
		print("===============Search rank component==============")
		#Search rank component of the SERP
		for rank_item in driver.find_elements_by_xpath("//*[contains(@class, 's-result-item s-asin')]"):
			asin = rank_item.get_attribute("data-asin")
            
			try:
				spons = rank_item.find_element_by_class_name("s-label-popover-default").text
				sponsored = "1"               
			except Exception as e:
				sponsored = "0"
				
			try:
				badges = rank_item.find_element_by_class_name("a-badge-text").text
				if badges == 'Best seller':
					bestseller = '1'
				else:
					bestseller = '0'
			except:
				bestseller = '0'
                
			try:
				ac = rank_item.find_element_by_class_name("a-badge-text").text
				if ac == "Amazon's":
					amazonChoice = '1'
				else:
					amazonChoice = '0'
			except:
				amazonChoice = '0'
			
			try:
				titleElement = rank_item.find_element_by_css_selector('.a-size-base-plus.a-color-base.a-text-normal')#xpath("//*[contains(@class, 'a-size-base-plus')]")
				title = titleElement.text
				try:
					brand = rank_item.find_elements_by_class_name('a-size-base')[0].text
				except:
					brand = ''
				try:
					base = rank_item.find_elements_by_class_name('a-size-base')[1].text
				except:
					base = ''
			except Exception as e:
				try:
					titleElement = rank_item.find_element_by_css_selector('.a-size-medium.a-color-base.a-text-normal')#xpath("//*[contains(@class, 'a-size-base-plus')]")
					title = titleElement.text
					brand = title.split()[0]
					base = rank_item.find_elements_by_class_name('a-size-base')[0].text
				except:
					title = ''
					brand = ''
					base = ''
					
			NumPresent = False
			for char in brand:
				if char.isnumeric():
					NumPresent = True
					break		
			if NumPresent:
				base = brand
				brand = title.split()[0]	
				
			try:
				ratingElement = rank_item.find_element_by_class_name('a-icon-alt')#_xpath("//*[contains(@class, 'a-icon-alt')]")
				rating = ratingElement.get_attribute("innerHTML")
				x = rating.find('o')
				if x==-1:
					rating = "0"
				else:
					rating = rating[0:x-1]
			except Exception as e:
				rating = '0'
            
			try:
				Noofratings = rank_item.find_element_by_class_name('a-size-small').find_element_by_class_name('a-size-base').text
			except:
				Noofratings="0"
			
			try:
				priceElement = rank_item.find_element_by_class_name('a-price-whole')
				price = priceElement.text
			except Exception as e:

				try:
					priceElement = rank_item.find_element_by_class_name('a-color-price')
					price = priceElement.text
				except:
					price = '0'
				
			try:
				discount = rank_item.find_element_by_class_name('s-price-instructions-style').find_element_by_class_name('a-color-base').text
				x = discount.rfind('(')
				if x==-1:
					discount="0"
				else:
					discount = discount[x+1:]
					y = discount.rfind(')')
					if discount[y-1]=='%':
						discount = discount[:y-1]
					else:
						discount="0"
			except:
				discount="0"
                    
			try:
				primeDelivery = rank_item.find_element_by_class_name('a-icon-prime')
				isPrimeDelivery = '1'
			except:
				isPrimeDelivery = '0'
                
			try:
				delivery = rank_item.find_element_by_class_name('s-align-children-center').find_element_by_class_name('a-text-bold').text
			except:
				delivery=""
				
			temp ={
				'asin':asin,
				'title':title,
				'brand':brand,
				'Sponsored':sponsored,
				'Best Seller':bestseller,
				"Amazon's Choice":amazonChoice,
				'Price':price,
				'Rating':rating,
				'NoofRatings':Noofratings,
				'Discount':discount,
				'Delivery':delivery,
				'Prime Delivery':isPrimeDelivery,
				'base':base,}
			alldetails.append(temp)
		try:
			next = driver.find_element_by_class_name('s-pagination-next')
			print('next')
		except:
			truth = False
		if next.get_attribute("aria-disabled") == "true":
			truth = False
		print(truth)
	pd.DataFrame(alldetails)
	data = pd.DataFrame(alldetails)
	data.to_csv('C:/Users/Nikita/Amazon_'+query+'_16 Feb_2.csv')


def main(query= ""):
	profile = webdriver.FirefoxProfile()
	options = Options()
	options = webdriver.FirefoxOptions()
	options.headless = True
	binary = FirefoxBinary("I:/Downloads/firefox")
	driver = webdriver.Firefox(firefox_profile=profile, executable_path=r'C:/Users/Nikita/Downloads/geckodriver-v0.30.0-win64/geckodriver.exe', service_log_path="C:/Users/Nikita/geckodriver.log")
	driver.set_page_load_timeout(60)
	driver.get('https://www.amazon.in')
	time.sleep(5)
		
	
	query_list= ["AAA batteries","Apple charger","Baby wipes","Backpack","Battery","Bean bags","Bedsheet","Belt","Blanket","Blender","Camera","Coffee mugs","Desk","Detergent","Display port to HDMI Cable","Dumbbells and weights","Gaming headset","Hand soap","HDMI Cable","Jackets","Jeans","Kettle","Keyboard","Luggage","Mask","Mattresses","Microwave","Monitor mount","Mouse","Mouse Pad","Nintendo switch case","Pans","Paper Towel","Pens","Phone case","Pillows","Rain cover for backpack","Shoe rack","Shoes","Shower curtain","Skipping rope","Socks","Sports gloves","Sports shoes","Sweaters","T-shirts for men","T-shirts for women","Table lamp","Tissue paper","Toilet paper","Towel","Trimmer","TV","TV stand","USB C Cable","Vacuum cleaner","Wall clock","Wallet","Washing machine","Water bottle","Yoga Mat"]

	for i in range(len(query_list)):
		if i%10==0:
			time.sleep(2)
		print(i,' Query ',query_list[i])
		print(os.getcwd())
		search(query_list[i], driver)
# 		time.sleep(1)
			
	driver.close()
	driver.quit()
    
if __name__ == "__main__":
	#error = True
	main()
	time.sleep(60)
	exit(0)	


# In[ ]:




