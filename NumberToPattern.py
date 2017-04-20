
array = []

def numberToPattern(index, k_mer):
	
	if k_mer == 1:
		symbol = numberToSymbol(index)
		array.append(symbol)
		return 0 

	preIndex = index / 4
	remainder = index % 4
	symbol = numberToSymbol(remainder)
	prePattern = numberToPattern(preIndex, k_mer-1)

	array.append(symbol)
	return array

def numberToSymbol(position):
	if position == 0:
		return 'A'
	elif position == 1:
		return 'C'
	elif position == 2:
		return 'G'
	elif position == 3:
		return 'T'

result = numberToPattern(231,4)

print("".join(str(x) for x in array))