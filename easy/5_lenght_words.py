'''
words_length : returns as a tuple the average, longest & shortest
length of word in words.

@words : list of strings
'''

def words_length(words):
	average = longest = 0
	shortest = 50
	for word in words:
		average += len(word)
		if len(word) > longest:
			longest = len(word)
		if len(word) < shortest:
			shortest = len(word)

	return average/2, longest, shortest