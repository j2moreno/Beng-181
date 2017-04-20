import sys
import collections

def eulerianP(graph):
	array = []
	valuesArray = []
	for key in graph.keys():
		array.append(key)
	for values in graph.values():
		for i in range(len(values)):
			valuesArray.append(values[i])

	for element in valuesArray:
		if element not in array:
			endNode = element

	for element in  array:
		outEdges = len(graph[element])
		inEdges = 0
		for values in valuesArray:
			if element == values:
				inEdges +=1

		if inEdges < outEdges:
			startNode = element

	graph[endNode] = [startNode]
	finalResult = eulerian(graph,startNode)
	return finalResult

def eulerian(graph, sNode):
	startNode = sNode
	cycleArray = [startNode]
	nextNode = None
	endNode = startNode

	while(True):

		if len(graph[startNode]) == 0:
			break

		cycleArray.append(graph[startNode][0])	
		if len(graph[startNode]) == 1:
			nextNode = graph[startNode][0]
			del graph[startNode]

		else:
			nextNode = graph[startNode][0]
			del graph[startNode][0]

		if cycleArray[len(cycleArray)-1] in graph:
			startNode = nextNode 
	
		else: 
			break

	while(len(graph) > 0):
		for element in cycleArray:

			if element in graph:
				startNode = element
				newCycle = [startNode]
				nextNode = None
				endNode = startNode
				while(True):

					if len(graph[startNode]) == 0:
						cycleArray = cycleArray[:cycleArray.index(element)] + newCycle + cycleArray[cycleArray.index(element)+1:]
						print cycleArray
						break

					newCycle.append(graph[startNode][0])

					if len(graph[startNode]) == 1:
						nextNode = graph[startNode][0]
						del graph[startNode]

					else:
						nextNode = graph[startNode][0]
						del graph[startNode][0]
							
					if newCycle[len(newCycle)-1] in graph:
						startNode = nextNode

					else:
						cycleArray = cycleArray[:cycleArray.index(element)] + newCycle + cycleArray[cycleArray.index(element)+1:]
						break
					


	return cycleArray


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
	result = eulerianP(dictionary)
	
	finalResult = []
	finalResult.append(result[0])
	del result[len(result)-1]
	for i in range(len(result)):
		i +=1
		if i == len(result):
			break
		finalResult.append(result[i][len(result[i]) -1])



	return finalResult

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

result = BruijnKmers(array)
print("".join(str(x) for x in result))





