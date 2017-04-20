import sys

def shared(k, dna1, dna2):
	
	dictionary = dict()

	for i in range(len(dna1) - k +1):
		pattern = dna1[i:i+k]

		if pattern in dictionary:
			dictionary[pattern].append(i)
		else:
			dictionary[pattern] = [i]


	for i in range(len(dna2)-k+1):
		pattern2 = dna2[i:i+k]
		reverse = reverseComp(pattern2)

		if pattern2 in dictionary:
			for element in dictionary[pattern2]:
				print '(' + str(element) + ', ' + str(i) + ')'

		if reverse in dictionary:
			for element in dictionary[reverse]:
				print '(' + str(element) + ', ' + str(i) + ')'


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


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

string1 = array[0]
string2 = array[1]

shared(15,string1, string2)