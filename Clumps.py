import math

count = 0
array = []

def findClumpsFast(genome,k,L,t):
	freqPatterns = []

	sizeOfArray = int(math.pow(4,k))
	clump = [None] * sizeOfArray 
	for i in range(sizeOfArray - 1 ):
		clump[i] = 0

	window = genome[0:L]
	freqArray = computeFreqs(window,k)
	for i in range(sizeOfArray - 1 ):
		if freqArray[i] >= t:
			clump[i] = 1

	end = len(genome) - L
	for index in range(end):
		index += 1
		firstPat = genome[index-1:index+k -1]
		position = patternToNumber(firstPat)
		freqArray[position] = freqArray[position] - 1
		lastPat = genome[index+L-k: index+L]
		position = patternToNumber(lastPat)
		freqArray[position] = freqArray[position] + 1
		if freqArray[position] >= t:
			clump[position] = 1

	for i in range(sizeOfArray - 1):
		if clump[i] == 1:
			pattern = numberToPattern(i,k)
			freqPatterns.append(pattern)
	
	result = []
	end2 = len(freqPatterns[0])
	string = ("".join(str(x) for x in array))
	for i in range(0, end2,k):
		result.append(string[i:i+k])

	print(" ".join(str(x) for x in result))


def findClumpsSlow(genome, k, L, t):
	freqPatterns = []

	sizeOfArray = int(math.pow(4,k))
	clump = [None] * sizeOfArray 
	for i in range(sizeOfArray - 1 ):
		clump[i] = 0

	end = len(genome) - L
	for j in range(end):
		window = genome[j:j+L]
		freqArray = computeFreqs(window,k)
		for position in range(sizeOfArray - 1):
			if freqArray[position] >= t:
				clump[position] = 1

	for i in range(sizeOfArray - 1):
		if clump[i] == 1:
			pat2 = numberToPattern(i,k)
			freqPatterns.append(pat2)

	result = []
	end2 = len(freqPatterns[0])
	string = ("".join(str(x) for x in array))
	for i in range(0, end2,5):
		result.append(string[i:i+k])

	print(" ".join(str(x) for x in result))

def computeFreqs(text, k_mer):

	sizeArr = int(math.pow(4,k_mer)) 
	array2 = [None] * sizeArr
	for i in range(sizeArr):
		array2[i] = 0

	end = len(text) - k_mer
	for i in range(end + 1):
		pattern = text[i:i+k_mer]
		numberOfPattern = patternToNumber(pattern)
		array2[numberOfPattern] = array2[numberOfPattern] + 1

	#print(" ".join(str(x) for x in array))
	return array2

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
	
	if k_mer == 1:
		symbol = numberToSymbol(index)
		array.append(symbol)
		return 0 

	preIndex = index / 4
	remainder = index % 4
	symbol = numberToSymbol(remainder)
	prePattern = numberToPattern(preIndex, k_mer-1)

	array.append(symbol)
	return array

def numberToSymbol(position):
	if position == 0:
		return 'A'
	elif position == 1:
		return 'C'
	elif position == 2:
		return 'G'
	elif position == 3:
		return 'T'

#findClumpsFast('CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC', 5,75,4)
findClumpsFast('AGCGGAGATGAGCGAGTGATGGTAGGGACCGCGTTAACCCCCGCGCGTATAGTTAGTTGGTGGTTCTCCGCAAACTAATGCTTAAAAGTACCGGAGCTGACGGTCCGGGCCGCCTTTGTATGACTAACCTCTCTTTTTTACCCCAGCTTTTGTCGCAAGTAATAAACGTGGAAGTGGGTACCTGGCTTGTTGGGAGAGGGTAAGACCCCTAGGAGCGCAATCTACTGTCGCACATTCGCCACAGAATACAGTGCGATATCCCTCCGACTGTATGGCCCCCTAGGCGTCGTATATGGGTAGTCTACAATTTTTTGGCTAGAATATAAGGGGTCAGTGCTCGTTGTACTAGTTCACAAATATTCACCCTACTAGGAACGGACATCCTGTAACCTCTAGTTAGGTAGAACAAGTATGCCAAAAGCGCCGGAACACCGCCTAGTGAACGTCGCGAACGCAGTCGAGAATCGCGTGACCTAGATTGCTTGCCCTCCGCTTGTTCTCCCTAATTGCCCTCCGCTTAACTTGCCCTCCGCCTCCGAGTTGCCCTCCGCTCCGTCCTAAGTTGCCCTCCGTTGCCCTCCTTGCCCTCCGAAGAGTAGAGATTGCTCCTCTTGCTTGCCCTCCGCCATTGCTCCTCACTCATTGCTCTTGCCCTCCGCCGGCCACCGTCATTGCTCCTCTGCTCCTCATTGCTTGCCCTCCGGCCCTCCGGAAATCATCATTGCCCTCCGCCCTCCGTCCGTGTCTTTTGCCCTCCGCATTGCTCCTTTGCCCTCCGGAATATTGCTTTGCCCTTTGCCCTCCGCCGTCCGTTGCCCTCCGATCTAGCGAGCCTTGCCCTCCGCAGAAGTGATTGCCCTCCGATCGTGTTGCCCTTTGTTGCCCTCCGTGTGGGGTACCTAGCTGTATTGCTCCTCAGCGCGCAATTGCTCCTCGGCTCATTGCTCCTCGGCAGCTGTTGCCCTCCGATTGTTGCCCTCCGTCCTCGTGCATTGGATTTGATAGGCGTTATTGCATTGGATTGGATTTGATAATAGTTGCCCTCCGTAAGAGATTGCTCCTATTGCTCCTCACGCCGCGACCCGGCTGTCCCTAATACGTCGGATTTGATACCGCAGGTTTGACGTATCGACGATCCGGATTTGATATAGTCACGCCGGATTTGATAGGATTTGATAGGATTTGATATTTGATATTGAGGATTTGATATTAGGATTTGATAACCTTTCGCAGGTGTGCATAGTGGATTTGATATCCACTTTGACATGGAGGTCACACAAATGCGGCCGCTGTCAAGATGTCATGGATTTGATACTACGAGTACTAGCTGAGGATTTGATAAAGCGGGATTTGATATGTCCTGGATTTGATACAGGATTTGATAAGAGGAAGGTACAGCCGGGAAATCCAAGGATTTGATAAGGGATTTGATAATAATTTGATAATCCTAATAAGCGGGATTTGATAGTTCGATTGTATCCCCAGGGAATAAGTCCGGCCAGCTGCGTGGATTTGATATGGATTTGATATGATATTCTGGATTTGATATACGGATTTGATATTTGATAGCAAGTAATAAGGATTTGATACCGACATGCGAGTTGTGTTTAGCTTCAAGGGCCGGAAGGGCGGCTACCACTAACTATCCCGCACTCGGTTGACTGTAGACGCTAGTTTACCAGCAGTCTGATAAGTAACAGTTAAATAAGTGGCAGCGTTAATAAGGGATCTCCGCATCGCACGTATACAATGTCTAAAATTACTAGGGGCGACTTTTCGTTGGTGTTGTTGGACACGTGAGTACGTTGGCATCGCCGCCTAGGTGCAACTTGCAGAGCAAGATCTCTCAATAGCGACCGAGGTACATGATCACGTGTGTGTGCGTTGGACGTGATTTTACTCTGTCCTCTGGTCCACGCTTGGGTGTCCGTGTTCACTGTCTCCGCTTTCTGTCCGCCCGCCTGGGGCAAACGGGGGACGGCAGCGTTCCCGCGGGTAGCTCTAACGACAACTTGTGACAGATGGAGGATCAGCCAACAAGCCTATCATAGGAAGGAAGTCCGAGGTACGTGGTACCTCTACTGATATGTATTGACATACGTTGCGAAAATATATTTTGACAATGAAGAAAAAAATGGCCTGGGAATCAAAGCTGTGTTCAAGAACCCACTAATTTGGCACCTTGTAAATATCAAGCCACCAATCTAGCGTCCAAACTAGTCGGTCGGCGGTATCGGAAAGGAGTGGAAGTAACTGATCGGCCTTCTTGCTGTTACTAGTCAGTTGGTGTGGCACAATCTCTATGTTTATCAACGACCCAATTAGGACGGAAACACACCTGATGCCAGGGGGAATGCTTGGGAGGGTAAGATTAGACTCAGGCCGTTCTGCACCATAGTTCCGCTATTGAGAGCAAAAACCCCTCCACCCCGCCGAATATGAGAATTCCTCAGCAGCGTATTGAGTCTCCTTTCCCAAACCGTGTGCTTATACGGGTCATTGGTGGCTTGAATACAAGGAGGGCGATAACCTCTATAGCATCAGCTAGCCCCAACTAAGGCAAACGCCCTCAACATGAAAGAGAGCACCTGTACCGTGTGCACCACTTAGCGGTTAGTGGGATGTGCCTCAACCCTTCATTCGTGTCCTCTAGCGTAGGTTGCCCCTTCTTCTTTAGTGTCACTGACGGACCGTCTATTTCAGCTAACAACATTGATTCATGCACGATGGAGATTGGTCCTCATGCGCTTACAGGTGCCGGGCCCAGGACTCCGCACGCCACCCTTGGAGAAGATATAAGACTGACCGCTCGTCGTTTGTCACCGACATATTAATATTCGCTCGGCAACGTTAGCTAGGCGCGACTCCCACATTCATGTTGGGACCATTCACGCCCATAACACACGATAAGAGATGATCTAGACTGAGGCCGTCGCCGGAACCGAAGTGCTCAGTGGAGTCCTACGATGTCAACACTGGCGCCAGGATGAACCACGAACTTCCCCGGCCGTGAAACTGATCTATCGAGACGGGTATATATCCATCGGCCAACTTGCGCTAGGTTGCACGCTGCAATCACCCTCAAGTGCCTGACGCACACCCCACCCTCAAGGTTACTCGGCCACCCTCAAGTCAAGTACCCGAGCAAAATAGTCACGCCACCCTCAAGTCCCGACTCGAAGAAGACTTCACCCTCACACCCTCAAGCAATAGTTGATTTAATGCCCCTTATAATAAGACACCCTCAAGGAGTCGTTAATCCCTACGCTCACCCTCAAGTCGCCCACCCTCAAGAGACCCTCAAGCAGCACCCTCAAGGTAGCACCCTCAACACCCTCAAGTCCACCCTCAAGCACCCTCAAGTCGACGCACCCTCAAGTGCAACCTGTTATAGTTCTGTTATCACCCTCAAGCACCCTCAAGCAGTCGTCGATTGACCGTTTACATCATGAACCGCACCCTCCACCCTCAAGCCCTCAAGCTTAGTACAACACCCTCAAGGATATAGTGGCAGTTCGATAAACACGTGGCACGCGGGTCAACGAGCACCCACCCTCAAGTTTGCCGATAGCCTAGATTAGAACACCCTCAAGAAGCACCCTCAAGACCACCCTCCACCCTCAAGTGTGCACCCTCAAGCAACTCGCTACACCCTCAAGCTTGCCCGGCCCGATCGTATGTCTCGTCAAATAGCGCCGAATATCAGACTATTTATCAAAGTGATTTTCCACTGAGCGCGTGCATATGGACGTTGACGAAGGCGTATCGCGTCCGTGATCGCGCGTTTCTAGTTGCAACCGTCACTACCCCCCGCAGTAATGCTCATAGCTAGAAATCCGGTACTACAACGTATGTGGCTGAGAGCTCGATAGCCTCCAGTTCCGAGTAGTTATCTCTAGTACCGAATGGCGGGGCTTTACAGTCGACCCGGTCTTCGGGAACAGGTACGAATCATCTACACCCGGCCGAAGGTGTAGATAGTGCACGCCTGTTGAGACAATCGGCCTTCATGTTTGTTGCTCTGTTGCCCCGCAGATCCTAGGAGTGGGCTTGGTCCTGCACCAAGAAATGGGTCTCTCCGGAGTGTCATTCACCGTATCAAAAGGGTCTCAATACACCCGCTCGGTCACGGAGCCGAGAATTTTGTAGGTAAAAGAGATAGTAAAAGAGAAAAAGAGAGGAACTCCCGGCCGTGGCTATTAACTACCGTGGTATTGTAAAAGAGAGGAACATGCAATTATGACTACTTTTCTCGATTGTAAAAGAGAGGGCTATCGTACACTCCTATACGTAAAAGAGAACGGGACGGTGTGTAAAAGTAAAAGAGAAGAGAATATGCGGTAAAAGAGACACGGAGTAAAAGAGACTACTTTGGTTGCAGCATCCGTTCGTGATCTGAACGTAAAAGAGAAGATGGAAGTAAAAGAGAGTAAAAGAGACAAGTTTTATCCTATCAGAGGACGAGAGTAAAAGAGGTAAAAGAGACCAGTCGAGACCGGTAAAAGAGACGTAGTAAAAGAGAAGATCGGTAAAAGAGAGAATGATACAACTACCGTGCGATAGTAGTAAAAGAGAAAAGAGAGAGAGAGGTAAAAGAGAGTCGTCGGAGGCAGCTTTGAAAGGTAAAAGAGATTGTAAAAGAGAAAAGAGATCTGTAGCGCCAGACGTAAAAGAGATCGTTGTAAAAGAGAATTATTGCGATGTCACGTAAAAGAGAAATCATTTGCGTTCATCGATCGTCGGAGACGCGTCCAGCGGTTGTGGATGCGCTCCTGCTCTAGGAGGGAGCATGGTCTGGACATGTAGAGATGTAAGACGTAAGAAACGTAAGACCTAAGACCAGACGTAAGACCGAAATACGTAAGACCGCGTCGAGCCCCGCCACGTAAGACCTTCTCGTTCTGAAAAACGTAAGACCACACTTATACTCTAAAATGGGGAATCGGAGTACCTACGTAAGACCAGAAGTGTACGCGTGGGGTCAATGATAACAATCGGCCCCCGCGACGTAAGACGTAAGACCGGATGCTGACAGCATAGTTAGACCCGACGTAAGACCCAAAATGGGGGTGCGACGTAAGACCTTACGTAAGACCAAGACCACCTAACGTAAGAACGTAACGTAAGACCGAGACGTAAGACGTAAGACCAGCGACGTAAGACACGTAAGACACGTAAGACCATTACGTAAGACCACATCTTGCTGTACATCCCGCAAGTTCACGTAAGACCTAAGAACGTAAGACCTAAACACCTAAACGTAAGACCAAACAGTCATGGGTGTTAGGTGAGTACGTAAACGTAAGACCGTTAACGTAAGACCCCACAATGATGGACAACCTTTATTCGAATCGGACGTAAGACCGTAACGTAAGACCCAGGAAACGGATTAACTGACAGACCGGCAGCTGTAGGCAGGGAGTTCACTAGTAGAGGAAATACAGGGGACTCTCTAACGTCCTACGACGCACATCCTAGTATCAATTTCGCGCGCTCCCCATTGCAGTACTCTACTAGTTAAATGAGCATCAGGTGTACCATACCACCTAAAACGCTTACCACCTAACCTACTCGCGGTTGCGACTACCACCTACCACCTAACTAAAGAACTAACCGTCTGGGTCCTTTAATCTATATCAGAGCACAGGAGTTTGTCTTACCACCTAAGTGAGTACCACCTAATATCGTACCACTACCACCTAAGCGACAGTATACCACCTAATAATTTTCACGCATTTGACTACCACCTAAACCTAAAGTACTACCACCTAAGTGATACCACCTAAAACCACCTAAAAATGACCACTGGAGGTGTCGCGTCTTGGCATTATACCACCTAACCAGTATTTCGTACGTAACCCAAATACAGTGTACCACCTAACATTGCGCAGACTCTACCACCTAAGCTTAAGGAAACCTACTAGTACCACCTACCACCTAAAAAGTACCACCTAAGGACTATTACTGAGTACCACGTACCTAGGCGTACCTAGGCCACGTACCTCGTACGTACCTAGGACAGTACGTACCTAGGATTCGTACCTAGGGACCTAGGGTACGTACCTAGGTAGGCCTAGGGCCTCTCCCATTACGTACCTAGGCCACCTAACTGGGGTTCTATATGGAATGGGCTCTAATTTGACTGGTCGTACCTAGCGTACCTAGGCACCGGGCGTACCTAGGCGCCACTCTGAGACAACCGTACCTAGGGTAATCACGCTGTAACTCGTACCTAGGCTGGACGCAGGCACCGTTTCAACCAAAGTATACCACCGTACCTAGGTATCTCACACGACGGCTGGTTACGTACCTAGCGTACCTAGGGTGCGATGTATCGCTATATGATGCTCCGGAGCGTACCGTACCTAGGGGTTCTGCTTAAGGCTCATTAGTCGTACCTAGGAGAACGCCACTAATTGTTAACGTCCGCGTACCTAGGTAGGCGTACCTAGGAGGATCGTACCTCGTACCTAGGATGTAATTCTTTTCTCGTACCTAGGATTGCTCTTCATGCGTACCTAGGGTGCACTAGTGCTCTCCTAAAGGCTTAATGGTTTAATCACGACTCTTATACGCAGGCTAGACACCTCTCCATCAAACACCTCGGTGAACCCGGTGTATAAGTCTTCGTTTAACTCGGATGGTTTGTGGTCCGCAACCAGGGCGAATCGCCTATCCCGTGACGTACACGATCCTCAAGGGGACACGGGCCGGCTCTCATCCGGCTCTCACTCCGGCTCTCCGGCTCCGGCTCTCAGATGGTACTCGATGGTACTCAAGGATGGTACTCCTGCAGTTTTAGATGCCGGCTCTCATACATCCGATTGTCATCTCACTCCGGCTCTCACCCGACCGATTGTCAGCAACTTGCCTCGGCCGATTGTCACCCGATTGTCATCACCCCGATTGTCATTGTCATCCGATTGTCATCAAACCGGCTCTCAACTCACACCCCCGATTGTCACTCGTTCCGATTGTCAAGTCAGTTGATGGTCCGCCGATTGTCACTCATGGTCCGGCCCGGCTCTCAGTTCCGATTGTCACCGATTGTCATCTACTCCAGCCGGCTCTCACCGGCTCTCAGCTCTCAACTCTACTCGACCGGCTCTCAACACCGGCTCTCACACCGATTGTCATTGTCATACCCGATTGTCAGATTCCGATCCGATTGTCACAACTCTTCCGATTGTCACTCCGATTGTCAATTGTCACCCGATTGTCAGATTGTCAGCTCCGGCCGATTGTCACACTCTCAAACCCGATTGTCAGATGGTCCGATTGTCACAAGTTTTACATACAGTGACCCGATTGTCAGTTTTACACGATGGTACTCTGGTACCGACCGACCGATTGTCAAGTTTTACAGCGTGCCCGATTGTCAGCACGGCCGGTCCCGTATTTGATCGCACGGCCGGGTGCCGCACGGCCGCGCACGGCCGGCGCACGGCCCGCACGGCCGTCACCTCTAGGTGTTAAGTATGAGACGCCCCTCATCGCACGGCCGCACGGCCGGTGATCAGATCTTCTTGCCGCACGGCCGCACGGCCGCCGAAGACTTCGTATTCTTAACGCACCGCACGGCCGACTATATATGCCAGCAGAAGGGATCCCGGGTGCCGCACGGCCCGCACGGCCGGTGCTCTAACGGGCAGATAGAGTTGGCGCACGGCCGGAGACCCGCACGGCCGGAGGCTCAATTCCGCCGCACGGCCGCGGGGCGGAATCAGGGTAGCACGGTTTGCTTGTCTTGGGAGGCTATAGGTCACGATTCCCCTACGCACGGCCGCGCACGGCCGGAACGCACGGCCGCACGGCCGACGGCCGGCCGCCCGCACGGCCGAGTCGTGTCGCACCGCACGGCCGATGCGCAAGGGTTCAGAACGCACGGCCGCACGGCCGCACGGCCGACCTGGAAGTACCAGTTAGGACACAGCGGTGAGGTACGGAGAGCATGAACGAGTCTACGTTCGTGATGCGAGCTCATCCCAAAAAGATACACCGAGATGAGATCGCCTGTTCCTGGCATTTACCAGAGCGCAGCGATTTCGTCCTCAACAAATCACTTATTACGCGTATCGCGTATACTGAGGGCTCGAGGCGGCGTGTATCGCCCCTGGGGTGTGCGCCTGGCGGACCCTCAAGACCGTCCGTATATTACCTTCTGTGGAGGGTAACCAATACCTGTAGTACGGTTCACAAGTTCATATTGTTCTTTGATGACGTGGGCAAGCGCGCAAAGGTATGAACTAATAGAAATAAGGCAACGGTAGGTGTAATCCATCACATGAGCATATGCCACGCGTATACTAGTGGATATCCCAACCGGGCGTTACGGCTTAGCTCGTATCAACCTCGACCAAGGCGTTTAGGGTGTCTGCTGAGTAACCCGTAAGATCGGTGGCGGTGAACAGGGGTTCAGCCTAGGATAAAACTTTTGAGAACACGTTCCACTGGTCACGCCGCGAGGCGATGATTCTAGGTCGAAGATTGGGGTGTGGGGTTAACAGTAGCGACATTCCAAGATCTTCCGGGCCCCCTAGGCTTTAAGTCTTCGGGTTAGAGATTCATTTGTGGCCATACGACGCGCAGCCTAGCGAGGAAATCGCATTCCAACAGACGCTTGTTATCGGAGCAGAACGGTGACCCTTCAAAGTTGCTCGTGGCGTACGAATACTATTTGTGATTTCGACACCATCCCACACTAGCCAGCACTCTTCCCCCCGCGGTTATCCGAACGCTGCTGAAAGTCGACTTTCGCGCCCGCGAGTAGCCTCGTTGCAGATCAATGTTTGGCGGGCGGGGAACTCTGGTGCCCAGTAGGTTCAACACCATTTTCGGATTAAGGAAAGCTAGGACCCTCGGATTGTGCTTCGCACCGTCATGTCCGTGGAGGACTCGTATATCCTCGTGGCCTCTATGAAACCTCTAACCTGGTGTGCTCCATCACTGGGGCTGAAGACAAAGCCTGGCAGATCACGGTTGTTTCATAAAAGAAGTGTCGTAGTACTATAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTAGCGCCTACTCTCAACACGTAGCGCCTACTAGCGCCTACTAGCCTCAACACTCAACACGTCTCAACACGTAGCGCCTACTAGCGCTCAACACGTCCTACTAGCGCCTACTAGCGCCCTCAACACGTTACTAGCGCCCTCAACACGTCACGTGCTCAACACGTTGCCTACTAGCGCCCTCAACCTCAACACGTCGCCTACTAGCGCCTACTAGCGCCTACTACTCAACACGTCAACACGTCTCAACACGTAACACGTCTCAACACGTCGTCTCAACCTCAACACGTACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGTCTCAACACGT', 10, 552, 19)