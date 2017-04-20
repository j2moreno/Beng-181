import sys
import math
import collections

def cycletoChrom(cycle):
	chromosome = [0]*(len(cycle)/2)

	for j in range(1, len(cycle)/2 +1):
		
		if cycle[(2*j)-2 ]  < cycle[2*j-1]:
			
			chromosome[j-1] = int(math.ceil(cycle[2*j-1]/2))
		else:
			chromosome[j-1] = -int(math.ceil(cycle[(2*j)-2]/2))

	return chromosome

def graph(G):
	P = []

	
	for element in G:

		if element[1] % 2 == 0:
			toAdd = element[1] - 1
			
			element.insert(len(element), toAdd)
			
		else:
			#odd add 1
			toAdd = element[1] + 1
			
			element.insert(len(element), toAdd)

		if element[0] % 2 == 0:
			#even minus 1
			toAdd = element[0] - 1
			element = [toAdd] + element
		else:
			#odd add 1
			toAdd = element[0] + 1
			element = [toAdd]+ element


		chrom = cycletoChrom(element)
		for item in chrom:
			P.append(item)

	
	bigArray = []
	i = 0
	while i < len(P):

		if i == 0:
			head = P[0]
			i += 1
		if head == P[i]:#found cycle
			bigArray.append(P[:i])
			for j in range(i+1):
				P[j] = 0
			if i == len(P) -1:
				break

			head = P[i+1]
			
			i += 1

		i += 1

	biggerArray = []
	
	for element in bigArray:
		tempArray = []
		for element2 in element:
			if element2 != 0:
				tempArray.append(element2)
		biggerArray.append(tempArray)


	
	cycles = []

	for element in biggerArray:
		i = 1
		while i < len(element):
			if element[i-1] == element[i]:
				element.remove(element[i])
			i += 1

		cycles.append(element)
	
	printChrom = []
	for element in cycles:
		for i in range(len(element)):
			if element[i] > 0:
				element[i] = ("%+d" % (element[i]))

		printChrom.append(element)
	
	lastArray = []
	for element in printChrom:
		lastArray.append('('+(" ".join(str(x) for x in element)) + ')')

	print ("".join(str(x) for x in lastArray))



def breakonGG(G, i, iPrime, j, jPrime):
	


	if i in G.keys():
		
		del G[i]

	if int(jPrime) in G.keys():
		
		del G[int(jPrime)]

	if int(iPrime) in G.keys():
		
		del G[int(iPrime)]

	if int(j) in G.keys():
		
		del G[int(j)]
	
	
	G[int(j)] = int(i)
	G[int(iPrime)] = int(jPrime)
	
	return G

def cycle(chrom):
	cycle = [0]*(len(chrom)*2)

	for j in range(0,len(chrom)):
		element = chrom[j]

		if element > 0 :
			cycle[2*j-1] = 2*element -1
			cycle[2*j] = 2*element
		else:
			cycle[2*j-1] = -2*element
			cycle[2*j] = -2*element -1

	newCycle = [cycle[len(cycle)-1]]
	
	for i in range(len(cycle)-1):
		newCycle.append(cycle[i])
	
	return newCycle

def colored(P):
	edges = dict()
	

	for element in P:
		nodes = cycle(element)
		for j in range(0,len(element)):
			edges[nodes[2*j-1]] = nodes[2*j]

	return edges


def break_2(Pgraph, i, iPrime, j, jPrime):
	
	genomeG = colored(Pgraph)

	genomeG = breakonGG(genomeG, i, iPrime, j, jPrime)
	tempArray = []
	genomeG = collections.OrderedDict(sorted(genomeG.items()))
	#print genomeG
	for key, value in genomeG.iteritems():
		tempArray.append([key,value])
	

	
	Pgraph = graph(tempArray)












filename = sys.argv[1]
file = open(filename, 'r')
data = file.readline().splitlines()
array = []

for line in data:
	line = line.strip('(')
	line = line.strip(')')
	array.append([int(x) for x in line.split()])


data2 = file.readline()

array2 = []
array2 = data2.split(', ')

for i in range(len(array2)):
	array2[i] = int(array2[i])


first = array2[0] 
second = array2[1]
third = array2[2]
fourth = array2[3] 


result = break_2(array, first, second, third, fourth)