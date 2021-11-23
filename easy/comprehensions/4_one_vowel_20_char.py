def one_v_20_c(file):
	#Writes lines of file that have at least 1 vowel and more than 20 chars, into new.txt.
	with open(file) as f, open('new.txt', 'w') as m:
		print([line.rstrip(' \n') for line in f if len(line)>20 and len(set('aeiou') & set(line))>0], file=m)

#one_v_20_c('delfin.txt')