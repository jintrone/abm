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
		self.isn = random.random()
		self.esn = random.random()
		self.csn = random.random()
		self.tot = self.isn + self.esn + self.csn
		self.stay = 1
		self.post = 0
		self.totsp = 0
	def leave(self):
		self.stay = 0
	def addpost(self):
		self.post += 1
	def tally(self, recsp):
		self.totsp += recsp
	def new(self):
		self.totsp = 0
		
post = []
nofpost = [500]
for i in range(0,nofpost[0]): post.append(Post())
agent = []
for i in range(0,50): agent.append(Agent())

def agenteval(agent, npost, post):
	for i in range(0, npost): agent.tally(post[i].tot)
	lower = agent.tot * npost
	upper = lower +  npost ** 0.25
	if agent.totsp < lower: 
		agent.leave()
	elif lower <= agent.totsp < upper: 
		pass
	else:
		agent.addpost()
		newpost = Post()
		newpost.new(agent.isn, agent.esn, agent.csn, 0.05)
		return post.append(newpost)

for i in range(0,len(agent)): agenteval(agent[i], nofpost[0], post)

nofpost.append(len(post))
agent1 = [x for x in agent if x.stay==1]
post1 = post[nofpost[1]-nofpost[0]:]

for i in range(0,len(agent1)): 
	agent1[i].new()
	agenteval(agent1[i], nofpost[0], post1)
