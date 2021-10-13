'''
@capitalize_ubbi(word): Translates word to Ubbi language 
considering capitalized words.

@word: String
'''
def capitalized_ubbi(word):
	new = []
	for i in word:
		if i in 'aeiouAEIOU':
			new.append(f'ub{i}')
		else:
			new.append(i)
	return ''.join(new)

#print(capitalized_ubbi('Reed'))

