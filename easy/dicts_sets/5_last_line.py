'''
@last_line(file): Returns last line of file.
@file: Text file
'''
def last_line(file):
	with open(file) as f:
		return(list(f)[-1])

#print(last_line('squid.txt'))