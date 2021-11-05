'''
@calc_args(prefix): Returns calculation of a mathemarical expression
using prefix notation.

@prefix: String
'''
import operator

def calc_args(prefix):
	a = prefix.split()
	c = a[1]

	d = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'**': operator.pow,
		'/': operator.truediv,
		'%': operator.mod,
	}

	for number in a[2:]:
		c = d[a[0]](c,number)
	
	return c