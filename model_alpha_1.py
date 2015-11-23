import time
import random

class Post:
	def __init__(self):
		self.time = int(time.time())
		self.isb = random.random()
		self.esb = random.random()
		self.csb = random.random()
		self.tot = self.isb + self.esb + self.csb\
		self.show = 1
	def delete(self):
		self.show = 0

class Agent:
	def __init__(self):
		self.isn = random.uniform(0.5,1)
		self.esn = random.uniform(0.3, 0.8)
		self.csn = random.uniform(0, 0.5)
		self.stay = 1
		self.post = 0
		self.totsp = 0
	def leave(self):
		self.stay = 0
	def post(self):
		self.post = 1
	def tally(self, recsp):
		self.totsp += recsp}