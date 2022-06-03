import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 
# This code generates heatmap at positions where repetitions were observed and also generates csv for the temporal repetition count. 
# 

path = 'C:/Users/yashwanth/Desktop/DATA/feb_07_1pm/horizontal/beds_Furniture_data.csv'
p = 'C:/Users/yashwanth/Desktop/DATA/'
common =['backpacks','Battery','bean bags' ,'Bedsheet','belt','blanket','camera' ,'coffee mugs','dumbells and weights' ,'jackets' ,'jeans' ,'kettle' ,'masks','matresses','pans','pillows' ,'shoe rack','socks','sports gloves','sports shoes','sweaters','trimmer','tv','wall clock','wallet','washing machines','water bottles','yoga mat']

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

def heat_generator(data,flag,nam) :
    maximum = 0
    tots = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            maximum = max(maximum,data[i][j])
            tots += data[i][j]
    a = np.array(data)

    
    if flag ==1 :
        fig, ax = plt.subplots(figsize=(10,10))
        # For 4 cols and 15 rows
        ax.set_xticks(np.arange(4))
        ax.set_yticks(np.arange(10))

        ax.set_xticklabels([1,2,3,4])
        ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10])
    elif flag == 0 :
        fig, ax = plt.subplots(figsize=(15,15))
        # For 4 cols and 15 rows
        ax.set_xticks(np.arange(1))
        ax.set_yticks(np.arange(24))

        ax.set_xticklabels([1])
        ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    
    for y in range(len(data)):
        for x in range(len(data[0])):
            plt.text(x, y, '%.2f' % data[y][x],
                    horizontalalignment='center',
                    verticalalignment='center',
                    )
        # plt.xticks(np.arange(1))
            #plt.yticks(np.arange(0, 23, 2))
    im = plt.imshow( data, interpolation = 'none' , cmap = 'Oranges' )
    # Here 14 is the number of queries
    # maximum = 81
    plt.clim(0, maximum)
    cbar = plt.colorbar(im)
    cbar.set_ticks([0,maximum])
    cbar.set_ticklabels(["0", str(maximum)])
    plt.savefig('C:/Users/yashwanth/Desktop/OLD_DATA/repeat/'+str(nam)+'_'+str(tots)+'.png')
    # plt.show()


if __name__ == '__main__':
    data_list = []
    dirs = directories(p)
    jqp = {}
    jcp = {}
    jqo = {}
    jco = {}
    hsum = 0
    vsum = 0
    hsumc = 0
    vsumc = 0
    com_count = 0
    horizontal = [[0,0,0,0],
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
    horizontal_common = [[0,0,0,0],
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
    vertical = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    vertical_common = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    for dir in dirs : 
        dir_path = p + dir + '/'
        for things in os.listdir(dir_path) : 
            if things == 'vertical' or things == 'horizontal':
                for file in os.listdir(dir_path+things+'/') :
                    # print(dir_path+things+'/'+file)
                    element_list = []
                    query = file.split('_')[0]
                    category = file.split('_')[1]
                    plst = {}
                    fo = {}
                    dates = {}
                    col = {}
                    print(query)
                    date = 0
                    for D in dirs : 
                        dl = []
                        date += 1 
                        dirPath = p + D + '/'
                        upath = dirPath + things + '/' + file
                        # print(upath)
                        df = pd.read_csv(upath)
                        if things == 'horizontal' :
                            condition = 40
                        else : 
                            condition = 24
                        for ind in df.index : 
                            x = df['Ad'][ind]
                            did = df['Data-id'][ind]
                            if ind < 3*condition and x == 1 and df['Pvt'][ind] == 1:
                                dl.append(did)
                        # print(len(dl))
                        dl = set(dl)
                        # print(len(dl))
                        for did in dl : 
                            if did not in plst.keys() :
                                plst[did] = []
                                dates[did] = []
                                fo[did] = []
                            lst = []
                            fo_flag = 1
                            for indx in df.index : 
                                dids = df['Data-id'][indx]
                                ads = df['Ad'][indx]
                                if dids == did and ads == 1 : 
                                    if fo_flag == 1 : 
                                        fo[did].append(indx+1)
                                        fo_flag = 0
                                    lst.append(indx)
                            if did not in col.keys():
                                if condition == 40 : 
                                    col[did] = [[0,0,0,0],
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
                                elif condition == 24 :
                                    col[did] = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
                            if  len(lst) > 1 :
                                for i in lst : 
                                    if condition == 40 :
                                        col[did][int(int(i%40)/4)][int(int(i%40)%4)] += 1
                                    elif condition == 24 : 
                                        col[did][int(int(i%24))][0] += 1
                                # print(col)
                                plst[did].append(len(lst))
                                dates[did].append(date)
                    if query in common :
                        # com_count += 1
                        # print("common-",query)
                        for dd in col.keys() :
                            if things == 'horizontal' :
                                for i in range(len(col[dd])):
                                    for j in range(len(col[dd][0])):
                                        horizontal_common[i][j] += col[dd][i][j]
                            if things == 'vertical' :
                                # print(col[dd])
                                for i in range(len(col[dd])):
                                    for j in range(len(col[dd][0])):
                                        vertical_common[i][j] += col[dd][i][j]
                    for dd in col.keys() :
                        # nam = query + '_' + str(dd)
                        # heat_generator(col[dd],int(condition/40),nam)
                        if things == 'horizontal' :
                            for i in range(len(col[dd])):
                                for j in range(len(col[dd][0])):
                                    horizontal[i][j] += col[dd][i][j]
                        if things == 'vertical' :
                            # print(col[dd])
                            for i in range(len(col[dd])):
                                for j in range(len(col[dd][0])):
                                    vertical[i][j] += col[dd][i][j]
                    element_list.append(query) 
                    flag = 1
                    for item in plst.keys() : 
                        if flag == 1 :
                            flag = 0
                        else : 
                            element_list = []
                            element_list.append("")
                        element_list.append(item)
                        dc = 0
                        dt = dates[item]
                        for i in range(20) :
                            if dc < len(dt) : 
                                if dt[dc] == i+1 : 
                                    # element_list.append(str(plst[item][dc])+',('+str(fo[item][dc])+')')
                                    element_list.append(str(plst[item][dc]))
                                    dc += 1
                                else : 
                                    element_list.append("")
                            else : 
                                element_list.append("")
                        data_list.append(element_list)       
        break

    for i in range(len(horizontal)):
        for j in range(len(horizontal[0])):
            hsum += horizontal[i][j]
    for i in range(len(horizontal)):
        for j in range(len(horizontal[0])):
            horizontal[i][j] = (horizontal[i][j]/hsum )*100
    print('hsum = ',hsum)
    heat_generator(horizontal,1,'grid_modified')
    for i in range(len(vertical)):
        for j in range(len(vertical[0])):
            vsum += vertical[i][j]
    # print(vertical)
    for i in range(len(vertical)):
        for j in range(len(vertical[0])):
            vertical[i][j] = (vertical[i][j]/vsum )*100
    print('vsum = ',vsum)
    heat_generator(vertical,0,'line_modified')
    ############
    for i in range(len(horizontal_common)):
        for j in range(len(horizontal_common[0])):
            hsumc += horizontal_common[i][j]
    for i in range(len(horizontal_common)):
        for j in range(len(horizontal_common[0])):
            horizontal_common[i][j] = (horizontal_common[i][j]/hsumc )*100
    print('hsumc = ',hsumc)
    heat_generator(horizontal_common,1,'grid_common')
    for i in range(len(vertical_common)):
        for j in range(len(vertical_common[0])):
            vsumc += vertical_common[i][j]
    # print(vertical)
    for i in range(len(vertical_common)):
        for j in range(len(vertical_common[0])):
            vertical_common[i][j] = (vertical_common[i][j]/vsumc )*100
    print('vsumc = ',vsumc)
    heat_generator(vertical_common,0,'line_common')

    frame = pd.DataFrame(data_list, columns = ['query','Data_id','feb_07_1pm','feb_07_8pm','feb_08_1pm','feb_08_8pm','feb_09_1pm','feb_09_8pm','feb_10_1pm','feb_10_8pm','feb_11_1pm','feb_11_8pm','feb_12_1pm','feb_12_8pm','feb_13_1pm','feb_13_8pm','feb_14_1pm','feb_14_8pm','feb_15_1pm','feb_15_8pm','feb_16_1pm','feb_16_8pm'])
    frame.to_csv('repeatition_ads_pvt_modified.csv')



                
