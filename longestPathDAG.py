import sys
import copy

def topoOrdering(graph2):
	ordering = []
	candidates = incomingEdges(graph2)
	
	candidates = list(set(candidates))
	while len(candidates) > 0:
		node = candidates[0]
		ordering.append(node)
		while(True):

			if node not in graph2.keys():
				break
			nextNode = graph2[node][0]
			
			del graph2[node][0]
			if anyEdges(nextNode,graph2) == 0:
				candidates.append(nextNode)

			if len(graph2[node]) == 0:
				break
		

		candidates.remove(node)
		
	return ordering

def anyEdges(node,graph3):
	count = 0

	for values in graph3.values():
		for i in range(len(values)):
			if node == values[i]:
				count += 1
	return count

def incomingEdges(graph3):

	array = set()

	for key in graph3.keys():
		array.add(key)

	for values in graph3.values():
		for i in range(len(values)):
			if values[i] in array:
				array.discard(values[i])

	return array


def longestPath(graph, weightGraph, source, sink):
	weights = dict()
	tempGraph = copy.deepcopy(graph)
	order = topoOrdering(graph)
	for value in order:
		weights[value] = float("-inf")
	weights['0'] = 0
	order.remove(order[0])

	for value in order:
		if weights[value] < weights[]		







filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

dictionary = dict()
for element in array:
	key = element[0]
	value = element[3]
	if key not in dictionary:
		dictionary[key] = [value]
	else:
		dictionary[key].append(value)

dictionary2 = dict()
for element in array:
	key = element[0]
	value = element[3:]
	if key not in dictionary2:
		dictionary2[key] = [value]
	else:
		dictionary2[key].append(value)


longestPath(dictionary,dictionary2,0,4)
