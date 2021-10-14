'''
@something(article, names): Given a string(article) and a list
of strings(names), replace names in article with '___'.

@article: .txt file
@names: list of strings
'''

def something(article, names):
	a = (''.join(open(article)))
	for name in names:
		if name in a:
			a = a.replace(name, '___')
	return a