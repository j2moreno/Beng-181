import sys
sys.setrecursionlimit(10000)

def lcsBack(v,w):
	matrix = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]
	back = [[0 for x in range(len(w)+1)] for y in range(len(v)+1)]

	for i in range(1,len(v)+1):
		for j in range(1,len(w)+1):
			if v[i-1] == w[j-1]:
				temp =  matrix[i-1][j-1] + 1
				matrix[i][j] = temp
			else:
				matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

			
			if matrix[i][j] == matrix[i-1][j]:
				back[i][j] = 'down'
			elif matrix[i][j] == matrix[i][j-1]:
				back[i][j] = 'right'
			elif matrix[i][j] == matrix[i-1][j-1] + 1 and v[i-1] == w[j-1]:
				back[i][j] = 'diagonal'
	
	return back

def outputLCS(backTrack, v, i ,j):
	if i == 0 or j == 0:
		return 0
	if backTrack[i][j] == 'down':
		outputLCS(backTrack, v, i-1 ,j)
	elif backTrack[i][j] == 'right':
		outputLCS(backTrack, v, i, j-1)
	else:
		
		outputLCS(backTrack, v, i-1, j-1)
		LCS.append(v[i-1])
		

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

string1 = array[0]
string2 = array[1]


result = lcsBack(string1,string2)
LCS = []
result2 = outputLCS(result, string1, len(string1), len(string2))
print("".join(str(x) for x in LCS))

