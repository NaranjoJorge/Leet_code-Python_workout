'''
@sum_integers_string(file): Receives a text file and returns sum
of integer strings within that file.

@file: Text file
'''
def sum_integers_string(file):
	sum = 0
	with open(file) as f:
		for string in "".join(f).split():
			try:
				sum += float(string)
			except ValueError:
				continue
	return sum

print(sum_integers_string('../dicts_sets/squid.txt'))

	
