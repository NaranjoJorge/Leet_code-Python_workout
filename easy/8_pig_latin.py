'''
@pig_latin(word): function that translate word into pig_latin.
@word: string
'''
def pig_latin(word):
	word = list(word)
	if word[0] in 'aeiou':
		word.append('way')
		return ''.join(word)
	first_char = word[0]
	word = word[1:]
	word.append(first_char + 'ay')
	return ''.join(word)