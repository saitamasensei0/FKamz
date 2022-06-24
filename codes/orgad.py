from ctypes import sizeof
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/yashwanth/Desktop/DATA/feb_07_1pm/'
p = 'C:/Users/yashwanth/Desktop/DATA/'
figpath = 'C:/Users/yashwanth/Desktop/DATA/orgad_snaps/'

#         This code generates heatmaps for organic positions of advertised products acrosss snapshots             #


def heat_generator(list_of_names,label,flag) :
    for j in range(len(list_of_names)):
        # print(list_of_names[j])
        query = ((list_of_names[j].split('/')[-1]).split('.')[0]).split('_')[0]
        print(query)
        if flag == 'horizontal' :
            condition = 40
            ad_lst = [0,1,3,7,11,15,19,23,27,31,35,39]
        else : 
            condition = 24
            ad_lst = [0,1,7,11,15,19,23]
        dirs = ['feb_07_1pm','feb_07_8pm','feb_08_1pm','feb_08_8pm','feb_09_1pm','feb_09_8pm','feb_10_1pm','feb_10_8pm','feb_11_1pm','feb_11_8pm']
        rank = {}
        for dir in dirs :
            file = p+dir+'/'+flag + '/'+ list_of_names[j].split('/')[-1]
            df = pd.read_csv(file)
            lst = []
            for ind in df.index :
                did = df['Data-id'][ind]
                if df[label][ind] == 0 :
                    lst.append(did)
            for ind in df.index :
                x = df[label][ind]
                did = df['Data-id'][ind]
                if ind in ad_lst :
                    if ind not in rank :
                        rank[ind] = []
                    if x == 0 :
                        rank[ind].append(0)
                    else :
                        try :
                            rank[ind].append(lst.index(did) + 1)
                        except :
                            rank[ind].append(1001)
            # print(dir)
            # print(rank)
        # print(rank)
        x_len = len(rank.keys())
        lt = []
        for k in rank.keys() :
            lt.append(k)
        y_len = len(rank[0])
        result = [ [ 0 for i in range(y_len) ] for j in range(x_len) ]
        for i in range(x_len):
            for j in range(y_len):
                result[i][j] = rank[lt[i]][j]
        # print(result)


        fig, ax = plt.subplots(figsize=(40,40))
        if flag =='horizontal' :
            # For 4 cols and 15 rows
            ax.set_xticks(np.arange(10))
            ax.set_yticks(np.arange(12))

            ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10])
            ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12])
        elif flag == 'vertical' :
            # For 4 cols and 15 rows
            ax.set_xticks(np.arange(10))
            ax.set_yticks(np.arange(24))

            ax.set_xticklabels([1,2,3,4,5,6,7,8,9,10])
            ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
        for y in range(len(result)):
            for x in range(len(result[0])):
                if result[y][x] == 1001:
                    plt.text(x, y, 'NA',
                            horizontalalignment='center',
                            verticalalignment='center',
                            )
                else :
                    plt.text(x, y, '%.0f' % result[y][x],
                        horizontalalignment='center',
                        verticalalignment='center',
                        )
            # plt.xticks(np.arange(1))
                #plt.yticks(np.arange(0, 23, 2))
        im = plt.imshow( result, interpolation = 'none' , cmap = 'Oranges' )
        # Here 14 is the number of queries
        maximum = 1001
        plt.clim(0, maximum)
        cbar = plt.colorbar(im)
        cbar.set_ticks([0,maximum])
        cbar.set_ticklabels(["0", str(maximum)])
        plt.show()


if __name__ == '__main__':
    for dirs in os.listdir(path) :
        # print(dirs)
        d = path +'/' + str(dirs)
        list_of_names = []
        if os.path.isdir(d) :
            for files in os.listdir(d) :
                # print(files)
                f = d +'/' + str(files)
                list_of_names.append(f)
        if dirs == 'vertical' :
            heat_generator(list_of_names,'Ad',dirs)
 
