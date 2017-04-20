import sys
import collections

def BruijnKmers(text):

	dictionary = dict()

	for element in text:
		kmer = element[i:i+k-1]
		kmer2 = element[i+1:i+k]
		if kmer in dictionary:
			dictionary[kmer].add(kmer2)
		else:
			dictionary[kmer] = {kmer2}
	
	result = collections.OrderedDict(sorted(dictionary.items()))
	return result

'''	for element in array:
		suffix = element[1:]
		for element2 in array:
			prefix = element2[:-1]
			if element[:-1] in dictionary:
				dictionary[element[:-1]].add(element2[:-1])
			else:
				dictionary[element[:-1]] = {element2[:-1]}
'''
	
	
	
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
	