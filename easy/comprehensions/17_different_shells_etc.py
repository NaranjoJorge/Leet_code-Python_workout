def diff_shells(etc):
	#Gets /etc/passwd file, returns set of different shells used.
	return {line.split(':')[6].strip() for line in open(etc) if not line.startswith('#')}

print(diff_shells('/etc/passwd'))