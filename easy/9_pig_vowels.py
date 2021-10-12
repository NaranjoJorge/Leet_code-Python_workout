'''
@pig_vowels(word): If word contains 2 different vowels.
'way' is added to the end of the word. If only one vowel,
we take the first letter move it to the last and add 'ay'.

@word: string
'''
def pig_vowels(word):
	count = 0
	for i in set(word):
		if i in 'aeiou':
			count+=1
	if count > 1:
		return word + 'way'
	return word[1:] + word[0] + 'ay'

print(pig_vowels('wind'))

