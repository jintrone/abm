from model_alpha_2 import Forum, Agent, Post
import random
import pprint
import csv

f = Forum(10)
for i in f.alist: i.addten() #len=10
f.gena(10)

def main(time = 2):
	temlist = []
	apool = [x for x in f.alist if x.stay == 1]
	
	for i in apool: #len=20
		if i.stage == 0:#info seeking
			ppool = [x for x in f.plist if (x.info == 1 and x.auth != i.id and x.time >= i.ften)]
			for j in ppool:
				prob = random.random()
				if prob <= i.capa:
					i.evalai(j, time)
					if j.auth in i.inter:
						i.updinter(j.auth)
					else:
						i.addinter(j.auth)
				else:
					pass
			i.evalqi(time)
		else:
			ppool = [x for x in f.plist if (x.info == 0 and x.auth != i.id and x.time >= i.ften)]
			for j in ppool:
				prob = random.random()
				if prob <= i.capa:
					i.evalc(j, time)
					if j.auth in i.inter:
						i.updinter(j.auth)
					else:
						i.addinter(j.auth)
				else:
					pass
			i.evalqc(time)	
		
		i.leave()
		if i.stay == 1:
			i.addten()
		else:
			pass
		
		for obj0 in i.ppost: 
			temlist.append(obj0)
	
	for obj1 in temlist:
		f.plist.append(obj1)

def write():
	outlist = []
	for i in f.plist:
		outlist.append(vars(i))

	with open('plist.csv', 'a') as fun:
		w = csv.DictWriter(fun, lineterminator='\n',
				   fieldnames = ['auth','info','iran','time','type'])
		w.writeheader()
		for i in outlist:
			w.writerow(i)
			
	outlist = []		
	for i in f.alist:
		outlist.append(vars(i))		
		
	with open('alist.csv', 'a') as fun:
		w = csv.DictWriter(fun, lineterminator='\n',
				   fieldnames = ['act','capa','fit','dfit','ften','id','ineed',
						'inter','know','ppost','stage','stay','ten'])
		w.writeheader()
		for i in outlist:
			w.writerow(i)	
