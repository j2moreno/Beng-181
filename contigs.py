import sys
import collections

def BruijnKmers(text):

	dictionary = dict()

	for element in text:
		kmer = element[:-1]
		kmer2 = element[1:]
		if kmer in dictionary:
			dictionary[kmer].append(kmer2)
		else:
			dictionary[kmer] = [kmer2]
	
	
	#result = collections.OrderedDict(sorted(dictionary.items()))
	return maxBranching(dictionary)


def inNumber(graph2,v):

	inNum = 0

	for element in graph2.values():
		for i in range(len(element)):
			if v == element[i]:
				inNum += 1

	return inNum

def outNumber(graph2,v):

	outNum = 0
	if v not in graph2.keys():
		return outNum

	for element in graph2[v]:
		outNum +=1

	return outNum

def eulerian(graph2):
	sNode = graph2.keys()[0]
	cycleArray = [sNode]
	nextNode = None
	endNode = sNode

	while(True):

		if len(graph2[sNode]) == 0:
			break

		cycleArray.append(graph2[sNode][0])	
		if len(graph2[sNode]) == 1:
			nextNode = graph2[sNode][0]
			del graph2[sNode]

		else:
			nextNode = graph2[sNode][0]
			del graph2[sNode][0]

		if cycleArray[len(cycleArray)-1] in graph2:
			sNode = nextNode 
	
		else: 
			break

	return cycleArray
			

def maxBranching(graph):
	paths = []

	for key in graph.keys():
		if inNumber(graph,key) != 1 or outNumber(graph,key) != 1:
			if outNumber(graph,key) > 0:
				for element in graph[key]:
					nonBrachArray = []
					nonBrachArray.append(key)
					nonBrachArray.append(element)
					while outNumber(graph,element) == 1 and inNumber(graph,element) == 1:
						nonBrachArray.append(graph[element][0])
						element = graph[element][0]
					paths.append(nonBrachArray)
					


	for element in paths:
		for i in range(len(element)):
			if element[i] in graph:
				del graph[element[i]]

	while(len(graph) > 0 ):
		isolatedP = eulerian(graph)
		paths.append(isolatedP)

	return paths

def reconstruction(k_strings):
	recon = []
	
	for element in k_strings:
		temp = []
		for i in range(len(element)):
			if i == len(element) - 1:
				temp.append(element[i])
				break
			temp.append(element[i][0])
		recon.append(temp)

	temp = []
	for element in recon:
		element = "".join(str(x) for x in element)
		temp.append(element)
	
	temp = " ".join(str(x) for x in temp)
	return temp

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

result = BruijnKmers(array)
finalResult = reconstruction(result)
print finalResult



