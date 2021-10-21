'''
@print_tuple_records(lst): Prints sorted records of tuples.
@lst: List of tuples/lists.
'''
from operator import itemgetter

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]
 
def print_tuple_records(lst):
	for tuple in sorted(lst, key=itemgetter(1,0)):
		print(f'{tuple[1]:10} {tuple[0]:10} {tuple[2]:5.2f}')

#print_tuple_records(PEOPLE)
