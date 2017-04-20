import sys
import math

def chrom(cycle):
	chromosome = [0]*(len(cycle)/2)

	for j in range(1, len(cycle)/2 +1):
		
		if cycle[(2*j)-2 ]  < cycle[2*j-1]:
			
			chromosome[j-1] = int(math.ceil(cycle[2*j-1]/2))
		else:
			chromosome[j-1] = -int(math.ceil(cycle[(2*j)-2]/2))

	
	printChrom = []
	for x in range(len(chromosome)):
		if chromosome[x] > 0:
			printChrom.append("%+d" % (chromosome[x]))
		else:
			printChrom.append(chromosome[x])

	return printChrom 

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

result = chrom(seqArray)

print '('+(" ".join(str(x) for x in result)) + ')'