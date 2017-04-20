import sys

def find(string1, string2):

	minAt = min(len(string1), len(string2))
	for j in range(minAt):
		if string1[j] != string2[j]:
			x = string1[:j]
			return x

	return string1[:]


def longest(text):
	longest = []

	for i in range(len(text)):
		longest.append(text[i:] )
	
	longest.sort()
	longestString = ''

	for i in range(len(text)-1):
		x = find(longest[i], longest[i+1])
		if len(x) > len(longestString):
			longestString = x

	print longestString


filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)

string = array[0]

result = longest(string)
