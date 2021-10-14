'''
@sort(words): Sorts individual words in string containing more than 
one word.
@words: String
'''

def sort(words):
	a = ''
	b = ''
	for word in words.split():
		a = ''.join(sorted(word))
		b += f'{a}, '
	return b

#print(sort('Tom Dick Harry'))