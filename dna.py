import random

chars = range(32,128)
target = "RIP Harambe, Go Giants"

mutationRate = 0.01

class DNA:
	
	def __init__(self):
		self.genes = []
		for i in range(len(target)):
			gene = chr(random.choice(chars))
			self.genes.append(gene)

	def update_fitness(self):
			score = 0
			for i in range(len(self.genes)):
				if self.genes[i] == target[i]:
					score += 1

			self.fitness = float(score)/len(target)

	def crossover(self, partner):
			child = DNA()

			midpoint = random.choice(range(len(self.genes)))

			for i in range(len(self.genes)):
				if i > midpoint:
						child.genes[i] = self.genes[i]
				else:
						child.genes[i] = partner.genes[i]

			return child

	def mutate(self):
				for i in range(len(self.genes)):
					if random.random() < mutationRate:
						self.genes[i] = chr(random.choice(chars))

	def getPhrase(self):
				return ''.join(self.genes)
