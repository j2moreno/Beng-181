import sys
import collections

def createSuffixArray(text):
	splitArray = dict()

	for i in range(len(text)):
		splitArray[text[i:]] = i

	
	newDict = collections.OrderedDict(sorted(splitArray.items()))
	

	result = []
	for element in newDict.values():
		result.append(element)

	return result

def matching(text, pattern, suffixArray):
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


for i in range(1, len(data)):
	array.append(data[i])

result = createSuffixArray(string1)

result2 = []
for element in array:
	answer = matching(string1, element, result)
	result2.append(answer)

array3 = []
for element in result2:
	for element2 in element:
		array3.append(element2)
array3.sort()
print(" ".join(str(x) for x in array3))




