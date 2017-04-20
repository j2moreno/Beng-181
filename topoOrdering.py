import sys

def topoOrder(graph2):
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


filename = sys.argv[1]

dictionary = dict()
with open(filename) as file:
	for line in file:
		toAdd = line.split('->')[0]
		toAdd2 = line.split('->')[1]
		toAdd2 = toAdd2.split(',')

		dictionary[int(toAdd)] = map(int,toAdd2)
  
result = topoOrder(dictionary)
print(", ".join(str(x) for x in result))


