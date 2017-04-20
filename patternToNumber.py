

def patternToNumber(pat):

	if len(pat) == 0:
		return 0
	symbol = pat[len(pat) - 1] 
	prefix = pat[0:len(pat) - 1]
	
	return 4*patternToNumber(prefix) + symbolToNumber(symbol)

def symbolToNumber(letter):

	if letter == 'A':
		return 0
	elif letter == 'C':
		return 1
	elif letter == 'G':
		return 2
	elif letter == 'T':
		return 3

result = patternToNumber('AGTGCCTCGGCCACCAGTCGCCATCCG')
print result
