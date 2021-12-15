def int_values_dict(file):
	#Returns dict from config file. With values as int. Ignoring those values that can't be converte to int.
	return {line.split('=')[0]:int(line.split('=')[1].strip()) for line in open(file) if line.split('=')[1].strip().isdigit()}

print(int_values_dict('config.txt'))