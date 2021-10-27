'''
@word_count(file): Returns # of lines, words, unique words
and chars in file.

@file:Text file
'''
def word_count(file):
	a = b = c = 0
	unique = set()

	with open(file) as f:
		for line in f:
			a += 1
			for char in line:
				c += 1
			for word in line.split():
				b += 1
				unique.add(word)

	return a,b,len(unique),c

#print(word_count('wcfile.txt'))

	
	