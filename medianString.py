import sys
import math

def HammingDistance(first,second):
	hammingDist = 0
	for i in range(len(first)):
		if first[i] != second[i]:
			hammingDist += 1
		continue
	return hammingDist

def numberToPattern(index, k_mer):
	
	temp = []

	if k_mer == 1:
		symbol = numberToSymbol(index)
		array2.append(symbol)
		return 0 

	preIndex = index / 4
	remainder = index % 4
	symbol = numberToSymbol(remainder)
	prePattern = numberToPattern(preIndex, k_mer-1)


	array2.append(symbol)
	temp = array2
	result = ("".join(str(x) for x in temp))
	return result

def numberToSymbol(position):
	if position == 0:
		return 'A'
	elif position == 1:
		return 'C'
	elif position == 2:
		return 'G'
	elif position == 3:
		return 'T'

def distBtwPatternString(pat,DNA):
	k = len(pat)
	distance = 0
	for element in DNA:
		HamDist = float("inf")
		for i in range(len(element) - k):
			pattern2 = element[i:i+k]
			if HamDist > HammingDistance(pat,pattern2):
				HamDist = HammingDistance(pat,pattern2)
		distance = distance + HamDist

	return distance

def medianString(dna,k):
	distance = float("inf")
	size = int(math.pow(4,k))

	for i in range(size - 1):
		pattern = numberToPattern(i,k)
		del array2[:]
		if distance > distBtwPatternString(pattern,dna):
			distance = distBtwPatternString(pattern,dna)
			median = pattern

	return median

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

array2 = []
result = medianString(array,6)
#print(" ".join(str(x) for x in result))
print result




