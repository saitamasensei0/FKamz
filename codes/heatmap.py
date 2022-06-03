import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = 'C:/Users/yashwanth/Desktop/DATA/feb_07_1pm'

# 
# This code generates heatmaps for horizontal/vertical alignments for positions of Ads and PLs.
# 

def heat_generator(result,list_of_names,label,flag) :
    for j in range(len(list_of_names)):
        print(list_of_names[j])
        df = pd.read_csv(list_of_names[j])
    
        # here I have added the PL column to dataset
        df['PL'] = 0
    
        for ind in df.index:
            x = df[label][ind]
            if x==1:
                df['PL'][ind] = 1
            else:
                df['PL'][ind] = 0
            
        i=0
        data = []
        # here 60 is the number of products in the first page
        if flag ==1 : 
            while i < 40:
                col = []
                col.append(int(int((df['PL'][i]))))
                col.append(int(int((df['PL'][i+1]))))
                col.append(int(int((df['PL'][i+2]))))
                col.append(int(int((df['PL'][i+3]))))
                #Here 4 is the number of columns in each row
                i+=4
                print(i,col)
                data.append(col)
        elif flag ==0 :
            while i < 24:
                col = []
                col.append(int(int((df['PL'][i]))))
                #Here 1 is the number of columns in each row
                i+=1
                print(i,col)
                data.append(col)

        print(data)
        maximum = 0
        for i in range(len(data)):
            for j in range(len(data[0])):
                result[i][j] += data[i][j]
                maximum = max(maximum,result[i][j])

    print(result)
    a = np.array(result)

    fig, ax = plt.subplots(figsize=(10,10))
    if flag ==1 :
        # For 4 cols and 15 rows
        ax.set_xticks(np.arange(4))
        ax.set_yticks(np.arange(10))

        ax.set_xticklabels([1,2,3,4])
        ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10])
    elif flag == 0 :
        # For 4 cols and 15 rows
        ax.set_xticks(np.arange(1))
        ax.set_yticks(np.arange(24))

        ax.set_xticklabels([1])
        ax.set_yticklabels([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
    
    for y in range(len(result)):
        for x in range(len(result[0])):
            plt.text(x, y, '%.0f' % result[y][x],
                    horizontalalignment='center',
                    verticalalignment='center',
                    )
        # plt.xticks(np.arange(1))
            #plt.yticks(np.arange(0, 23, 2))
    im = plt.imshow( result, interpolation = 'none' , cmap = 'Oranges' )
    # Here 14 is the number of queries
    # maximum = 81
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
                if files.split('_')[1] == 'homeDecor' :
                    list_of_names.append(f)
            if dirs == 'horizontal' :
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
                heat_generator(result,list_of_names,'Pvt',1)
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
                heat_generator(result,list_of_names,'Ad',1)
                print(len(list_of_names))    
            elif dirs == 'vertical' :
                result = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
                heat_generator(result,list_of_names,'Pvt',0)
                result = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
                heat_generator(result,list_of_names,'Ad',0)
            print(len(list_of_names))
