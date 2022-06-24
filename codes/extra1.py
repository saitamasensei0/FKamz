import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

path = 'C:/Users/yashwanth/Desktop/DATA/feb_07_1pm/horizontal/beds_Furniture_data.csv'
p = 'C:/Users/yashwanth/Desktop/DATA/'
def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

if __name__ == '__main__':
    dirs = directories(p)
    qp = {} # has counts of organic in this list
    pvts = {}
    for dir in dirs : 
        dir_path = p + dir + '/'
        for things in os.listdir(dir_path) : 
            if things == 'horizontal' or things == 'vertical':
                jqp = {}  # has the jumps 
                print(dir)
                for file in os.listdir(dir_path+things+'/') :
                    # print(dir_path+things+'/'+file)
                    query = file.split('_')[0]
                    category = file.split('_')[1]
                    if query not in qp : 
                        qp[query] = []
                    if query not in pvts : 
                        pvts[query] = []
                    jqp[query] = []
                    df = pd.read_csv(dir_path+things+'/'+file)
                    lst = []
                    if things == 'horizontal' :
                        condition = 40
                    else : 
                        condition = 24
                    for ind in df.index : 
                        x = df['Ad'][ind]
                        did = df['Data-id'][ind]
                        if x == 0 :
                            lst.append(did)
                    for ind in df.index : 
                        x = df['Ad'][ind]
                        did = df['Data-id'][ind]
                        pt = df['Pvt'][ind]
                        if x == 1 and ind < condition: 
                            if pt ==1 : 
                                pvts[query].append(did)
                            try : 
                                if pt == 1 : 
                                    jqp[query].append(lst.index(did) + 1)
                            except : 
                                nothing = 1
                                # if pt == 1 : 
                                #     jqp[query].append(1001)
                                #     qrp.append(ind+1)
                                # else : 
                                #     jqo[query].append(1001)
                                #     qro.append(ind+1)
                    qp[query].append(len(jqp[query]))  
    print(len(qp))
    print(len(qp[query]))          
    data_list = []
    for q in qp.keys() : 
        element_list = []
        element_list.append(q)
        for v in qp[q] :
            element_list.append(v)
        data_list.append(element_list)
    frame = pd.DataFrame(data_list, columns = ['query','feb_07_1pm','feb_07_8pm','feb_08_1pm','feb_08_8pm','feb_09_1pm','feb_09_8pm','feb_10_1pm','feb_10_8pm','feb_11_1pm','feb_11_8pm','feb_12_1pm','feb_12_8pm','feb_13_1pm','feb_13_8pm','feb_14_1pm','feb_14_8pm','feb_15_1pm','feb_15_8pm','feb_16_1pm','feb_16_8pm'])
    frame.to_csv('organic_in_ads.csv')
    print(pvts)
                    

 