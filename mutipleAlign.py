import sys

def alignMutiple(v,w,x):
	matrixSol = [[[0 for i in range(len(x)+1)] for j in range(len(w)+1)] for k in range(len(v)+1)]
	back = [[[0 for i in range(len(x)+1)] for j in range(len(w)+1)] for k in range(len(v)+1)]
	
	for i in range(1,len(v)+1):
		back[i][0][0] = "1"
		for j in range(1,len(w)+1):
			back[0][j][0] = "2"
			back[i][j][0] = "3"
			for k in range(1,len(x)+1):
				back[0][0][k] = "4"
				back[i][0][k] = "5"
				back[0][j][k] = "6"
				

	for i in range(1, len(v)+1):
		for j in range(1, len(w)+1):
			for k in range(1, len(x)+1):
				if v[i-1] == w[j-1] == x[k-1]:
					scores = [matrixSol[i-1][j][k], matrixSol[i][j-1][k], matrixSol[i][j][k-1],matrixSol[i-1][j-1][k], matrixSol[i-1][j][k-1], matrixSol[i][j-1][k-1], matrixSol[i-1][j-1][k-1]+1]
					matrixSol[i][j][k] = max(scores)
					
				else:
					scores = [matrixSol[i-1][j][k], matrixSol[i][j-1][k], matrixSol[i][j][k-1],matrixSol[i-1][j-1][k], matrixSol[i-1][j][k-1], matrixSol[i][j-1][k-1], matrixSol[i-1][j-1][k-1]]
					matrixSol[i][j][k] = max(scores)


				if matrixSol[i][j][k] == matrixSol[i-1][j][k]:
					back[i][j][k] = "1"
				elif matrixSol[i][j][k] == matrixSol[i][j-1][k]:
					back[i][j][k] = "2"
				elif matrixSol[i][j][k] == matrixSol[i][j][k-1]:
					back[i][j][k] = "4"
				elif matrixSol[i][j][k] == matrixSol[i-1][j-1][k]:
					back[i][j][k] = "3"
				elif matrixSol[i][j][k] == matrixSol[i-1][j][k-1]:
					back[i][j][k] = "5"
				elif matrixSol[i][j][k] == matrixSol[i][j-1][k-1]:
					back[i][j][k] = "6"
				else:
					back[i][j][k] = "7"
	


	maxScore = matrixSol[i][j][k]
	print maxScore
	outputAlign(v,w,x,len(v),len(w),len(x),back)

def outputAlign(v,w,x,i,j,k,backTrack):
	if i == 0 and j == 0 and k == 0:
		print v
		print w
		print x
		return 0

	if backTrack[i][j][k] == "1":
		w = w[:j] + '-' + w[j:]
		x = x[:k] + '-' + x[k:]
		outputAlign(v,w,x,i-1,j,k,backTrack)

	elif backTrack[i][j][k] == "2":
		v = v[:i] + '-' + v[i:]
		x = x[:k] + '-' + x[k:]
		outputAlign(v,w,x,i,j-1,k,backTrack)

	elif backTrack[i][j][k] == "4":
		v = v[:i] + '-' + v[i:]
		w = w[:j] + '-' + w[j:]
		outputAlign(v,w,x,i,j,k-1,backTrack)

	elif backTrack[i][j][k] == "3":
		x = x[:k] + '-' + x[k:]
		outputAlign(v,w,x,i-1,j-1,k,backTrack)

	elif backTrack[i][j][k] == "5":
		w = w[:j] + '-' + w[j:]
		outputAlign(v,w,x,i-1,j,k-1,backTrack)

	elif backTrack[i][j][k] == "6":
		v = v[:i] + '-' + v[i:]
		outputAlign(v,w,x,i,j-1,k-1,backTrack)

	else:
		outputAlign(v,w,x,i-1,j-1,k-1,backTrack)
	


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line.split(" "))

string1 = array[0][0]
string2 = array[1][0]
string3 = array[2][0]


alignMutiple(string1,string2,string3)
