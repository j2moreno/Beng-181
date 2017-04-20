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

	newCycle = [cycle[len(cycle)-1]]
	
	for i in range(len(cycle)-1):
		newCycle.append(cycle[i])
	print '(' + (" ".join(str(x) for x in newCycle)) + ')'

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	line = line.strip('(')
	line = line.strip(')')
	array.append([int(x) for x in line.split()])

seqArray = []
for element in array:
	for element2 in element:
		seqArray.append(element2)



result = cycle(seqArray)