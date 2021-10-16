'''
@plus_minus(x):Takes list or tuple of numbers and returns
 result of alternating summing and subtracting numbers.
 
@x: String or tuple
'''
def plus_minus(x):
	odd = x[0]
	even = 0
	for i in range(1,len(x)):
		if i%2 == 0:
			even += x[i]
		else:
			odd += x[i]
	return odd-even
	
#print(plus_minus([10,20,30,40,50,60]))