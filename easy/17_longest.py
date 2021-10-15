'''
@longest_word(article): Returns longest word in text file.

@article: String/text file.
'''
def longest_word(article):
	longest = 0
	letters = ''
	for line in open(article):
		line = line.split()
		for word in line:
			word = word.strip('.,:;?!')
			if longest < len(word):
				longest = len(word)
				letters = word
		
	return f'The longest word is [{letters}] and has [{longest}] characters.'

#print(non_sense('data.txt'))