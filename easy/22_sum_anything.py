'''
sum_anything(*args):

@args:Strings,lists,numbers or tuples.
'''
def sum_anything(*args):
	if not args:
		return 0

	a = args[0]
	for i in args[1:]:
		a += i
	return a
#print(sum_anything('abc', 'cdf'))