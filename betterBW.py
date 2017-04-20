import sys

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

def BWMatch(text, occurDict, lastColumn,firstColumn, pattern, COUNT):
	top = 0
	bottom = len(lastColumn) -1

	while top <= bottom:
		
		if pattern != '':
			symbol = pattern[len(pattern)-1]
			pattern = pattern[:-1]
			if symbol in text[top:bottom+1] :

				if symbol == 'A':
					top = occurDict[symbol] + COUNT[top][1]
					bottom = occurDict[symbol] + COUNT[bottom+1][1] -1
				elif symbol == 'C':
					top = occurDict[symbol] + COUNT[top][2]
					bottom = occurDict[symbol] + COUNT[bottom+1][2] -1
			
				elif symbol== 'G':
					top = occurDict[symbol] + COUNT[top][3]
					bottom = occurDict[symbol] + COUNT[bottom+1][3] -1
		
				elif symbol == 'T':
					top = occurDict[symbol] + COUNT[top][4]
					bottom = occurDict[symbol] + COUNT[bottom+1][4] -1
			
				else:
					top = occurDict[symbol] + COUNT[top][0]
					bottom = occurDict[symbol] + COUNT[bottom+1][0] -1
			
				
			else:
				return 0
		else:
			
			return bottom - top + 1
	

def firstToLast(last,first, index):
	return first.index(last[index])

def count(lastColumn):
	countArray = []

	T = 0
	C = 0
	A = 0
	G = 0
	dollar = 0
	countArray.append([dollar, A,C,G,T])
	for i in range(len(lastColumn)):
		
		if lastColumn[i] == 'T':
			T += 1
			countArray.append([dollar,A,C,G,T])
		elif lastColumn[i] == 'C':
			C +=1
			countArray.append([dollar,A,C,G,T])
		elif lastColumn[i] == 'G':
			G+=1
			
			countArray.append([dollar,A,C,G,T])
			
		elif lastColumn[i] == 'A':
			A+=1
			countArray.append([dollar,A,C,G,T])
		else:
			dollar +=1
			countArray.append([dollar,A,C,G,T])
			
	return countArray


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
count = count(string)

occurance = dict()
firstList = ''.join(sorted(string))
occurance['$'] = firstList.find('$')
occurance['A'] = firstList.find('A')
occurance['C'] = firstList.find('C')
occurance['G'] = firstList.find('G')
occurance['T'] = firstList.find('T')



for element in pats:
	answer = BWMatch(string, occurance, last,first, element, count)
	result.append(answer)

print(" ".join(str(x) for x in result))





