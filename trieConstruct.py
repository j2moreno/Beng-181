import sys


def trieConst(patterns):
	root = dict()
	root[0] = {}
	counter = 0
	struct = []
	for element in patterns:
		currDict = root[0]
		for letter in element:
			if letter in currDict:
				currDict = root[currDict[letter]]
				
			else:
				counter += 1
				root[counter] = {}
				newNode = root[counter]
				currDict[letter] = counter
				currDict = newNode
				

	result = dict()
	print root
	
	for key, value in root.items():
		print key,value
		for key2,value2 in value.items():
			print str(key) + '->' + str(value2) + ':' + str(key2)
			
		

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

trieConst(array)

