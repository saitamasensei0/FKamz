#Scraper 1 Flipkart

import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import time

start_time = time.ctime()
#Path for chrome driver in local machine
#Change it accordingly
path = 'C:/Users/yashwanth/Desktop/DATA/'
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver1 = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(PATH)
#driver1 = webdriver.Chrome(PATH)
url = "https://www.flipkart.com"

def get_url(search_term):
	template = 'https://www.flipkart.com/search?q={}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
	search_term = search_term.replace(' ','+')
	return template.format(search_term)

pvt_labels = ['adrenex','flipkart perfect homes studio','flipkart perfect homes junior','flipkart perfect homes','flipkart smartbuy','marq by flipkart','disney by miss & chief','marvel by miss & chief','miss & chief baby','justice league by miss & chief','miss & chief','billion','m7 by metronaut','metronaut','ann springs','cara mia','divastri','anmi'  ]
electronics = ['mobiles' ,'camera' ,'power bank','mobile chargers','trimmer','computer mouse','headphones' ,'laptop','mobile covers' ,'Battery','screen guards' ,'mobile cables' ,'mobile holders' ,'tempered glass' ]
sports = ['yoga mat','dumbells and weights' ,'badminton racquet' ,'football','sports shoes','sports gloves','cycles']
fashion = ['jeans' ,'shorts' ,'blanket','sweaters','Bedsheet','watches' ,'bags','t shirts','socks','masks','sandals' ,'clutch bags','jackets' ,'wallet','belt','backpacks']
appliances = ['gas stove' ,'microwave oven','fan' ,'ac','tv','refrigerators','washing machines','water purifier' ,'kettle' ]
# appliances = ['water purifier' ,'kettle' ]
furniture = ['table','tv entertainment unit','sofa' ,'shoe rack','dining set','chairs' ,'beds' ,'matresses' ,'wardrobe']
kids = ['baby footwear' ,'remote control toys' ,'toy guns ','baby innerwear' ]
kitchen = ['coffee mugs' ,'water bottles' ,'flask','lunch box','pans']
cleaning = ['cleaning gloves' ,'toilet brush']
decor = ['wall clock','bean bags' ,'pillows' ]
dic = [electronics,sports,fashion,appliances,furniture,kids,kitchen,cleaning,decor]
categories = ['Electronics','Sports','clothesAndApparell','Appliances','Furniture','Kids','Kitchen','cleaningSupplies','homeDecor']
# dic = [appliances,furniture,kids,kitchen,cleaning,decor]
# categories = ['Appliances','Furniture','Kids','Kitchen','cleaningSupplies','homeDecor']

for i in range(0,len(dic)) :
	category = categories[i]
	q = dic[i]
	print(category)
	print(q)
	if i>0 and i<7:
		time.sleep(300)
	for query in q:
		rank = 0
		data_list = []
		ultimate = 0
		for count in range (1,6):
			for page in range(1, 11):
				if ultimate == 4 and pageno >= 30 : 
					break
				elif ultimate == 1 and pageno >= 45 : 
					break
				pageno = (count-1)*10 + page
				print('Processing page no: ', pageno, ' ****************************************************************************************')

				#Change query here
				url = get_url(query)
				extension = '&page=' + str(pageno)
				url += extension
				driver.get(url)
				soup = BeautifulSoup(driver.page_source, 'html.parser')

				#for every row
				results = soup.find_all('div',{'class': '_1AtVbE col-12-12'})
				length = len(results)
				for result in results:
					next_div = result.find_all('div',{'class': '_13oc-S'})
					for item in next_div:
						#print(item)
						divs = item.find_all('div', {'style':'width: 25%;'})
						divs2 = item.find_all('div', {'style': 'width: 100%;'})
						#print(len(divs))   
						#print(len(divs2))
						#for 4 elements in a row
						if len(divs) == 4:
							ultimate = 4
							for div_tab in divs:
								element_list = []
								rank = rank + 1
								pvt = 0
								element_list.append(rank)
								element_list.append(div_tab.get('data-id'))
								atags = div_tab.find_all('a')
								spantag = div_tab.find_all('span')
								try : 
									brandname = div_tab.find('div',{'class' : '_2WkVRV'}).text
								except : 
									brandname = ""
								try :
									producttitle = div_tab.find('a',{'class' : 'IRpwTa'}).text
								except : 
									try : 
										producttitle = div_tab.find('a',{'class' : 's1Q9rs'}).text
									except : 
										try : 
											producttitle = div_tab.find('a',{'class' : '_4rR01T'}).text
										except :
											producttitle = ""
								try : 
									price = div_tab.find('div',{'class' : '_30jeq3'}).text
								except : 
									price = ""
								try :
									discount_intag = div_tab.find('div',{'class' : '_3Ay6Sb'})
									discounts = discount_intag.find_all('span')
									discount = discounts[0].text
								except :
									discount = '0' + '%' +  ' off'
								try : 
									f_image = div_tab.find('div',{'class' : '_1a8UBa'})
									if len(f_image.find_all('img')) == 1 :
										assured = 1
									else : 
										assured = 0
								except :
									try : 
										f_image = div_tab.find('div',{'class' : '_32g5_j'})
										if len(f_image.find_all('img')) == 1 :
											assured = 1
										else : 
											assured = 0
									except :
										assured = 0
								try : 
									description = div_tab.find('div',{'class':'_3Djpdu'}).text
								except :
									try : 
										description = div_tab.find('div',{'class':'_3eWWd-'}).text
									except :
										description = '-' 
								try : 
									rating = div_tab.find('div',{'class':'_3LWZlK'}).text
								except : 
									rating = '-'
								try : 
									nrating = div_tab.find('span',{'class':'_2_R_DZ'}).text
								except :
									nrating = '-'
								reviews = ""
								# div_tab.find_all('img')

								#for checking AD
								flag = 0
								for span in spantag:
									if span.text == 'Ad':
										flag = 1 #1 means it is advertised
										break
								element_list.append(flag)
								#ad part ends here
								for a in atags:
									if a.get('title'):
										product_url = 'https://www.flipkart.com' + a.get('href')
										break
								try : 
									spotlight = (((product_url.split('spotlightTagId')[1]).split('_')[0]).split('=')[1]).split('Id')[0]
								except : 
									spotlight = ""
								if pd.isna(brandname) or brandname == "" :
									for brand in pvt_labels :
										if brand in producttitle.lower() :
											brandname = brand
											break
								if brandname.lower() in pvt_labels : 
										pvt = 1	
								element_list.append(product_url)
								element_list.append(brandname)
								element_list.append(price)
								element_list.append(discount)
								element_list.append(assured)
								element_list.append(producttitle)
								element_list.append(description)
								element_list.append(rating)
								element_list.append(nrating)
								element_list.append(reviews)
								element_list.append(spotlight)
								element_list.append(pvt)
								data_list.append(element_list)
						elif len(divs2): 
							ultimate = 1
							pvt = 0
							for div_tab in divs2:
								element_list = []
								rank = rank + 1
								element_list.append(rank)
								element_list.append(div_tab.get('data-id'))
								atags = div_tab.find_all('a')
								spantag = div_tab.find_all('span')
								try : 
									brandname = div_tab.find('div',{'class' : '_2WkVRV'}).text
								except : 
									brandname = ""
								try :
									producttitle = div_tab.find('div',{'class' : '_4rR01T'}).text
								except :
									producttitle = ""
								try : 
									price = div_tab.find('div',{'class' : '_30jeq3'}).text
								except : 
									price = ""
								try :
									discount_intag = div_tab.find('div',{'class' : '_3Ay6Sb'})
									discounts = discount_intag.find_all('span')
									discount = discounts[0].text
								except :
									discount = '0' + '%' +  ' off'
								try : 
									f_image = div_tab.find('div',{'class' : '_13J9qT'})
									if len(f_image.find_all('img')) == 1 :
										assured = 1
									else : 
										assured = 0
								except :
									assured = 0
								description = ""
								# try : 
								# 	description = div_tab.find('div',{'class':'_3Djpdu'}).text
								# except :
								# 	try : 
								# 		description = div_tab.find('div',{'class':'_3eWWd-'}).text
								# 	except :
								# 		description = '' 
								try : 
									rating = div_tab.find('div',{'class':'_3LWZlK'}).text
								except : 
									rating = ''
								try : 
									rrr = div_tab.find('span',{'class':'_2_R_DZ'})
									spans = rrr.find_all('span')
									nrating = (spans[1].text).split(" ")[0]
									reviews = (spans[3].text).split(" ")[0]
								except :
									nrating = ""
									reviews = ""
								# try : 
								# 	reviews = div_tab.find('')
								# div_tab.find_all('img')

								#for checking AD
								flag = 0
								for span in spantag:
									if span.text == 'Ad':
										flag = 1 #1 means it is advertised
										break
								element_list.append(flag)
								#ad part ends here
								#for a in atags: 
								link = div_tab.find('a' ,{'class' :'_1fQZEK'})
								product_url = 'https://www.flipkart.com' + link.get('href')
								try : 
									spotlight = (((product_url.split('spotlightTagId')[1]).split('_')[0]).split('=')[1]).split('Id')[0]
								except : 
									spotlight = ""
								if pd.isna(brandname) or brandname == "" :
									for brand in pvt_labels :
										if brand in producttitle.lower() :
											brandname = brand
											break
								if brandname in pvt_labels : 
										pvt = 1	
								element_list.append(product_url)
								element_list.append(brandname)
								element_list.append(price)
								element_list.append(discount)
								element_list.append(assured)
								element_list.append(producttitle)
								element_list.append(description)
								element_list.append(rating)
								element_list.append(nrating)
								element_list.append(reviews)
								element_list.append(spotlight)
								element_list.append(pvt)
								data_list.append(element_list)
								



		frame = pd.DataFrame(data_list, columns = ['Rank', 'Data-id', 'Ad', 'Link', 'Brand', 'price', 'Discount', 'F-assured', 'Title','Description', 'Rating','#Ratings','#Reviews','Spotlight','Pvt'])
		# filenametosave = query + '_data.csv'
		filenametosave = query + '_' + category + '_data.csv'
		if ultimate == 4 :
			frame.to_csv(path + "horizontal/" + filenametosave)
		elif ultimate == 1 :
			frame.to_csv(path + "vertical/" + filenametosave)
end_time = time.ctime()
with open(path+'time_report.txt','a') as f :
	line = "started at " + str(start_time.split(" ")[3]) + ", ended at " + str(end_time.split(" ")[3])
	f.write(line)