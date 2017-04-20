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

	print(", ".join(str(x) for x in result))


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

string = array[0]

createSuffixArray(string)