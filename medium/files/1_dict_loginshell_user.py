'''
@dict_loginshell_user(file): Returns dict with loginshell as
keys and list of users with that loginshell.

@file:'Password file' (/etc/passwd)
'''
from collections import defaultdict
from json import dumps

def dict_loginshell_user(file):
	dict = defaultdict(list)

	with open(file) as f:
		for line in f:
			if not line.startswith('#'):
				lst = line.lstrip('_').rstrip().split(':')
				dict[lst[-1]].append(lst[0])
	dict = dumps(dict, indent=4, sort_keys=True)

	return dict

#print(dict_loginshell_user('/etc/passwd'))