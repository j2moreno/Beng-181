import sys

def trieConst(patterns):
	root = dict()
	root[0] = {}
	counter = 0
	struct = []
	for element in patterns:
		currDict = root[0]
		for letter in element:
			currDict = currDict.setdefault(letter, {})
		currDict['$'] = '$'	
		
	return root

def preMatch(text, pattern):

	positions = []
	kmer = len(pattern)
	for i in range(len(text)-kmer+1):
		
		if text[i:i+kmer] == pattern:
			positions.append(i)

	return positions


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

string1 = data[0]

array2 = []
for element in range(1,len(data)):
	array2.append(data[element])


trieToPass = trieConst(array2)
result2 = []
for element in array2:
	answer = preMatch(string1, element)
	result2.append(answer)

array3 = []
for element in result2:
	for element2 in element:
		array3.append(element2)
array3.sort()
print(" ".join(str(x) for x in array3))