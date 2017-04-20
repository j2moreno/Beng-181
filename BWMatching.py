import sys
import collections

def burrows(text):
	
	lastColumn = []
	T = 0
	C = 0
	A = 0
	G = 0
	for letter in text:
		if letter == 'T':
			lastColumn.append(letter + str(T))
			T +=1
		elif letter == 'C':
			lastColumn.append(letter + str(C))
			C +=1
		elif letter == 'G':
			lastColumn.append(letter + str(G))
			G +=1
		elif letter == 'A':
			lastColumn.append(letter + str(A))
			A +=1
		else:
			lastColumn.append(letter + '0')
	
	array = []
	for letter in text:
		array.append(letter)

	array.sort()
	firstColumn = []
	T = 0
	C = 0
	A = 0
	G = 0
	for letter in array:
		if letter == 'T':
			firstColumn.append(letter + str(T))
			T +=1
		elif letter == 'C':
			firstColumn.append(letter + str(C))
			C +=1
		elif letter == 'G':
			firstColumn.append(letter + str(G))
			G +=1
		elif letter == 'A':
			firstColumn.append(letter + str(A))
			A +=1
		else:
			firstColumn.append(letter + '0')
	
	return firstColumn, lastColumn

def BWMatch(text, firstColumn, lastColumn, pattern):
	top = 0
	bottom = len(lastColumn) - 1

	while top <= bottom:
		
		if pattern != '':
			symbol = pattern[len(pattern)-1]
			pattern = pattern[:-1]
			if symbol in text[top:bottom+1] :
				topIndex = top + text[top:bottom+1].index(symbol)
				bottomIndex = bottom - text[top:bottom+1][::-1].index(symbol)
				top = firstToLast(lastColumn,firstColumn,topIndex)
				bottom = firstToLast(lastColumn, firstColumn, bottomIndex)
			else:
				return 0
		else:
			
			return bottom - top + 1
	

def firstToLast(last,first, index):
	return first.index(last[index])


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().split(' ')

data2 =  data[0].split('\n')

for i in range(1,len(data)):
	data2.append(data[i])



pats = []
for j in range(1, len(data2)):
	pats.append(data2[j])

string = data2[0]

result = []
first, last = burrows(string)
for element in pats:
	toAdd = BWMatch(string, first, last, element)
	result.append(toAdd)

print(" ".join(str(x) for x in result))


