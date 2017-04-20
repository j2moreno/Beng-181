import sys


def greedy(P):
	approxReversalDist = 0
	perArray = []
	
	for i in range(len(P)):
		tempArray = []
		if P[i] != i +1:
			if i+1 in P:
				indexOfI = P.index(abs(i+1))
			else:
				indexOfI = P.index(-abs(i+1))
			for x in list(reversed(P[i:indexOfI+1])):
				tempArray.append(-int(x))
			P = P[:i] + tempArray + P[indexOfI+1:]
			approxReversalDist +=1
			tempArray2 = P[:]
			
			for y in range(len(tempArray2)):
				if tempArray2[y] > 0:
					tempArray2[y] = "%+d" % (tempArray2[y])

			perArray.append(tempArray2[:])
			

		if P[i] == -(i+1):
			P[i] = i+1
			tempArray3 = P[:]
			for y in range(len(tempArray2)):
				if tempArray3[y] > 0:
					tempArray3[y] = "%+d" % (tempArray3[y])

			perArray.append(tempArray3[:])

	
	return perArray

		

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


result = greedy(seqArray)

for element in result:
	print '('+(" ".join(str(x) for x in element)) + ')'












