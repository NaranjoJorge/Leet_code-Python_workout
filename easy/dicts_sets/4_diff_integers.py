'''
@diff_integers(lst): Given a list of integers, returns number
of different integers contain within that list.

@lst: list of integers
'''
def diff_integers(lst):
	a = set(lst)
	return len(a)

#print(diff_integers([1,1,1,2,3,3,2,4,5,4,7]))