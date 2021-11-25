def area_code(x):
	# Given a list of strings. Strings are 10digits in the form xxx-abc-zzzz. If a is 0,1,2,3,4 or 5, then
	# xxx+1-abc-zzzz. Otherwise xxx-abc-zzzz. Returns new list with afore-mentioned parameters. 
	return [str(int(i.split('-')[0]) + 1) + i[3:]
			if i[4] in '012345'
			else i
			for i in x
	]

#print(area_code(['123-456-7890', '123-333-4444', '123-777-8888']))