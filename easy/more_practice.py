'''
@f_number: Takes a float(z) and two integers (before and after). 
The function should return a float consisting of before digits 
before the decimal point and after digits after.

@z : float
@before: int
@after: int
'''

def float_number(z, before, after):
	count = 1
	before = str(int(z))[-before:]
	for i in range(after):
		count *= 10
	z *= count
	after = str(int(z))[-after:]
	z = float(before + '.' + after)
	return(z)

#print(float_number(12345.9987,4,2))

