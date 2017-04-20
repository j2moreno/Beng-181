import sys
import math

def cycletoChrom(cycle):
	chromosome = [0]*(len(cycle)/2)

	for j in range(1, len(cycle)/2 +1):
		
		if cycle[(2*j)-2 ]  < cycle[2*j-1]:
			
			chromosome[j-1] = int(math.ceil(cycle[2*j-1]/2))
		else:
			chromosome[j-1] = -int(math.ceil(cycle[(2*j)-2]/2))

	print chromosome

	return chromosome

def graph(G):
	P = []
	print G
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

	print P
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



filename = sys.argv[1]
file = open(filename, 'r')
data = file.read()
data = data.strip(')')
data = data.strip('(')
data = data.strip('\n')
data = data.strip(')')
data = data.strip(', ')

array = []


array = data.split('), (')

array = map(lambda x: x.split(','), array)
array = [list(map(int,row)) for row in array]

result = graph(array)


