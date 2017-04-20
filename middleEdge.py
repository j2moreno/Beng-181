import sys

def middle(v,w,score):

	matrix = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
	
	for i in range(1, len(v) +1):
		matrix[i][0] = -5*i

	for j in range(1,len(w) +1):
		matrix[0][j] = -5*j

	for i in range(1,len(v) +1):
		for j in range(1,len(w)/2 +1):
			
			index = alphatbet.index(w[j-1])
			temp =  matrix[i-1][j-1] + int(score[v[i-1]][index+1])
			matrix[i][j] = max(matrix[i-1][j]-5, matrix[i][j-1]-5,temp)
			

	array = []
	array2 = []
	for i in range(len(v)+1):
		array.append(matrix[i][len(w)/2])
		array2.append(matrix[i][len(w)/2-1])

	middleEdge1 = max(array)
	middleEdge2 = max(array2)

	for i in range(len(v)+1):
		if matrix[i][len(w)/2] == middleEdge1:
			position = i
			middle = len(w)/2 +1

		if matrix[i][len(w)/2-1] == middleEdge2:
			position2 = i
			middle2 = len(w)/2
	
	middleEdge1 = position+1, middle
	middleEdge2 = position2+1, middle2
	
	return middleEdge2, middleEdge1



#blosum file read 
filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []
alphatbet = ['A','C','D','E', 'F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']

for line in data:
	array.append(line.split(" "))

scoreMatrix = dict()

for i in range(1,len(array)):
	letter = array[i][0]
	for element in array[i]:
		if element == "":
			continue
		if letter not in scoreMatrix.keys():
			scoreMatrix[letter] = [element]
		else:
			scoreMatrix[letter].append(element)

#Reads 2 strings from file
filename = sys.argv[2]
file = open(filename, 'r')
data = file.read().splitlines()
array2 = []

for line in data:
	array2.append(line.split(" "))

string1 = array2[0][0]
string2 = array2[1][0]

result, result2 = middle(string1,string2, scoreMatrix)

print result, result2

