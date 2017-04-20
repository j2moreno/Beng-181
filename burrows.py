import sys

def burrowsTrans(text):
	cyclic = []

	for i in range(len(text)):
		word = text
		word = word[i:] + word[:i]
		cyclic.append(word)

	cyclic.sort()
	BWT = []
	for element in cyclic:
		BWT.append(element[len(element)-1])

	print("".join(str(x) for x in BWT))

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

string1 = data[0]

burrowsTrans(string1)