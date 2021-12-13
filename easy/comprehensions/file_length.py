import os

def file_length(lst):
	#Receives list of files and returns dict with with files as keys,
	#and length of file as value.
	return {file:os.stat(file).st_size for file in lst}

print(file_length(['amarillo.txt', 'delfin.txt', 'deer.txt', 'christmas.txt']))
