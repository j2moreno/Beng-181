import sys

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


filename = sys.argv[1]

dictionary = dict()
with open(filename) as file:
	for line in file:
		toAdd = line.split('->')[0]
		toAdd2 = line.split('->')[1]
		toAdd2 = toAdd2.split(',')

		dictionary[int(toAdd)] = map(int,toAdd2)
  

print dictionary
result = eulerianP(dictionary)
print("->".join(str(x) for x in result))
