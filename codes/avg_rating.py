import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#    This code generates txt file with avg rating category wise, for PL-AD,TP-AD,TP-ORG,PL-ORG        #

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
	sum_pad_cat = {}
	sum_porg_cat = {}
	sum_tad_cat = {}
	sum_torg_cat = {}
	count_pad_cat = {}
	count_porg_cat = {}
	count_tad_cat = {}
	count_torg_cat = {}
	# jqp = {}
	# jqo = {}
	# jcp = {}
	# jco = {}
	for dir in dirs : 
		dir_path = p + dir + '/'
		for thing in os.listdir(dir_path) :
			print(thing)
			if thing == 'horizontal' :
				condition = 40
			elif thing == 'vertical' :
				condition = 24
			if os.path.isdir(dir_path+thing):
				for file in os.listdir(dir_path+thing+'/') :
					# print(dir_path+thing+'/'+file)
					df = pd.read_csv(dir_path+thing+'/'+file)
					query = file.split('_')[0]
					category = file.split('_')[1]
					if category not in sum_pad_cat :
						sum_pad_cat[category] = 0
						count_pad_cat[category] = 0
					if category not in sum_porg_cat :
						sum_porg_cat[category] = 0
						count_porg_cat[category] = 0
					if category not in sum_tad_cat :
						sum_tad_cat[category] = 0
						count_tad_cat[category] = 0
					if category not in sum_torg_cat :
						sum_torg_cat[category] = 0
						count_torg_cat[category] = 0
					# if query not in jqp : 
					# 	jqp[query] = []
					# 	jqo[query] = []
					# if category not in jcp :
					# 	jcp[category] = []
					# 	jco[category] = []
					lst = []
					for ind in df.index :
						if ind < condition :
							rat = df['Rating'][ind]
							# x = df['Ad'][ind]
							# did = df['Data-id'][ind]
							# if x == 0: 
							# 	lst.append(did)
							if not (rat == '-' or pd.isna(rat)):
								rat = float(rat)
								if df['Ad'][ind] == 1 and df['Pvt'][ind] == 1 :
									sum_pad_cat[category] += rat
									count_pad_cat[category] += 1
								elif df['Ad'][ind] == 0 and df['Pvt'][ind] == 1 :
									sum_porg_cat[category] += rat
									count_porg_cat[category] += 1
								elif df['Ad'][ind] == 1 and df['Pvt'][ind] == 0 :
									sum_tad_cat[category] += rat
									count_tad_cat[category] += 1
								# elif df['Ad'][ind] == 0 and df['Pvt'][ind] == 0 :
								else:
									sum_torg_cat[category] += rat
									count_torg_cat[category] += 1
						# for ind in df.index : 
					# 	x = df['Ad'][ind]
					# 	did = df['Data-id'][ind]
					# 	p = df['Pvt'][ind]
					# 	if x == 1 :
					# 		try :
					# 			if p == 1 :
					# 				jqp[query].append(lst.index(did) + 1-ind)
					# 				jcp[category].append(lst.index(did) + 1-ind)
					# 			else :
					# 				jqo[query].append(lst.index(did) + 1-ind)
					# 				jco[category].append(lst.index(did) + 1-ind)
					# 		except :
					# 			if p == 1 :
					# 				jqp[query].append(1001-ind)
					# 				jcp[category].append(1001-ind)
					# 			else :
					# 				jqo[query].append(1001-ind)
					# 				jco[category].append(1001-ind)

	# for cat in jcp.keys() :
	# 	fig = plt.figure(figsize =(10, 10))
	# 	plt.boxplot([jcp[cat],jco[cat]])
	# 	plt.show()

	sum_pad = 0
	sum_tad = 0
	sum_porg = 0
	sum_torg = 0
	count_pad = 0
	count_tad = 0
	count_porg = 0
	count_torg = 0
	with open(p+'todo11.txt','a') as f : 
		for category in sum_pad_cat.keys() :
			sum_pad += sum_pad_cat[category]
			count_pad += count_pad_cat[category]
			sum_tad += sum_tad_cat[category]
			count_tad += count_tad_cat[category]
			sum_porg += sum_porg_cat[category]
			count_porg += count_porg_cat[category]
			sum_torg += sum_torg_cat[category]
			count_torg += count_torg_cat[category]
			print(category)
			line = 'In '+ category  + '\n'
			f.write(line)
			if not count_pad_cat[category] == 0 :
				line = 'The avg rating for advertised pvt labels : ' + "{:.2f}".format(sum_pad_cat[category]/count_pad_cat[category]) + '\n'
			else : 
				line = 'The avg rating for advertised pvt labels : 0'  + '\n'
			f.write(line)
			if not count_porg_cat[category] == 0 :
				line = 'The avg rating for organic pvt labels : ' + "{:.2f}".format(sum_porg_cat[category]/count_porg_cat[category]) + '\n'
			else : 
				line = 'The avg rating for advertised pvt labels : 0'  + '\n'
			f.write(line)
			if not count_tad_cat[category] == 0 :
				line = 'The avg rating for advertised 3-P labels : ' + "{:.2f}".format(sum_tad_cat[category]/count_tad_cat[category]) + '\n'
			else : 
				line = 'The avg rating for advertised pvt labels : 0'  + '\n'
			f.write(line)
			if not count_torg_cat[category] == 0 :
				line = 'The avg rating for organic 3-P labels : ' + "{:.2f}".format(sum_torg_cat[category]/count_torg_cat[category]) + '\n' + '\n'
			else : 
				line = 'The avg rating for advertised pvt labels : 0'  + '\n' + '\n'
			f.write(line)
		line = "{:.2f}".format(sum_pad/count_pad)+ '\n' + "{:.2f}".format(sum_porg/count_porg)+ '\n' + "{:.2f}".format(sum_tad/count_tad)+ '\n' + "{:.2f}".format(sum_torg/count_torg)
		f.write(line)
	print('done')
					

