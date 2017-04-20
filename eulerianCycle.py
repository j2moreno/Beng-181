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
			

filename = sys.argv[1]

dictionary = dict()
with open(filename) as file:
	for line in file:
		toAdd = line.split('->')[0]
		toAdd2 = line.split('->')[1]
		toAdd2 = toAdd2.split(',')

		dictionary[int(toAdd)] = map(int,toAdd2)
  


result = eulerian(dictionary)
print("->".join(str(x) for x in result))







