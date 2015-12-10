import time
import random
import uuid
import math

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
	def addinter(self, id):
		self.inter[id] = 1
	def updinter(self, id):
		self.inter[id] += 1
	def leave(self):
		self.stay = 0		
		
class Post:
	def __init__(self):
		self.type = random.randint(0,1) #0 Question
		self.info = random.randint(0,1)
		self.iran = 0
		if self.info = 1: self.iran = random.random()
		self.auth = 'null'
	def add(self, type, range, author):
		self.type = type
		self.iran = range
		self.auth = author

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
	
