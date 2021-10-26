'''
@passwd_to_dict(file): Returns a dict where keys are username and
values are user_id.

@file: 'password file' (/etc/passwd)
'''
from json import dumps

def passwd_to_dict(file):
	dict = {}
	with open(file) as f:
		for line in f:
			if line.startswith('#'):
				continue
			dict[line.lstrip('_').split(':')[0]] = line.lstrip('_').split(':')[2]
	dict = dumps(dict, indent=4, sort_keys=True)
	return dict

#print(passwd_to_dict('/etc/passwd'))
			
			
