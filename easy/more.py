def pl_sentence(sentence):
	new_words = []
	for i in sentence.split():
		if i[0] in 'aeiou':
			i = i + 'way'
		else:
			i = i[1:] + i[0] + 'ay'
	return sentence

print(pl_sentence('this is a test translation'))