import csv
from multiprocessing.sharedctypes import Value
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
from random import random
import matplotlib.pyplot as plt 
import requests

# 
# This script generates the probability distribution (dumped into csvs) and CSVs for all three product patterns. 
# 

path = 'C:/Users/yashwanth/Desktop/DATA/'
query = ['backpacks_clothesAndApparell_data','jeans_clothesAndApparell_data','water bottles_Kitchen_data','wall clock_homeDecor_data','yoga mat_Sports_data']
dest = 'C:/Users/yashwanth/Desktop/OLD_DATA/'

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

def psort(lst) : 
    l = {}
    for k in lst : 
        for did in lst[k] : 
            if did not in l : 
                l[did] = lst[k][did]
            else : 
                l[did] = max(l[did],lst[k][did])
    sl = sorted(l.items(), key = lambda kv:(kv[1], kv[0]))
    return(sl)

def Random(pvt,pp,t) : 
    i = 0
    a = 0
    b = 0
    lst = []
    while(i<40) : 
        value = random()
        # print(value)
        if value > 0.75 and a < t:
            # print('a : ',a) 
            lst.append(pvt[a])
            a += 1
        elif b < 40-t: 
            # print('b : ',b)
            lst.append(pp[b])
            b += 1
        else : 
            lst.append(pvt[a])
            a += 1
        i += 1
    return lst

def zigzag(pvt,pp,t) : 
    i = 0
    a = 0
    b = 0
    lst = []
    if t == 5 : 
        plranks = [1,4,14,21,24]
    else : 
        plranks = [1,4,14,21,24,34]
    while(i<40) :
        if i+1 in plranks : 
            lst.append(pvt[a])
            a += 1
        else : 
            lst.append(pp[b])
            b += 1
        i += 1 
    return lst    
    
def gen_csv(final,pattern,data) : 
    data_list_fo = [] 
    i = 0
    for did in final :
        element_list_fo = [] 
        element_list_fo.append(i+1)
        i+=1
        for ind in data[did].index : 
            element_list_fo.append(data[did][ind])
        data_list_fo.append(element_list_fo)
    frame = pd.DataFrame(data_list_fo, columns = ['Rank','','o_Rank', 'Data-id', 'Ad', 'Link', 'Brand', 'price', 'Discount', 'F-assured', 'Title','Description', 'Rating','#Ratings','#Reviews','Spotlight','Pvt'])
    name = q.split('_')[0] + '_'+pattern+'_pattern.csv'
    frame.to_csv(dest+name)

if __name__ == '__main__':
    dirs = directories(path)
    lst = {}
    alst = {}
    plst = {}
    data = {}
    for dir in dirs : 
        print(dir)
        p = path + str(dir) + '/horizontal/'
        for q in query : 
            if q not in lst : 
                plst[q] = []
            if q not in lst : 
                lst[q] = {}
            if q not in alst : 
                alst[q] = {}
            ps = p + q + '.csv'
            df = pd.read_csv(ps)
            for i in df.index : 
                did = df['Data-id'][i]
                ad = df['Ad'][i]
                if i < 360 : 
                    if i not in lst[q] : 
                        alst[q][i] = {}
                    if did not in alst[q][i] : 
                        alst[q][i][did] = 0
                    alst[q][i][did] += 1
                    data[did] = df.iloc[i]   
                if i < 40 : 
                    if df['Pvt'][i] == 1 :
                        plst[q].append(did)
                    if i not in lst[q] : 
                        lst[q][i] = {}
                    if did not in lst[q][i] : 
                        lst[q][i][did] = 0
                    lst[q][i][did] += 1
                    data[did] = df.iloc[i]
    for q in query : 
        print('.....................................')
        print(q)
        print('all pls in SERP : ',len(set(plst[q])))
        data_list = []
        pls = 0
        target = 6
        final = []
        sl = psort(lst[q])
        asl = psort(alst[q])
        for i in lst[q] : 
            element_list = []
            # print(i)
            for did in lst[q][i] : 
                lst[q][i][did] /= 20
            # print(lst[q][i])
            element_list.append(i+1)
            element_list.append(lst[q][i])
            dids = []
            pbb = []
            for k in lst[q][i] : 
                dids.append(k)
                pbb.append(lst[q][i][k])
            if max(pbb) > 0.5 : 
                val = dids[pbb.index(max(pbb))]
            else :
                val = np.random.choice(dids,p = pbb)
                while val in final or val == 'BOTF4ZRGYEE9PNRG' or val == 'BOTFU4YKDTAW6BPU': 
                    val = np.random.choice(dids,p = pbb)
            if data[val]['Pvt'] == 1 : 
                pls += 1
                print('\t \t Pl occurence : ',i)
            # print(val)
            final.append(val)
            data_list.append(element_list)
        # print('initially pls : ',pls)
        # print(final)
        elements = []
        for element in asl : 
            elements.append(element[0])
        # print(elements)
        i = 39 - target + pls + 1
        j = len(asl)-1
        finals = 0
        # print('Set : ',len(set(final)))
        while (j>=0) :
            if asl[j][0] in final : 
                finals += 1
            j = j-1
        if q == 'backpacks_clothesAndApparell_data' or q == 'yoga mat_Sports_data' or q == 'wall clock_homeDecor_data' :
            j = len(asl)-1
        else : 
            j = len(sl) - 1
        while(i<40) :
            while(j>=0) :
                if q == 'backpacks_clothesAndApparell_data' or q == 'yoga mat_Sports_data' or q == 'wall clock_homeDecor_data' : 
                    if asl[j][0] not in final : 
                        if data[asl[j][0]]['Pvt'] == 1 : 
                            final[i] = asl[j][0]
                            j = j-1
                            break
                else : 
                    if sl[j][0] not in final : 
                        if data[sl[j][0]]['Pvt'] == 1 : 
                            final[i] = sl[j][0]
                            j = j-1
                            break
                j = j-1
            i+=1   
        print('Set : ',len(set(final)),'\t finalists : ',finals)
        plsa = 0
        indi = 0
        final_pvt = []
        final_pp = []
        # print('original : ')
        # print(final)
        print('\t In original pattern --->')
        for dids in final : 
            indi += 1
            if data[dids]['Pvt']==1 : 
                plsa += 1
                print('\t \t PL appearance : ',indi)
                final_pvt.append(dids)
            else : 
                final_pp.append(dids)
        r_list = Random(final_pvt,final_pp,plsa)
        z_list = zigzag(final_pvt,final_pp,plsa)
        # print("random : ")
        # print(r_list)
        indi = 0
        print('\t random pattern --->')
        for dids in r_list : 
            indi += 1
            if data[dids]['Pvt']==1 : 
                print('\t \t PL appearance : ',indi)
        indi = 0
        print('\t zigzag pattern --->')
        for dids in z_list : 
            indi += 1
            if data[dids]['Pvt']==1 : 
                print('\t \t PL appearance : ',indi)
        print('initially pls : ',pls,'\t Now,PLs : ',plsa)
        gen_csv(final,'original',data)
        gen_csv(r_list,'random',data)
        gen_csv(z_list,'zigzag',data)

        frame = pd.DataFrame(data_list, columns = ['Rank', 'Distribution'])
        name = q.split('_')[0] + '_distribution.csv'
        frame.to_csv(dest+name)

		
            

    



