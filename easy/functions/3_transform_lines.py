'''
@transform_lines(func, filein, fileout):Runs func in every line
of filein and prints it to fileout.

@func:Function with 1 and only 1 argument.
@filein: File
@fileout: File
'''
def transform_lines(func, filein, fileout):
	with open(fileout, 'w') as o:
		with open(filein) as i:
			for line in i:
				print(func(line), file=o)

#transform_lines(len, 'texto.txt', 'afuera.txt')