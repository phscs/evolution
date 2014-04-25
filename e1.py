import random
import string

goal = "To be or not to be? That is the question."
mutability = 0.01

# INITIALIZE POPULATION
population = []
generations = 0

for s in range(100):
	new_string = ""
	
	for c in range(len(goal)):
		new_string += string.printable[random.randint(0, len(string.printable)-1)]
		
	population.append(new_string)

# SUBMIT POPULATION TO FITNESS TEST
unfit = True
winner = None

while unfit:
	fittest = []

	for s in population:
		print s
				
		score = 0
		
		for i in range(len(s)):
			if s[i] == goal[i]:
				score += 1
				
		if len(fittest) < 0.1 * len(population):
			fittest.append([s, score])
			
		else:
			for f in range(len(fittest)):
				if score > fittest[f][1]:
					fittest[f] = [s, score]
					break
					
		if score >= len(goal):
			unfit = False
			winner = s
						
	# MATE FITTEST INDIVIDUALS TO PRODUCE A NEW GENERATION OF THE POPULATION
	next_generation = []

	while len(next_generation) < len(population):
		f1 = fittest[random.randint(0, len(fittest)-1)][0]
		f2 = fittest[random.randint(0, len(fittest)-1)][0]
		
		new_individual = ""
		
		for character in f1[:len(f1)/2]:
			if random.random() < mutability:
				new_individual += string.printable[random.randint(0, len(string.printable)-1)]
			else:
				new_individual += character
				
		for character in f2[len(f2)/2:]:
			if random.random() < mutability:
				new_individual += string.printable[random.randint(0, len(string.printable)-1)]
			else:
				new_individual += character
				
		next_generation.append(new_individual)
			
	population = next_generation
	generations += 1
			
print winner
print "Generations: " + str(generations)
