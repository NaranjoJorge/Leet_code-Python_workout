#function that sums arbitrary number of arguments.

def mysum(*args):
	sum = 0
	for i in args:
		sum += i
	return sum