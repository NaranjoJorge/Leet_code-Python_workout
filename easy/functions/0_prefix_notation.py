'''
@calc(prefix):Returns calculation of a math expresion in prefix 
notation (one operator and two numbers).
@prefix: String
'''
def calc(prefix):
	a = prefix.split()
	d = {
		'+': int(a[1]) + int(a[2]),
		'-': int(a[1]) - int(a[2]),
		'/': int(a[1]) / int(a[2]),
		'*': int(a[1]) * int(a[2]),
		'**': int(a[1]) ** int(a[2]),
		'%': int(a[1]) % int(a[2]),
	}

	return d[a[0]]

#print(calc('** 6 4'))