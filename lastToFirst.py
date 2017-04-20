import sys


def burrowsPosition(text, number):
	
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
	
	print firstColumn.index(lastColumn[number]) 


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()


string1 = data[0]

burrowsPosition(string1,497)
