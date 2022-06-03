import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
#list_of_names = ['C:/Users/Nikita/Amazon_Baby wipes.csv','C:/Users/Nikita/Amazon_backpack.csv','C:/Users/Nikita/Amazon_bean bags.csv','C:/Users/Nikita/Amazon_bedsheet.csv','C:/Users/Nikita/Amazon_belt.csv','C:/Users/Nikita/Amazon_blanket.csv','C:/Users/Nikita/Amazon_desk.csv','C:/Users/Nikita/Amazon_detergent.csv','C:/Users/Nikita/Amazon_Dumbbells and weights.csv','C:/Users/Nikita/Amazon_Hand soap.csv','C:/Users/Nikita/Amazon_Jackets.csv','C:/Users/Nikita/Amazon_Luggage.csv','C:/Users/Nikita/Amazon_Mask.csv','C:/Users/Nikita/Amazon_Mattresses.csv']
list_of_names = []
path = 'C:/Users/yashwanth/Desktop/vertical'
for files in os.listdir(path) :
  f = path +'/' + str(files)
  list_of_names.append(f)
# Result is the no. of rows and cols in the first page
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
         ]

for j in range(len(list_of_names)):
    print(list_of_names[j])
    df = pd.read_csv(list_of_names[j])
   
    # here I have added the PL column to dataset
    df['PL'] = 0
   
    for ind in df.index:
        print(df['Ad'][ind])
        x = df['Ad'][ind]
        if x==1:
            df['PL'][ind] = 1
        else:
            df['PL'][ind] = 0
           
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
        print(i,col)
        data.append(col)

    print(data)
   
    for i in range(len(data)):
        for j in range(len(data[0])):
            result[i][j] += data[i][j]

print(result)
a = np.array(result)

for y in range(len(result)):
    for x in range(len(result[0])):
        plt.text(x, y, '%.0f' % result[y][x],
                 horizontalalignment='center',
                 verticalalignment='center',
                 )
im = plt.imshow( result, interpolation = 'none' , cmap = 'Reds' )
# Here 14 is the number of queries
plt.clim(0, 14)
cbar = plt.colorbar(im)
cbar.set_ticks([0, 14])
cbar.set_ticklabels(["0", "14"])
plt.show()