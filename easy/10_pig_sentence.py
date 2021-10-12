'''
@pl_sentence(sentence):Translates sentence into pig language.

@sentence: string
'''
def pl_sentence(sentence):
	new_words = []
	for i in sentence.split():
		if i[0] in 'aeiou':
			new_words.append(i + 'way')
		else:
			new_words.append(i[1:] + i[0] + 'ay')
	return ' '.join(new_words)

#print(pl_sentence('this is a test translation'))
			 