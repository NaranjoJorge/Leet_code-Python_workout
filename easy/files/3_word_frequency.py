'''
@words_frequency(): Returns frequency of words in file as a dict.
'''
from json import dumps

def words_frequency():
	d = {}
	file = input('Enter file name: ')
	words = input('Enter words: ')

	for word in words.split():	
		d[word] = "".join(open(file)).split().count(word)
	
	return dumps(d, indent=4, sort_keys=True)

#print(words_frequency())