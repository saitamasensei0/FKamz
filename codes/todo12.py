import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

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
            if things == 'horizontal' or things == 'vertical':
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
                                    jqp[query].append((lst.index(did) + 1-ind)**2)
                                    jcp[category].append((lst.index(did) + 1-ind)**2)
                                else : 
                                    jqo[query].append((lst.index(did) + 1-ind)**2)
                                    jco[category].append((lst.index(did) + 1-ind)**2)
                            except : 
                                nothing = 1
                                # if pt == 1 : 
                                #     jqp[query].append((1001-ind)**2)
                                #     jcp[category].append((1001-ind)**2)
                                # else : 
                                #     jqo[query].append((1001-ind)**2)
                                #     jco[category].append((1001-ind)**2)
    pvtc = 0
    pvtq = []
    orgc = 0
    orgq = []
    data_list = []
    element_list = []
    for cat in jcp.keys() : 
        element_list = []
        element_list.append(cat)
        print(cat)
        fig = plt.figure(figsize =(10, 7))
        bp = plt.boxplot([jcp[cat],jco[cat]],showfliers=False)
        value,pvalue = scipy.stats.ttest_ind(jcp[cat],jco[cat])
        element_list.append(value)
        element_list.append(pvalue)
        data_list.append(element_list)
        plt.xticks([1,2],['PL','TP'])
        plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/sq/cat/'+str(cat)+'.png')
        # plt.show()
    for q in jqp.keys() :
        print(q)
        element_list = []
        element_list.append(q)
        fig = plt.figure(figsize =(10, 7))
        bp = plt.boxplot([jqp[q],jqo[q]],showfliers=False)
        value,pvalue = scipy.stats.ttest_ind(jqp[q],jqo[q])
        element_list.append(value)
        element_list.append(pvalue)
        data_list.append(element_list)
        medians = [item.get_ydata()[0] for item in bp['medians']]
        print(medians)
        if medians[0] > medians[1] :
            pvtc += 1
            pvtq.append(q)
        elif medians[0] < medians[1] : 
            orgc += 1
            orgq.append(q)
        plt.xticks([1,2],['PL','TP'])
        plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/sq/q/'+str(q)+'.png')
        # plt.show()
    print("pvt > org : ",pvtc)
    for q in pvtq : 
        print(q)
    print("pvt < org : ",orgc)
    for q in orgq : 
        print(q)
    frame = pd.DataFrame(data_list, columns = ['Name','Value','pvalue'])
    frame.to_csv('stt.csv')

                