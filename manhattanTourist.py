import sys

def manHat(n,m, Down, Right):
	matrix = [[0 for x in range(m+1)] for y in range(n+1)]
	
	for i in range(1,n+1):
		matrix[i][0] = matrix[i-1][0]+ Down[i-1][0]
	
	for j in range(1,m+1):
		matrix[0][j] = matrix[0][j-1] + Right[0][j-1]

	for x in range(1,n+1):
		for y in range(1,m+1):
			matrix[x][y] = max(matrix[x-1][y] + Down[x-1][y], matrix[x][y-1] + Right[x][y-1])
	
	return matrix[n][m]


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

downArray = []
rightArray = []

indexOfDash = 0
for element in array:
	if element == "-":
		indexOfDash = array.index(element)
		break
	temp = []
	for i in element:
		if i != " ":
			temp.append(int(i))

	downArray.append(temp)

end = indexOfDash
while end < len(array):
	end += 1
	for element in range(indexOfDash+1, len(array)):
		temp = []
		for i in array[element]:
			if i != " ":
				temp.append(int(i))

		rightArray.append(temp)
	break

result = manHat(12,15,downArray,rightArray)
print result