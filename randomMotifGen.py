import sys
import random
import operator

def randomMotif(dna,k,t):

	bestMotifs = []
	motifsArray = []
	temp = []
	best = []
	for element in dna:
		for i in range(len(element)):
			random1 = random.randint(0,len(element) - k)
			motifsArray.append(element[random1:random1+k])
			break

	bestMotifs = motifsArray
	while(True):
		matrixMotif = profile(motifsArray)
		temp = profileKmer2(dna,k,matrixMotif)
		
		if score(temp) < score(bestMotifs):
			bestMotifs = temp
		else: 
			best = [score(bestMotifs), bestMotifs]
			return best


def profileKmer2(DNA,k_mer,matrix2):
	array3 = []
	for element in DNA:
		array3.append(profileKmer(element,k_mer,matrix2))
	return array3

def profile(motifs):
	matrix = [[],[],[],[]]

	for i in range(len(motifs[0])): #column by column
		A = 1
		C = 1
		G = 1
		T = 1

		for element in motifs:
			if element[i] == 'A':
				A += 1
			elif element[i] == 'C':
				C += 1
			elif element[i] == 'G':
				G += 1
			elif element[i] == 'T':
				T += 1

		total = A + C + G + T
		matrix[0].append(float(A)/total)
		matrix[1].append(float(C)/total)
		matrix[2].append(float(G)/total)
		matrix[3].append(float(T)/total)


	return matrix

def score(patternMotif):
	score2 = 0

	for i in range(len(patternMotif[0])):
		A = 0
		C = 0
		G = 0
		T = 0

		for element in patternMotif:
			if element[i] == 'A':
				A += 1
			elif element[i] == 'C':
				C += 1
			elif element[i] == 'G':
				G += 1
			elif element[i] == 'T':
				T += 1

		array = []
		array.append(A)
		array.append(C)
		array.append(G)
		array.append(T)

		maxNumber = max(array)
		total = A + C + G + T
		columnScore = total - maxNumber
		score2 = score2+columnScore

	return score2


def profileKmer(text, k, matrix):
	array = dict()
	bestk = text[0:int(k)]
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

bestOverall = [float("inf"), []]
end = 0
while(end != 1000):
	result = randomMotif(array,15,20)
	if result[0] < bestOverall[0]:
		bestOverall = result
	end +=1

answer = bestOverall[1]
print("\n".join(str(x) for x in answer))



