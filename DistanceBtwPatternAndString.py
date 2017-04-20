import sys

def distBtwPatternString(pat,DNA):
	k = len(pat)
	distance = 0
	for element in DNA:
		HamDist = float("inf")
		for i in range(len(element) - k):
			pattern2 = element[i:i+k]
			if HamDist > HammingDistance(pat,pattern2):
				HamDist = HammingDistance(pat,pattern2)
		distance = distance + HamDist

	return distance

def HammingDistance(first,second):
	hammingDist = 0
	for i in range(len(first)):
		if first[i] != second[i]:
			hammingDist += 1
		continue
	return hammingDist

filename = sys.argv[1]
file = open(filename, 'r')
data = file.readline().split(" ")
array = []

print distBtwPatternString('CAAGTA', data)