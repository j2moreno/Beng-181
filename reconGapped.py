import sys

def reconstruction(k_strings):
	recon = []
	
	for element in k_strings:
		recon.append(element[0])

	pat = k_strings[len(k_strings) - 1]
	recon.append(pat[1:])
	recon = "".join(str(x) for x in recon)
	return recon

def stringSpelledGapPat(first,second,k,d):
	prefix = reconstruction(first)
	suffix = reconstruction(second)

	for i in range(k+d+1, len(prefix)):
		if prefix[i] != suffix[i-k-d]:
			return "No string!"
	return prefix + suffix[len(suffix) - k-d:]


filename = sys.argv[1]

patternA = []
patternB = []
with open(filename) as file:
	for line in file:
		toAdd = line.split('|')[0]
		toAdd2 = line.split('|')[1].rstrip()
		
		patternA.append(toAdd)
		patternB.append(toAdd2)

result = stringSpelledGapPat(patternA, patternB,50,200)
print("".join(str(x) for x in result))