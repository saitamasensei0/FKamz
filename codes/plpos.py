import csv
import pandas as pd
import time
import os
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import matplotlib.pyplot as plt 
import requests

path = 'C:/Users/yashwanth/Desktop/DATA/'
# query = ['backpacks_clothesAndApparell_data','jeans_clothesAndApparell_data','water bottles_Kitchen_data','wall clock_homeDecor_data','yoga mat_Sports_data']
dest = 'C:/Users/yashwanth/Desktop/OLD_DATA/'

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

def heat_generator(list_of_names,label,flag) :
    data_list = []
    for j in range(len(list_of_names)):
        queryy = ((list_of_names[j].split('/')[-1]).split('.')[0]).split('_')[0]
        print(queryy)
        result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]
         ]
        element_list = []
        element_list.append(queryy)
        for dir in dirs :
            file = path+dir+'/'+flag + '/'+ list_of_names[j].split('/')[-1]
            # print(file)
            df = pd.read_csv(file)
            lst = []
            df['PL'] = 0
            sum = 0
            for ind in df.index :
                did = df['Data-id'][ind]
                x = df[label][ind]
                ads = df['Ad'][ind]
                if x==1 and ads ==1:
                    df['PL'][ind] = 1
                    if ind < 40 :
                        # print(did," ",ind) 
                        sum += 1
                else:
                    df['PL'][ind] = 0
            # print('\t',dir,'-',sum)
            element_list.append(sum)
            i=0
            data = []
            
            # here 60 is the number of products in the first page
            while i < 40:
                col = []
                col.append(int(int((df['PL'][i]))))
                col.append(int(int((df['PL'][i+1]))))
                col.append(int(int((df['PL'][i+2]))))
                col.append(int(int((df['PL'][i+3]))))
                # Here 4 is the number of columns in each row
                i+=4
                # print(i,col)
                data.append(col)

            # print(data)
        
            for i in range(len(data)):
                for k in range(len(data[0])):
                    result[i][k] += data[i][k]
            
        data_list.append(element_list)
        fig, ax = plt.subplots(figsize=(40,40))
        if flag =='horizontal' :
            # For 4 cols and 15 rows
            ax.set_xticks(np.arange(4))
            ax.set_yticks(np.arange(10))

            ax.set_xticklabels([1,2,3,4])
            ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10])
        maximum = -1
        for y in range(len(result)):
            for x in range(len(result[0])):
                    maximum = max (maximum,result[y][x])
                    plt.text(x, y, '%.0f' % result[y][x],
                        horizontalalignment='center',
                        verticalalignment='center',
                        )
        im = plt.imshow( result, interpolation = 'none' , cmap = 'Oranges' )
        # Here 14 is the number of queries
        plt.clim(0, maximum)
        cbar = plt.colorbar(im)
        cbar.set_ticks([0,maximum])
        cbar.set_ticklabels(["0", str(maximum)])
        # plt.show()
        # plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/plpos/'+str(queryy)+'xx.png')
    frame = pd.DataFrame(data_list, columns = ['Query', 'feb_07_1pm','feb_07_8pm','feb_08_1pm','feb_08_8pm','feb_09_1pm','feb_09_8pm','feb_10_1pm','feb_10_8pm','feb_11_1pm','feb_11_8pm','feb_12_1pm','feb_12_8pm','feb_13_1pm','feb_13_8pm','feb_14_1pm','feb_14_8pm','feb_15_1pm','feb_15_8pm','feb_16_1pm','feb_16_8pm'])
    name = q.split('_')[0] + 'PLs.csv'
    frame.to_csv(dest+name)

if __name__ == '__main__':
    dirs = directories(path)
    list_of_names = []
    query = []
    sp = 'C:/Users/yashwanth/Desktop/DATA/feb_08_1pm/horizontal/'
    for q in os.listdir(sp) : 
        query.append(q)
    for dir in dirs : 
        p = path + str(dir) + '/horizontal/'
        for q in query : 
            ps = p + q 
            list_of_names.append(ps)
        heat_generator(list_of_names,'Pvt','horizontal')
        break



print('............................................................')