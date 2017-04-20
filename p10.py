import math

def reverseComp(text):
	reverseStack = []
	for i in range(len(text)):
		if text[i] == "A":
			##text.replace(text[i], 'T')
			reverseStack.append('T')
		elif text[i] == 'T':
			#text.replace(text[i], 'A')
			reverseStack.append('A')
			
		elif text[i] == 'C':
			reverseStack.append('G')
		elif text[i] == 'G':
			reverseStack.append('C')

	reverseComplement = []
	for i in range(len(reverseStack)):
		reverseComplement.append(reverseStack.pop())
	return ("".join(str(x) for x in reverseComplement))

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

def patternToNumber(pat):

	if len(pat) == 0:
		return 0
	symbol = pat[len(pat) - 1] 
	prefix = pat[0:len(pat) - 1]
	
	return 4*patternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(letter):

	if letter == 'A':
		return 0
	elif letter == 'C':
		return 1
	elif letter == 'G':
		return 2
	elif letter == 'T':
		return 3

def numberToPattern(index, k_mer):
	
	temp = []

	if k_mer == 1:
		symbol = numberToSymbol(index)
		array.append(symbol)
		return 0 

	preIndex = index / 4
	remainder = index % 4
	symbol = numberToSymbol(remainder)
	prePattern = numberToPattern(preIndex, k_mer-1)


	array.append(symbol)
	temp = array
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

def approxPatternCount(text, pattern, d):
	count = 0
	end = len(text) - len(pattern)
	for i in range(end):
		pat = text[i:i+len(pattern)]
		if HammingDistance(pattern, pat) <= d:
			count += 1
	return count

def freqWordsWithMismatches(text,k,d):
	freqPatterns = []

	sizeOfArray = int(math.pow(4,k))
	similar = [None] * sizeOfArray 
	freqArray = []
	freqArray = [None] * sizeOfArray

	for i in range(sizeOfArray - 1):
		similar[i] = 0
		freqArray[i] = 0

	end = len(text) - k
	for i in range(end):
		neighbors2 = neighbors(text[i:i+k],d)
		for element in neighbors2:
			position = patternToNumber(element)
			similar[position] = 1
		k_mer = text[i:i+k]
		reverse = reverseComp(k_mer)
		print k_mer
		neighbors3 = neighbors(reverse,d)
		for element in neighbors3:
			position = patternToNumber(element)
			similar[position] = 1

	for j in range(sizeOfArray - 1):
		if similar[j] == 1:
			pat = numberToPattern(j,k)
			del array[:]
			freqArray[j] = approxPatternCount(text,pat,d)
	maxCount = max(freqArray)

	for i in range(sizeOfArray - 1):
		if freqArray[i] == maxCount:
			pat2 = numberToPattern(i,k)
			del array[:]
			
			freqPatterns.append(pat2)
	return freqPatterns

array = []
#sequence = 'GTCACTAACGTCACTAACTAAGTCACTAAGTCACGTGTGGTTAACCCTTGTGTGGTGTCACTAACTAAGTCACTAACCCTTTAACCCTTGTGTGGTTAACCCTTTAACCCTTGTCACTAACTAACCCTTTAAGTCACTTCCCCATGTCACTAACGTGTGGTTTCCCCATGTGTGGTGTCACTAACTTCCCCATTAAGTCACTTCCCCATTAACCCTTGTGTGGTGTGTGGTTAACCCTTGTCACTAACTAAGTCACGTGTGGTGTGTGGTTAAGTCACGTCACTAACTTCCCCATTAACCCTTGTGTGGTGTGTGGTTAACCCTTTTCCCCATTTCCCCATTAAGTCACTTCCCCATTTCCCCATGTGTGGTTAAGTCACTAACCCTTGTGTGGTTAAGTCACTAAGTCACTAAGTCACTAAGTCACGTCACTAACTTCCCCATTAAGTCACTAACCCTTGTGTGGTTAACCCTTGTCACTAACGTGTGGTTAACCCTTTAACCCTTGTGTGGTTAACCCTTGTCACTAACGTGTGGTTTCCCCATTAAGTCACTTCCCCATGTCACTAACTAACCCTTGTCACTAACGTGTGGTGTGTGGTTTCCCCATGTCACTAACTTCCCCATTAAGTCACGTGTGGTTAACCCTTTTCCCCATTTCCCCATGTCACTAACGTGTGGTTAAGTCACTAAGTCACGTCACTAACGTCACTAACGTGTGGTTAAGTCACTAAGTCACTAAGTCACTTCCCCATTAACCCTTTAACCCTTTTCCCCATTTCCCCATTTCCCCAT'

result = freqWordsWithMismatches('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1)
print(" ".join(str(x) for x in result))
