import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#   generates boxplots of difference in page difference of advertised product and its organic appearance squared, query wise and category wise  #


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
    jqp = {}
    jcp = {}
    jqo = {}
    jco = {}
    for dir in dirs : 
        dir_path = p + dir + '/'
        for things in os.listdir(dir_path) : 
            if things == 'vertical' or things == 'horizontal':
                for file in os.listdir(dir_path+things+'/') :
                    # print(dir_path+things+'/'+file)
                    query = file.split('_')[0]
                    category = file.split('_')[1]
                    if query not in jqp : 
                        jqp[query] = []
                        jqo[query] = []
                    if category not in jcp :
                        jcp[category] = []
                        jco[category] = []
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
                            try : 
                                if pt == 1 : 
                                    jqp[query].append((int(lst.index(did)/condition))**2)
                                    jcp[category].append((int(lst.index(did)/condition))**2)
                                else : 
                                    jqo[query].append((int(lst.index(did)/condition))**2)
                                    jco[category].append((int(lst.index(did)/condition))**2)
                            except : 
                                nothing = 1
                                # if pt == 1 : 
                                #     jqp[query].append(int(1000/condition))
                                #     jcp[category].append(int(1000/condition))
                                # else : 
                                #     jqo[query].append(int(1000/condition))
                                #     jco[category].append(int(1000/condition))

    for cat in jcp.keys() : 
        print(cat)
        fig = plt.figure(figsize =(10, 7))
        plt.boxplot([jcp[cat],jco[cat]],showfliers=False)
        plt.xticks([1,2],['PL','TP'])
        plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/pics/cat/'+str(cat)+'.png')
        # plt.show()
    for q in jqp.keys() :
        print(q)
        fig = plt.figure(figsize =(10, 7))
        plt.boxplot([jqp[q],jqo[q]],showfliers=False)
        plt.xticks([1,2],['PL','TP'])
        plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/pics/q/'+str(q)+'.png')
        # plt.show()


                
