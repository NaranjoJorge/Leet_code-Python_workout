def sum_numbers(x):
	#Sum numbers in string x
	return sum(int(i) for i in x.split() if i.isdigit())

#print(sum_numbers('10 abc 20 de44 30 55fg 40'))