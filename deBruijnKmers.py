import sys
import collections

def BruijnKmers(text):

	dictionary = dict()

	for element in text:
		kmer = element[:-1]
		kmer2 = element[1:]
		if kmer in dictionary:
			dictionary[kmer].append(kmer2)
		else:
			dictionary[kmer] = [kmer2]
	
	
	result = collections.OrderedDict(sorted(dictionary.items()))
	return result

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

result = BruijnKmers(array)
for x in result.items():
	matches = ','.join(x[1])
	print x[0] + " -> " + str(matches)
	