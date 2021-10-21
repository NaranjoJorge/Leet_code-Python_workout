'''
@most_vowels(*words): Returns string with more vowels
@words: Strings
'''
def most_vowels(*words):
	return sorted(words, key=lambda word: sum(char in 'aeiou' for char in word))[-1]

#print(most_vowels('caaaasa', 'peeero', 'puotea'))