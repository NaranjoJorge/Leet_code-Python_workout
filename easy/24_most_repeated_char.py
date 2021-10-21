'''
@most_repeated_char(*words): Returns string with most repeated
character.

@words: Strings
'''
from collections import Counter

def most_repeated_char(*words):
	a=0
	b=''
	for word in words:
		if Counter(word).most_common(1)[0][1] > a:
			a = Counter(word).most_common(1)[0][1]
			b = word
	return b

#print(most_repeated_char('cacacama', 'wase', 'perro', 'meeelo'))
