from model_alpha_3 import Forum, Agent, Post, Para
import random
import pprint
import csv
import pdb

#pdb.set_trace()

f = Forum(50)
for i in f.alist: i.addten()
f.gena(5)

def intera(time = 2):
	temlist = []
	f.alist = [x for x in f.alist if x.stay == 1]
	
	for i in f.alist: 
		if i.stage == 0:
			ppool = [x for x in f.plist if (x.info == 1 and x.auth != i.id and x.time >= i.ften and x.type == 'QI')]
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
			
		i.ppost=[]
	
	for obj1 in temlist:
		f.plist.append(obj1)

def writep():
	outlist = []
	for i in f.plist:
		outlist.append(vars(i))

	with open('plist.csv', 'a') as fun:
		w = csv.DictWriter(fun, lineterminator='\n',
				   fieldnames = ['auth','info','iran','time','type'])
		w.writeheader()
		for i in outlist:
			w.writerow(i)

def writea():		
	outlist = []		
	for i in f.alist:
		tem = dict((k, vars(i)[k]) for k in ('act','capa','fit','dfit','ften','id','ineed', 'npost',
						 'inter','know','stage','stay','ten','k'))
		outlist.append(tem)		
		
	with open('alist.csv', 'a') as fun:
		w = csv.DictWriter(fun, lineterminator='\n',
				   fieldnames = ['act','capa','fit','dfit','ften','id','ineed', 'npost',
						 'inter','know','stage','stay','ten', 'k'])
		w.writeheader()
		for i in outlist:
			w.writerow(i)

def main(l):
	for i in range(2, l):
		intera(i)
		writea()
		f.gena(5)

