def etc_passwd(file):
	#Gets /etc/passwd returns dict of user as keys and id's as value.
	return { line.split(':')[0].strip('_,-'): line.split(':')[2].strip('-_') for line in open(file) if not line.startswith('#')}

#print(etc_passwd('/etc/passwd'))