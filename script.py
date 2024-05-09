import random
from dna import DNA

population_size = 2000
bestScore = 0

population =[]

for i in range(int(population_size)):
	population.append(DNA())

while bestScore < 1.0:

	for i in range(len(population)):
		population[i].update_fitness()

		if population[i].fitness > bestScore:
			bestScore = population[i].fitness
			print(f"{population[i].getPhrase()}	score:	{round(bestScore, 3)}".replace(chr(127), " "))

	matingPool = []

	previous_population = population[:]
	population = []

	for i in range(len(previous_population)):
		n = int(previous_population[i].fitness * 100)
		for j in range(n):
			matingPool.append(previous_population[i])

	for i in range(len(previous_population)):
		a = random.choice(range(len(matingPool)))
		b = random.choice(range(len(matingPool)))

		parentA = matingPool[a]
		parentB = matingPool[b]
		child = parentA.crossover(parentB)
		child.mutate()

		population.append(child)
