import time
import random
import uuid
import math

class Forum:
	def __init__(self, num):
		self.plist = []
		self.alist = []
		for i in range(0, num):
			a = Agent(100)
			p = Post(0, a)
			self.alist.append(a)
			if a.stage == 0: 
				p.addq(a)
			else :
				p.addc(a)
			self.plist.append(p)

class Agent:
	def __init__(self, lambd):
		self.ten = random.expovariate(lambd)
		self.stage = 0
		self.ineed = random.random()
		if self.ten > math.log(10)/lambd: 
			self.stage = 1
			self.ineed = 0
		self.know = random.random()
		self.act = random.random()
		self.inter = {}
		self.id = uuid.uuid4().hex[:10]
		self.stay = 1
		self.capa = random.random()
	def addinter(self, id):
		self.inter[id] = 1
	def updinter(self, id):
		self.inter[id] += 1
	def leave(self):
		self.stay = 0		
		
class Post:
	def __init__(self, time, agent):
		self.info = 0
		self.iran = 0
		self.comm = 0
		self.auth = agent.id
		self.time = time
	def addq(self, agent):
		self.type = 'Q'
		self.info = 1
		self.iran = random.gauss(agent.ineed, 0.0005)
	def adda(self, agent):
		self.type = 'A'
		self.info = 1
		self.iran = random.gauss(agent.ineed, 0.0005)
	def addc(self, agent):
		self.type = 'C'
		self.comm = 1
	
def postq(agent, ifit, cfit):
	agent.act
	agent.stage
	ifit
	cfit
	newq = Post()
	return newq.add(type, range, agent.id)

def postir(agent, post):
	agent.act
	overlap = abs(agent.know - post.iran)
	newr = Post()
	return newr.add(type, range, agent.id)
	
def postcr(agent, post):
	agent.act
	if post.auth in agent.inter: times = agent.inter[post.auth]
	newr = Post()
	return newr.add(type, range, agent.id)
	
