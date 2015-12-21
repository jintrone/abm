import time
import random
import uuid
import math

class Forum:
	def __init__(self, num):
		self.plist = []
		self.alist = []
		for i in range(0, num):
			a = Agent()
			p = Post(1, a)
			self.alist.append(a)
			if a.stage == 0: 
				p.addq(a)
			else :
				p.addc(a)
			self.plist.append(p)
	def gena(self, num):
		for i in range(0, num):
			a = Agent()
			self.alist.append(a)

class Para: #externalizing the parameters
	def __init__(self):
		lambd = 0.01
		q = 4
		thre = 0.1
		self.int = 20
		self.p = {}
		self.p['ten'] = random.expovariate(lambd) #expo distribution to determine tenure
		self.p['qua'] = math.log(q)/lambd #quantile for expo distr.
		self.p['nint'] = [round(x * 1.0/self.int, 2) for x in range(1, self.int + 1)] #divide [0,1] into 20 equal intervals
		self.p['kint'] = [round(x * 1.0/self.int, 2) for x in range(1, self.int + 1)]
		self.p['act'] = random.random() #active level
		self.p['capa'] = random.random() #capacity
		self.p['fit'] = random.random()
		self.p['fthr'] = thre #threshold for fit
				
class Agent:
	def __init__(self):
		self.r = Para()
		self.ten = round(self.r.p['ten'])
		self.ften = 0
		self.stage = 0
		self.k = min(round(self.r.p['ten']/self.r.p['qua']*self.r.int),self.r.int) #determine the number of intervals to sample based on tenure
		self.ineed = random.sample(self.r.p['nint'], self.r.int-self.k) #randomly sample 20-k intervals as need
		if self.ten >= self.r.p['qua']: 
			self.stage = 1
			self.ineed = 0
		else:
			pass
		self.know = random.sample(self.r.p['nint'], self.k) #randomly sample k intervals as knowledge
		self.act = self.r.p['act']
		self.inter = {}
		self.id = uuid.uuid4().hex[:10]
		self.stay = 1
		self.capa = self.r.p['capa']
		self.fit = self.r.p['fit']
		self.dfit = self.fit - self.fit**2
		self.ppost = []
		
	def addinter(self, id):
		self.inter[id] = 1
	def updinter(self, id):
		self.inter[id] += 1
		
	def evalai(self, post, time):
		if len(set(self.know) & set(post.iran)) >= 5: #compare two intervals, has five or more intervals in common
			self.fit += self.dfit
			prob = random.random()
			if prob <= self.act:
				p = Post(time, self)
				p.adda(self)
				return self.ppost.append(p)
			else: 
				pass
		else:
			self.fit -= self.dfit
	def evalqi(self, time):
		prob = random.random()
		if prob <= self.act:
			p = Post(time, self)
			p.addq(self)
			return self.ppost.append(p)
		else:
			pass
	def evalc(self, post, time):
		if post.auth in self.inter:
			self.fit += self.dfit
			prob = random.random()
			if prob <= self.act:
				p = Post(time, self)
				p.addc(self)
				return self.ppost.append(p)
			else:
				pass
		else:
			self.fit -= self.dfit
	def evalqc(self, time):
		prob = random.random()
		if prob <= self.act:
			p = Post(time, self)
			p.addc(self)
			return self.ppost.append(p)
		else:
			pass
			
	def leave(self):
		if self.fit < self.r.p['fit']:
			self.stay = 0
		else:
			pass
	def addten(self):
		self.ten += 1
		self.ften += 1
		if self.ten >= self.r.p['qua']: 
			self.stage = 1
			self.ineed = 0
		
		
class Post:
	def __init__(self, time, agent):
		self.iran = 0
		self.auth = agent.id
		self.info = 1
		self.time = time
	def addq(self, agent):
		self.type = 'QI'
		self.iran = agent.ineed
	def adda(self, agent):
		self.type = 'AI'
		self.iran = agent.know
	def addc(self, agent):
		self.type = 'C'
		self.info = 0
	
