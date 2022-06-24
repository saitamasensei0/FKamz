import csv
import pandas as pd
import time
import os

path = 'C:/Users/yashwanth/Desktop/DATA/feb_07_1pm/'

def directories(dir_path) : 
	dirs = []
	for things in os.listdir(dir_path) : 
		thing_path = dir_path + things
		if os.path.isdir(thing_path):
			dirs.append(things)
	return dirs



def parse(path) :
    dirs = directories(path)
    final_list = [[],[],[]]
    cat_ads = {}   # category wise ad count
    cat_organic = {}   # category wise orgainc pvt label product count
    cat_total = {}   # category wise pvt label product count
    cat_ads_serp = {}   # category wise advertised pvt label product count
    cat_queries = {}   # category wise product count
    for dir in dirs : 
        if dir == 'horizontal' : 
            condition = 40
        else : 
            condition = 24
        for file in os.listdir(path + dir + '/') :
            filepath = path + dir + '/' + file
            df = pd.read_csv(filepath)
            query = file.split('_')[0]
            category = file.split('_')[1]
            data_list = [[],[],[]]
            ads_serp = [0,0,0]
            only_ad_serp = [0,0,0]
            organic_serp = [0,0,0]
            total = 0
            o = [0,0,0]
            # ads_serp = 0   # number of ads on serp
            # only_ad_serp = 0   # number of advertised pvt label products on serp   
            # organic_serp = 0   # number of organic pvt label products on serp
            # total = 0   # number of pvt label products 
            brands = set()   # set of brands involved in this query
            t10 = 0   # number of pvt label products in top 10 of serp
            t5 = 0   # number of pvt label products in top 5 of serp
            serp = [0,0,0]   # number of pvt label products on serp
            flag = 1    # for first appearance of pvt label, 0 signifies observed
            rank = 2000    # rank of first observed initiated to number greater than 1000

            # initialising category wise counts
            if category not in cat_ads_serp :
                cat_ads_serp[category] = [0,0,0]
            if category not in cat_organic :
                cat_organic[category] = [0,0,0]
            if category not in cat_total :
                cat_total[category] = [0,0,0]
            if category not in cat_ads :
                cat_ads[category] = [0,0,0]
            if category not in cat_queries :
                cat_queries[category] = [0,0,0]

            for i in df.index :
                if df['Ad'][i] == 1 and i<condition :
                    ads_serp[0] += 1
                    if df['Pvt'][i] == 1 :
                        only_ad_serp[0] += 1
                if df['Ad'][i] == 1 and i<2*condition :
                    ads_serp[1] += 1
                    if df['Pvt'][i] == 1 :
                        only_ad_serp[1] += 1
                if df['Ad'][i] == 1 and i<3*condition :
                    ads_serp[2] += 1
                    if df['Pvt'][i] == 1 :
                        only_ad_serp[2] += 1
                if df['Ad'][i] == 0 and df['Pvt'][i] == 1 and i<condition:
                    organic_serp[0] += 1
                if df['Ad'][i] == 0 and df['Pvt'][i] == 1 and i<2*condition:
                    organic_serp[1] += 1
                if df['Ad'][i] == 0 and df['Pvt'][i] == 1 and i<3*condition:
                    organic_serp[2] += 1
                if df['Pvt'][i] == 1 :
                    total += 1
                    brands.add(df['Brand'][i].lower())
                    if i<10 :
                        t10 += 1
                    if i<5 :
                        t5 += 1
                    if i<condition :
                        serp[0] += 1
                    if i<2*condition :
                        serp[1] += 1
                    if i<3*condition :
                        serp[2] += 1
                    if flag :
                        rank = i+1
                        flag = 0
            for j in range(0,3) :
                o[j] = (j+1)*condition -ads_serp[j]    # number of organic search results on serp
                cat_ads[category][j] += ads_serp[j]
                cat_ads_serp[category][j] += only_ad_serp[j]
                cat_organic[category][j] += organic_serp[j]
                cat_total[category][j] += serp[j]
                cat_queries[category][j] += (j+1)*condition 
                # if total>0 :
                data_list[j].append(query)
                data_list[j].append(category)
                data_list[j].append(serp[j])
                data_list[j].append("{:.2f}".format((serp[j]/((j+1)*condition))*100) + '%')
                data_list[j].append(t10)
                data_list[j].append(t5)
                if rank<=1000 :
                    data_list[j].append(rank)
                else :
                    data_list[j].append('NA')
                data_list[j].append(total)
                data_list[j].append(len(brands))
                data_list[j].append(str(only_ad_serp[j])+' \ '+str(ads_serp[j]))
                if not ads_serp[j] == 0 : 
                    data_list[j].append("{:.2f}".format((only_ad_serp[j]/ads_serp[j])*100) + '%')
                else :
                    data_list[j].append("NA")
                data_list[j].append(str(organic_serp[j])+' \ '+str(o[j]))
                data_list[j].append("{:.2f}".format((organic_serp[j]/(o[j]))*100) + '%')
                if not only_ad_serp[j] + organic_serp[j] == 0 :
                    data_list[j].append("{:.2f}".format(only_ad_serp[j]/(only_ad_serp[j] + organic_serp[j])))
                else : 
                    data_list[j].append('NA')
                final_list[j].append(data_list[j])

    frame = pd.DataFrame(final_list[0],columns = ['Query','Category','Pvt label products in first SERP','percentage of Pvt label products in first SERP',' Products in top10','# Products in top5','Rank of first appearance','Total pvt label products','#pvt labels','Fraction of advertised Pvt label products','percentage','Fraction of organic Pvt label products','percentage','percentage in ads'])
    frame.to_csv(path + 'analysis_1_f.csv')
    frame = pd.DataFrame(final_list[1],columns = ['Query','Category','Pvt label products in first two SERP','percentage of Pvt label products in first two SERP',' Products in top10','# Products in top5','Rank of first appearance','Total pvt label products','#pvt labels','Fraction of advertised Pvt label products','percentage','Fraction of organic Pvt label products','percentage','percentage in ads'])
    frame.to_csv(path + 'analysis_2_f.csv')
    frame = pd.DataFrame(final_list[2],columns = ['Query','Category','Pvt label products in first three SERP','percentage of Pvt label products in first three SERP',' Products in top10','# Products in top5','Rank of first appearance','Total pvt label products','#pvt labels','Fraction of advertised Pvt label products','percentage','Fraction of organic Pvt label products','percentage','percentage in ads'])
    frame.to_csv(path + 'analysis_3_f.csv')

    overAll_ads = [0,0,0]   # overall ad count
    overAll_organic = [0,0,0]   # overall organic pvt label product count count
    overAll_serp = [0,0,0]   # overall pvt label product count
    overAll_queries = [0,0,0]   # overall product count
    overAll_ads_serp = [0,0,0]   # overall advertised pvt label product count

    for i in cat_organic.keys() :
        for j in range(0,3) : 
            overAll_ads[j] += cat_ads[i][j]
            overAll_organic[j] += cat_organic[i][j]
            overAll_queries[j] += cat_queries[i][j]
            overAll_serp[j] += cat_total[i][j]
            overAll_ads_serp[j] += cat_ads_serp[i][j]
    for j in range(0,3) :
        with open(path + 'analysis_' + str(j+1) + '_f.txt','a') as f :
            for i in cat_organic.keys() :
                line = 'In ' + i + ' : ' + '\n'
                f.write(line)
                line = 'Fraction of pvt label products - ' + str(cat_total[i][j]) +'/' +str(cat_queries[i][j]) + '       Percentage : ' + "{:.2f}".format((cat_total[i][j]/cat_queries[i][j])*100) + '\n' 
                f.write(line)
                line =  'Fraction of advertised pvt label products - ' + str(cat_ads_serp[i][j])+'/'+str(cat_ads[i][j]) + '       Percentage : ' + "{:.2f}".format((cat_ads_serp[i][j]/cat_ads[i][j])*100) + '\n'
                f.write(line)
                line =  'Fraction of organic pvt label products - ' + str(cat_organic[i][j])+'/'+str((cat_queries[i][j]-cat_ads[i][j])) + '       Percentage : ' + "{:.2f}".format((cat_organic[i][j]/(cat_queries[i][j]-cat_ads[i][j]))*100) + '\n'
                f.write(line)
                if not cat_ads_serp[i][j]+cat_organic[i][j] == 0 :
                    line = 'Fraction of pvt label products which are ads - ' + str(cat_ads_serp[i][j])+'/'+str((cat_ads_serp[i][j]+cat_organic[i][j])) + '       Percentage : ' + "{:.2f}".format((cat_ads_serp[i][j]/(cat_ads_serp[i][j]+cat_organic[i][j]))*100) + '\n' + '\n'
                    f.write(line)
                else : 
                    f.write('no pvt labels. \n \n')
            line = 'Overall Fraction of pvt label products - ' + str(overAll_serp[j]) +'/' +str(overAll_queries[j]) + '       Percentage : ' + "{:.2f}".format((overAll_serp[j]/overAll_queries[j])*100) + '\n'
            f.write(line)
            line = 'Oveall Fraction of advertised pvt label products - ' + str(overAll_ads_serp[j])+'/'+str(overAll_ads[j]) + '       Percentage : ' + "{:.2f}".format((overAll_ads_serp[j]/overAll_ads[j])*100) + '\n'
            f.write(line)
            line = 'Overall Fraction of organic pvt label products - ' + str(overAll_organic[j])+'/'+str((overAll_queries[j]-overAll_ads[j])) + '       Percentage : ' + "{:.2f}".format((overAll_organic[j]/(overAll_queries[j]-overAll_ads[j]))*100)   + '\n'
            f.write(line)
            if not overAll_ads_serp[j]+overAll_organic[j] ==0 :
                line = 'Overall Fraction of pvt label products which are ads - ' + str(overAll_ads_serp[j])+'/'+str((overAll_ads_serp[j]+overAll_organic[j])) + '       Percentage : ' + "{:.2f}".format((overAll_ads_serp[j]/(overAll_ads_serp[j]+overAll_organic[j]))*100) + '\n' + '\n'
                f.write(line)
            else : 
                f.write('no pvt labels.')


if __name__ == '__main__':
    parse(path)