import sys
import collections

def overlapSolve(text):
	overlap = dict()
	for element in text:
		suffix = element[1:]
		for element2 in text:
			prefix = element2[0:len(element2)-1]
			if prefix == suffix:
				overlap[element] = element2

	result = collections.OrderedDict(sorted(overlap.items()))
	return result


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

result = overlapSolve(array)

for x in result.items():
	print x[0] + " -> " + x[1]