'''
@dict_in_dict(file):Returns dict with user_name keys and 
dicts as values with id, home & shell keys and their respective
values.

@file: 'Password file' (/etc/passwd)
'''
from collections import defaultdict
from json import dumps

def dict_in_dict(file):
	d = defaultdict(dict)

	with open(file) as f:
		for line in f:
			if not line.startswith('#'):
				line = line.lstrip('_').rstrip().split(':')
				d[line[0]].update({'ID' : int(line[2])})
				d[line[0]].update({'HOME' : line[5]})
				d[line[0]].update({'SHELL' : line[6]})

	d = dumps(d, indent=4,sort_keys=True)
	return d

#print(dict_in_dict('/etc/passwd'))
