import time
import random
import uuid

class Post:
	def __init__(self):
		self.time = time.time()
		self.isb = random.random()
		self.esb = random.random()
		self.csb = random.random()
		self.tot = self.isb + self.esb + self.csb
		self.show = 1
	def delete(self):
		self.show = 0
	def new(self, mui, mue, muc, sigma):
		self.time = time.time()
		self.isb = random.gauss(mui, sigma)
		self.esb = random.gauss(mue, sigma)
		self.csb = random.gauss(muc, sigma)
		self.tot = self.isb + self.esb + self.csb
		self.show = 1

class Agent:
	def __init__(self):
		self.ten = random.expovariate(lambd) #survival with para. lambda
		self.stage = 1 #info seeking
		self.ineed = 1
		self.know = random.random()
		self.inter = []
		self.act = random.random()
	def leave(self):
		self.stay = 0
	def addpost(self):
		self.post += 1
	def tally(self, recsp):
		self.totsp += recsp
	def new(self):

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
