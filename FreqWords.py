

def mostFrequentkmer(text,k):
	frequentpatterns = set([])
	count = []

	for i in range(len(text) - k):
		pattern = text[i:k+i]
		count.insert(i,PatternCount(text,pattern))

	maxNumber = max(count)
	for i in range(len(text) - k):
		if count[i] == maxNumber:
			frequentpatterns.add(text[i:i+k])

	print list(frequentpatterns)

def PatternCount(text, pattern):
	count = 0
	end = len(text) - len(pattern)
	for i in range(end+1):
		#checks if window contains pattern and if so increments occurrances 
		if text[i:len(pattern)+i] == pattern: 
			count += 1
	return count


mostFrequentkmer('GTCGGCACTTTACGCTTTTACGCTTTTACGCTTCGGCGGTGGCAACTGCCGGTGACAATGAAACTGCCGGTTTACGCTTGTCGGCACTTTACGCTTAACTGCCGGTAACTGCCGGTCGGCGGTGGCGACAATGAGTCGGCACTGACAATGAAACTGCCGGTGACAATGAGACAATGACGGCGGTGGCGACAATGACGGCGGTGGCAACTGCCGGTGACAATGAGTCGGCACTTTACGCTTCGGCGGTGGCCGGCGGTGGCAACTGCCGGTGACAATGATTACGCTTGACAATGATTACGCTTTTACGCTTCGGCGGTGGCCGGCGGTGGCCGGCGGTGGCGACAATGATTACGCTTCGGCGGTGGCTTACGCTTTTACGCTTAACTGCCGGTAACTGCCGGTGACAATGATTACGCTTGTCGGCACTCGGCGGTGGCCGGCGGTGGCAACTGCCGGTGTCGGCACTGTCGGCACTTTACGCTTGTCGGCACTGACAATGAGACAATGAAACTGCCGGTGACAATGACGGCGGTGGCGTCGGCACTGACAATGAGTCGGCACTGACAATGACGGCGGTGGCGACAATGAAACTGCCGGTGTCGGCACTCGGCGGTGGCCGGCGGTGGCAACTGCCGGTCGGCGGTGGCCGGCGGTGGCGACAATGAAACTGCCGGTCGGCGGTGGCTTACGCTTAACTGCCGGTAACTGCCGGTTTACGCTTAACTGCCGGTTTACGCTTGACAATGAAACTGCCGGTTTACGCTTGTCGGCACTCGGCGGTGGCTTACGCTTGACAATGAAACTGCCGGTGACAATGACGGCGGTGGCCGGCGGTGGCAACTGCCGGTCGGCGGTGGCGTCGGCACTAACTGCCGGTCGGCGGTGGCGACAATGACGGCGGTGGC',11)