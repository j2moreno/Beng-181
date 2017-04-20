import sys

def motifEnumeration(dna, k ,d):
	patterns = set()
	for element in dna:
		for i in range(len(element) - k +1):
			k_mer = element[i:i+k]
			neighborhood = neighbors(k_mer,d)
			for pat in neighborhood:
				
				for strings in dna:
					count = 0
					for j in range(len(strings) - k +1):
						if HammingDistance(pat,strings[j:j+k]) <= d:
							count = 1
							

					if count == 0:
						break	

				if count == 1:
					patterns.add(pat)


	return list(set(patterns))

def HammingDistance(first,second):
	hammingDist = 0
	for i in range(len(first)):
		if first[i] != second[i]:
			hammingDist += 1
		continue
	return hammingDist

def neighbors(pattern,d):
	if d == 0:
		return pattern
	if len(pattern) == 1:
		return ['A','C','G','T']

	neighborArray = set()
	suffixNeighbors = neighbors(pattern[1:],d)
	for element in suffixNeighbors:
		if HammingDistance(pattern[1:], element) < d:
			for x in 'AGCT':
				neighborArray.add(x + element)
		else:
			neighborArray.add(pattern[0] + element)

	return neighborArray

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)


result = motifEnumeration(array, 5, 2)
print(" ".join(str(x) for x in result))
