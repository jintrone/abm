import time
import random
import uuid
import math

lambd = 0.01

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
				
class Agent:
	def __init__(self):
		self.ten = round(random.expovariate(lambd))
		self.ften = 0
		self.stage = 0
		self.ineed = random.random()
		if self.ten >= round(math.log(4)/lambd): 
			self.stage = 1
			self.ineed = 0
		else:
			pass
		self.know = random.random()
		self.act = random.random()
		self.inter = {}
		self.id = uuid.uuid4().hex[:10]
		self.stay = 1
		self.capa = random.random()
		self.fit = random.random()
		self.dfit = self.fit - self.fit**2
		self.ppost = []
		
	def addinter(self, id):
		self.inter[id] = 1
	def updinter(self, id):
		self.inter[id] += 1
		
	def evalai(self, post, time):
		if self.know >= post.iran: 
			self.fit = self.fit + self.dfit
			prob = random.random()
			if prob <= self.act:
				p = Post(time, self)
				p.adda(self)
				return self.ppost.append(p)
			else: 
				pass
		else:
			self.fit = self.fit - self.dfit
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
			self.fit = self.fit + self.dfit
			prob = random.random()
			if prob <= self.act:
				p = Post(time, self)
				p.addc(self)
				return self.ppost.append(p)
			else:
				pass
		else:
			self.fit = self.fit - self.dfit
	def evalqc(self, time):
		prob = random.random()
		if prob <= self.act:
			p = Post(time, self)
			p.addc(self)
			return self.ppost.append(p)
		else:
			pass
			
	def leave(self):
		if self.fit < 0.1:
			self.stay = 0
		else:
			pass
	def addten(self):
		self.ten += 1
		self.ften += 1
		if self.ten >= round(math.log(4)/lambd): 
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
		self.iran = random.gauss(agent.ineed, 0.0005)
	def adda(self, agent):
		self.type = 'AI'
		self.iran = random.gauss(agent.know, 0.0005)
	def addc(self, agent):
		self.type = 'C'
		self.info = 0
	
