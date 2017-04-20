import sys
import operator 

def profileKmer(text, k, matrix):
	array = dict()
	bestk = text[0:len(k)]
	bestProb = 0
	k = int(k)
	end = len(text) - k
	for i in range(end):
		pat = text[i:i+k]
		probability = computeProb(pat, matrix)
		array.update({pat:probability})
		if bestProb < probability:
			bestProb = probability
			bestk = pat

	print bestk
	result = max(array.iteritems(), key=operator.itemgetter(1))[0]
	return bestk

def computeProb(pattern, mat):
	probability = 1
	count = 0
	for i in range(len(pattern)):
		if pattern[i] == 'A':
			probability = probability * float(mat[0][count])
		elif pattern[i] == 'C':
			probability = probability * float(mat[1][count])
		elif pattern[i] == 'G':
			probability = probability * float(mat[2][count])
		elif pattern[i] == 'T':
			probability = probability * float(mat[3][count])

		count += 1

	return probability


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)


dna = array[0]
k_mer = array[1]

temp = []
for i in array[2:]:
	temp.append(i)


matrix1 = []
for element in temp:
	matrix1.append(element.split(' '))
 

result = profileKmer(dna,k_mer,matrix1)
print result
