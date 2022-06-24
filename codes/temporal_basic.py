import csv
import pandas as pd
import time
import os
import parsers
import midend
 
	
#     This code generates the basic statistics like organic PL, advertised PL, organic TP, advertised TP across snapshots category wise and overall    #
	
path = 'C:/Users/yashwanth/Desktop/DATA/'

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs

def means(lst) :
    return sum(lst)/len(lst)

def sd(lst) : 
    mean = means(lst)
    variance = sum([((x - mean) ** 2) for x in lst])/len(lst)
    res = variance ** 0.5
    return res

if __name__ == '__main__':
    dirs = directories(path) 
    print(dirs)
    cat_ads_serp = {}
    cat_organic_serp = {}
    cat_pvt_serp = {}
    cat_orgad_serp = {}
    for dir in dirs : 
        dir_path = path + dir + '/'
        print(dir_path)
        # if int(dir.split('_')[1]) < 12 :
        # now run the parser for all the files 
        parsers.parse(dir_path)
        # midend.parse(dir_path)
        # print('done')
    # for dir in dirs :  
    #     dir_path = path + dir + '/'
        with open(dir_path+'analysis_3_f.txt','r') as f :
            count = 1
            for line in f : 
                if count == 0:
                    count += 1
                    continue 
                if count == 1 :
                    category = line.split(' ')[1] 
                    if category == 'Fraction' :
                        category = 'overAll'
                        count = 2
                    if category not in cat_pvt_serp :
                        cat_pvt_serp[category] = []
                    if category not in cat_ads_serp :
                        cat_ads_serp[category] = []
                    if category not in cat_organic_serp :
                        cat_organic_serp[category] = []
                    if category not in cat_orgad_serp :
                        cat_orgad_serp[category] = []
                if count == 2 :
                    cat_pvt_serp[category].append(float(line.split(' ')[-1]))
                if count == 3 :
                    try : 
                        cat_ads_serp[category].append(float(line.split(' ')[-1]))
                    except : 
                        count = 3
                if count == 4 :
                    cat_organic_serp[category].append(float(line.split(' ')[-1]))
                count += 1
                if count == 6 :
                    try : 
                        cat_orgad_serp[category].append(float(line.split(' ')[-1]))
                        count = 0
                    except : 
                        count = 0
    print('done with it')
    with open('C:/Users/yashwanth/Desktop/btp/scripts/first_pages_temporal_analysis.txt','a') as f :
        for cat in cat_pvt_serp.keys() :
            # if cat == 'Fraction' :
            #     break
            line = "In " + cat + " : \n"
            f.write(line)
            line = 'mean percentage of pvt in total : ' + "{:.2f}".format(means(cat_pvt_serp[cat])) + ', S.D : ' + "{:.2f}".format(sd(cat_pvt_serp[cat])) + '\n'
            f.write(line)
            line = 'mean percentage of pvt in ads : ' + "{:.2f}".format(means(cat_ads_serp[cat])) + ', S.D : ' + "{:.2f}".format(sd(cat_ads_serp[cat])) + '\n'
            f.write(line)
            line = 'mean percentage of pvt in organic : ' + "{:.2f}".format(means(cat_organic_serp[cat])) + ', S.D : ' + "{:.2f}".format(sd(cat_organic_serp[cat])) + '\n'
            f.write(line)
            line = 'mean percentage of ads in pvt : ' + "{:.2f}".format(means(cat_orgad_serp[cat])) + ', S.D : ' + "{:.2f}".format(sd(cat_orgad_serp[cat])) + '\n'
            f.write(line)
            line = 'mean percentage of organic in ads : ' + "{:.2f}".format(100-means(cat_orgad_serp[cat])) + ', S.D : ' + "{:.2f}".format(sd(cat_orgad_serp[cat])) + '\n' + '\n'
            f.write(line)


                    
                    

            
