def dict(file):
	return {line.split('=')[0]:line.split('=')[1].strip() for line in open(file)}

print(dict('config.txt'))