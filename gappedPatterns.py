import sys

def reconstruction(k_strings):
	recon = [k_strings[0]]
	
	for element in k_strings:
		if element == k_strings[0]:
			continue
		recon.append(element[len(element) - 1])

	return recon

def stringSpelledGapPat(first,second,k,d):
	prefix = reconstruction(first)
	suffix = reconstruction(second)

	for i in range(k+d+1:len(prefix)):
		if prefix[i] != suffix[i-k-d]:
			return "No string!"
	return prefix + suffix[k+d:]


filename = sys.argv[1]

patternA = []
patternB = []
with open(filename) as file:
	for line in file:
		toAdd = line.split('|')[0]
		print toAdd
		toAdd2 = line.split('|')[1].rstrip()
		
		patternA.append(toAdd)
		patternB.append(toAdd2)

result = stringSpelledGapPat(patternA, patternB,4,2)
print result
