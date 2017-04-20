import sys

def stringComposition(text, k):
	Comp = []
	for i in range(len(text) - k ):
		k_mer = text[i:i+k]
		if k_mer not in Comp:
			Comp.append(k_mer)

	Comp.sort()
	return Comp


filename = sys.argv[1]
file = open(filename, 'r')
string = file.read()

result = stringComposition(string,50)
print("\n".join(str(x) for x in result))
