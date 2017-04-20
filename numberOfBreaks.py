import sys

def breaks(P):
	numberOfBreaks = 0
	for i in range(len(P) -1):
		if P[i]+1 != P[i+1]:
			numberOfBreaks += 1 
	print numberOfBreaks

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
	line = line.strip('(')
	line = line.strip(')')
	array.append([int(x) for x in line.split()])

seqArray = []
for element in array:
	for element2 in element:
		seqArray.append(element2)


result = breaks(seqArray)