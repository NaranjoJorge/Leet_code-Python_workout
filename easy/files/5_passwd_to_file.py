'''
@passwd_to_file(file, file1): Gets items from csv /etc/passwd 
file and writes them in new file1.

@file:file
@file1:file
'''
def passwd_to_file(file, file1):
	d = {}
	with open(file) as f:
		for line in f:
			if not line.startswith('#'):
				d[line.split(':')[0].lstrip('_')] = line.split(':')[2]
	
	with open(file1, 'w') as f:
		for k,v in d.items():
			print(f'{k:25} {v:5}', file=f)

#passwd_to_file('/etc/passwd', 'wcfile.txt')
