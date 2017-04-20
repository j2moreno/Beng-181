import sys


def align(v,w,scoreMatrix2,sig,epsi):

	matrixSol = [[[0 for i in range(len(w)+1)] for j in range(len(v)+1)] for x in range(3)]
	back = [[[0 for i in range(len(w)+1)] for j in range(len(v)+1)] for x in range(3)]

	for i in range(1,len(v) +1):
		matrixSol[0][i][0] = -sig - (i-1)*epsi
		matrixSol[1][i][0] = -sig - (i-1)*epsi
		matrixSol[2][i][0] = -sig - (i-1)*epsi

	for j in range(1,len(w)+1):
		matrixSol[0][0][j] = -sig - (j-1)*epsi
		matrixSol[1][0][j] = -sig - (j-1)*epsi
		matrixSol[2][0][j] = -sig - (j-1)*epsi

	for i in range(0,len(v)+1):
		back[1][i][0] = 1
	for j in range(0,len(w)+1):
		back[1][0][j] = 1
	for i in range(0,len(v)+1):
		back[2][i][0] = 2
	for j in range(0,len(w)+1):
		back[2][0][j] = 2


	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			#lower
			score = [matrixSol[0][i-1][j] - epsi, matrixSol[1][i-1][j]-sig]
			matrixSol[0][i][j] = max(score)
			back[0][i][j] = score.index(matrixSol[0][i][j])
			
			#upper
			score = [-float("inf"), matrixSol[1][i][j-1]-sig,matrixSol[2][i][j-1] - epsi]
			matrixSol[2][i][j] = max(score)
			back[2][i][j] = score.index(matrixSol[2][i][j])

			#middle
			index = alphatbet.index(w[j-1])
			score = [matrixSol[0][i][j], matrixSol[1][i-1][j-1] + int(scoreMatrix2[v[i-1]][index+1]),matrixSol[2][i][j]] 
			matrixSol[1][i][j] = max(score)
			back[1][i][j] = score.index(matrixSol[1][i][j])

	bestScoreFromMatrix = [matrixSol[0][i][j],matrixSol[1][i][j], matrixSol[2][i][j]]
	score = max(bestScoreFromMatrix)
	backIndex = bestScoreFromMatrix.index(score)
	print score
	outputAlignment(back,v,w,len(v),len(w),backIndex)
	

	return 0


def outputAlignment(backTrack, v,w, i ,j, nextLevel):
	if i == 0 or j == 0:
		print v
		print w
		return 0
	
	
	if nextLevel == 0:
		#print "lower"
		if backTrack[0][i][j] == 1:
			nextLevel = 1

		w = w[:j] + '-' + w[j:]
		outputAlignment(backTrack,v,w,i-1,j,nextLevel)

	elif nextLevel == 2:
		#print "upper"
		if backTrack[2][i][j] == 1:
			nextLevel = 1
		v = v[:i] + '-' + v[i:]
		outputAlignment(backTrack,v,w,i,j-1,nextLevel)

	elif nextLevel == 1: 
		#print "middle"
		if backTrack[1][i-1][j-1] == 0:
			nextLevel = 0

		elif backTrack[1][i-1][j-1] == 2:
			nextLevel = 2

		outputAlignment(backTrack,v,w,i-1,j-1,nextLevel)





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

align(string1,string2,scoreMatrix, 11, 1)