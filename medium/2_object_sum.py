'''
objects_sum: Returns the sum of arbitrary arguments 
when they are numbers or can be turned to numbers, ignoring 
the others.

@*args : objects
description: Doesn't work for list inside list, dicts inside list, etc.
Also doesn't work for strings of the form 'sunny23'.
Note: I know I am repeating myself.
'''
def objects_sum(*args):
	sum = 0
	for object in args:
		if type(object) == dict:
			for k,v in object.items():
				try:
					sum += float(v)
				except (ValueError, TypeError) as e:
					continue
		elif type(object) == list or type(object) == tuple:
			for e in object:
				try:
					sum += float(e)
				except (ValueError, TypeError) as e:
					continue
		else:
			try:
				sum += float(object)
			except (ValueError, TypeError) as e:
				continue
	return sum

#print(objects_sum(5,'5', {'year': 5}))
