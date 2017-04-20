
'''def immediateNeighbors(pattern2):
	arrayNeighbor = []
	tempArray = []

	for i in range(len(pattern2)):
		symbol = pattern2[i]
		tempArray = determineSub(symbol)
		for element in range(len(tempArray)):
			tempPattern = pattern2
			listPattern = list(tempPattern)
			listPattern[i] = tempArray[element]
			temp = "".join(listPattern)
			arrayNeighbor.append(temp)

	result2 = (" ".join(str(x) for x in arrayNeighbor))
	return result2
		#for element in range() 
'''

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
			#temp = determinSub2()
			for x in 'AGCT':
				neighborArray.add(x + element)
		else:
			neighborArray.add(pattern[0] + element)

	return neighborArray

'''def iterativeNeighbors(pattern,d):

	neighborArray = []
	neighborArray.append(pattern)
	for i in range(d):
		i += 1
		for element in range(len(neighborArray)):
			neighborArray.append(immediateNeighbors(pattern))

	print neighborArray
	array = list(set(neighborArray))
	print array
	#result = (" ".join(str(x) for x in neighborArray))
	print result'''

#neighborArray = set()
#iterativeNeighbors('GACCAGGTC',3)
result = neighbors('CAGATCTCC', 3)
#result3 = (" ".join(str(x) for x in result))
result2 = list(set(result))
print '\n'.join(result2)
	
