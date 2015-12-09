import time
import random
import uuid

class Agent:
	def __init__(self, lambd):
		self.ten = random.expovariate(lambd)
		self.stage = 0
		if self.ten > 1.0/lambd: self.stage = 1
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
		self.iran = random.random()
		self.auth = 'null'
	def add(self, type, range, author):
		self.type = type
		self.iran = range
		self.auth = author
