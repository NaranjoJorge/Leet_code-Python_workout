'''
@alphabetically_last(file): Given a file, it returns 
the last word (alphabetically).

@file: String
'''
def alphabetically_last(file):
	a = ''.join(open(file)).lower().split()
	a.sort()
	return a[-1]

#print(alphabetically_last('data.txt'))
