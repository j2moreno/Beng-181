import sys

def breakonGG(G, i, iPrime, j, jPrime):
	
	
	if i in G.keys():
		del G[i]

	if int(jPrime) in G.keys():
		del G[int(jPrime)]

	if int(iPrime) in G.keys():
		del G[int(iPrime)]

	if int(j) in G.keys():
		del G[int(j)]
	
	

	G[int(i)] = int(j)
	G[int(iPrime)] = int(jPrime)
	
	return G


filename = sys.argv[1]
file = open(filename, 'r')
data = file.readline()
data = data.strip(')')
data = data.strip('(')
data = data.strip('\n')
data = data.strip(')')
data = data.strip(', ')

array = []


array = data.split('), (')

array = map(lambda x: x.split(','), array)
array = [list(map(int,row)) for row in array]

dictionary = dict()
for element in array:
	dictionary[element[0]] = element[1]

data2 = file.readline()


array2 = []
array2 = data2.split(', ')

for i in range(len(array2)):
	array2[i] = int(array2[i])


first = array2[0] 
second = array2[1]
third = array2[2]
fourth = array2[3] 


result = breakonGG(dictionary, first, second, third, fourth)
resultArray = []
for key,value in result.items():
	 resultArray.append([key,value])

last = []
for element in resultArray:
	last.append('('+(", ".join(str(x) for x in element)) + ')')

print (", ".join(str(x) for x in last))


