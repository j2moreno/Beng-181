import sys
import collections

def eulerian(graph):
	sNode = graph.keys()[0]
	cycleArray = [sNode]
	nextNode = None
	endNode = sNode

	while(True):

		if len(graph[sNode]) == 0:
			break

		cycleArray.append(graph[sNode][0])	
		if len(graph[sNode]) == 1:
			nextNode = graph[sNode][0]
			del graph[sNode]

		else:
			nextNode = graph[sNode][0]
			del graph[sNode][0]

		if cycleArray[len(cycleArray)-1] in graph:
			sNode = nextNode 
	
		else: 
			break

	while(len(graph) > 0):
		for element in cycleArray:

			if element in graph:
				sNode = element
				newCycle = [sNode]
				nextNode = None
				endNode = sNode
				while(True):

					if len(graph[sNode]) == 0:
						cycleArray = cycleArray[:cycleArray.index(element)] + newCycle + cycleArray[cycleArray.index(element)+1:]
						print cycleArray
						break

					newCycle.append(graph[sNode][0])

					if len(graph[sNode]) == 1:
						nextNode = graph[sNode][0]
						del graph[sNode]

					else:
						nextNode = graph[sNode][0]
						del graph[sNode][0]
							
					if newCycle[len(newCycle)-1] in graph:
						sNode = nextNode

					else:
						cycleArray = cycleArray[:cycleArray.index(element)] + newCycle + cycleArray[cycleArray.index(element)+1:]
						break
					

	return cycleArray

def BruijnKmers(kmer):

	array = []
	for i in range(2**kmer):
		array.append('{0:04b}'.format(i))

	dictionary = dict()

	for element in array:
		kmer2 = element[:-1]
		kmer3 = element[1:]
		if kmer2 in dictionary:
			dictionary[kmer2].append(kmer3)
		else:
			dictionary[kmer2] = [kmer3]
	print dictionary
	orderedDictionary = collections.OrderedDict(sorted(dictionary.items()))
	result = eulerian(orderedDictionary)

	finalResult = []
	del result[len(result)-1]
	for i in range(len(result)):
		finalResult.append(result[i][0])

	return finalResult


result = BruijnKmers(4)
print("".join(str(x) for x in result))
