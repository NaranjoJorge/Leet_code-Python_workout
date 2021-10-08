'''
objects_sum: Returns the sum of arbitrary arguments 
when they are numbers or can be turn to numbers, ignoring 
the others.

@*args : objects
'''
def objects_sum(*args):
	#Still not finish. Need to include tuples, dict & list
	#in *args
	sum = 0
	for object in args:
		try:
			if float(object):
				sum += float(object)
		except (ValueError, TypeError) as e:
			continue
	return sum

