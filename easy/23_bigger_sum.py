'''
@sum_bigger(x,*args): All arguments have to be of same type.
adds all args when theay are bigger than x.

@x: Number, string, list or tuple.
'''
def sum_bigger(x,*args):

	a = []
	for i in args:
		if i > x:
			a.append(i)
	b = a[0]
	for i in a[1:]:
		b += i 
	
	return b

#print(sum_bigger(['g'], ['was'], ['z'], ['m'], ['a']))