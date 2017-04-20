import sys


def cycle(chrom):
	cycle = [0]*(len(chrom)*2)

	for j in range(0,len(chrom)):
		element = chrom[j]

		if element > 0 :
			cycle[2*j-1] = 2*element -1
			cycle[2*j] = 2*element
		else:
			cycle[2*j-1] = -2*element
			cycle[2*j] = -2*element -1
	print cycle
	newCycle = [cycle[len(cycle)-1]]
	
	for i in range(len(cycle)-1):
		newCycle.append(cycle[i])

	print newCycle
	return newCycle

def colored(P):
	edges = dict()

	for element in P:
		print element
		nodes = cycle(element)
		for j in range(0,len(element)):
			edges[nodes[2*j-1]] = nodes[2*j]

	return edges



filename = sys.argv[1]
file = open(filename, 'r')
data = file.read()
data = data.strip(')')
data = data.strip('(')
data = data.strip('\n')
data = data.strip(')')
array = []




array = data.split(')(')
print array
array = map(lambda x: x.split(' '), array)
array = [list(map(int,row)) for row in array]


result = colored(array)
newResult = []
for key, value in result.iteritems():
	newResult.append('(' + str(key) + ', ' + str(value) + ')')

print (", ".join(str(x) for x in newResult))


