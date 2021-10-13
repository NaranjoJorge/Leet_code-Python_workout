'''
@def ubbi(word): Translates word into Ubbi Dubbi language.
@word: String
'''
def ubbi(word):
	a = list(word)
	i = 0
	while i < len(a):
		if a[i] in 'aeiou':
			a = a[:i] + ['ub'] + a[i:]
			i+=2
			continue
		i+=1
	return ''.join(a)

#print(ubbi('reed'))