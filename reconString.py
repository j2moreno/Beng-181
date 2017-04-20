import sys

def reconstruction(k_strings):
	recon = [k_strings[0]]
	
	for element in k_strings:
		if element == k_strings[0]:
			continue
		recon.append(element[len(element) - 1])

	return recon

filename = sys.argv[1]
file = open(filename, 'r')
data = file.read().splitlines()
array = []

for line in data:
	array.append(line)


result = reconstruction(array)
print("".join(str(x) for x in result))
