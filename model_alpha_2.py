import time
import random

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
