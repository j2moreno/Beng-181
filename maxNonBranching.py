import sys

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

	return cycleArray
			

def maxBranching(graph):
	paths = []

	for key in graph.keys():
		if inNumber(graph,key) != outNumber(graph,key):
			if outNumber(graph,key) > 0:
				for element in graph[key]:
					nonBrachArray = []
					nonBrachArray.append(key)
					nonBrachArray.append(element)
					while outNumber(graph,element) == inNumber(graph,element):
						nonBrachArray.append(graph[element][0])
						element = graph[element][0]
					paths.append(nonBrachArray)
					print nonBrachArray

	for element in paths:
		for i in range(len(element)):
			if element[i] in graph:
				del graph[element[i]]

	while(len(graph) > 0 ):
		isolatedP = eulerian(graph)
		paths.append(isolatedP)


	return paths

filename = sys.argv[1]

dictionary = dict()
with open(filename) as file:
	for line in file:
		toAdd = line.split('->')[0]
		toAdd2 = line.split('->')[1]
		toAdd2 = toAdd2.split(',')

		dictionary[int(toAdd)] = map(int,toAdd2)
  
result = maxBranching(dictionary)
for element in result:
	array2 = []
	for i in range(len(element)):
		array2.append(element[i])
	print("->".join(str(x) for x in array2))
	





