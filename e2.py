import random
import string

goal = "To be or not to be? That is the question."

# INITIALIZE RANDOM POPULATION
population = []
population_size = 100
mutability = 0.01

for x in range(population_size):
	individual = ""
	
	for c in range(len(goal)):
		individual += string.printable[random.randint(0, len(string.printable)-1)]
		
	population.append(individual)
 
unfit = True
generations = 0
winner = None

while unfit:
	# SUBJECT OUR POPULATION TO FITNESS TEST
	scores = []
	
	for individual in population:
		#print individual
		
		score = 0
		
		for i in range(len(individual)):
			if individual[i] == goal[i]:
				score += 1
				
		scores.append([score, individual])
		
		if score >= len(goal):
			winner = individual
			unfit = False
		
	scores.sort()
	for score in scores:
		print "individual: " + score[1]
		print "score: " + str(score[0])
		print ""

	"""
	# SELECT THE FITTEST INDIVIDUALS FOR PROCREATION
	next_generation = []
	fittest = scores[0:population_size/10]
	
	while len(next_generation) < len(population):
		p1 = fittest[random.randint(0, len(fittest)-1)][1]
		p2 = fittest[random.randint(0, len(fittest)-1)][1]
				
		# if p1 != p2:
		child = ""
		
		for character in p1[:len(p1)/2]:
			if random.random() < mutability:
				child += string.printable[random.randint(0, len(string.printable)-1)]
			else:
				child += character
				
		for character in p2[len(p2)/2:]:
			if random.random() < mutability:
				child += string.printable[random.randint(0, len(string.printable)-1)]
			else:
				child += character
				
		next_generation.append(child)			

	# OFFSPRING ARE NEW POPULATION
	population = next_generation
	generations += 1
	
print winner
print "Generations: " + generations
"""
