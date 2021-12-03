def flatten_odds(lsts):
	return [int(num)
			for lst in lsts
			for num in lst
			if (type(num) == int or num.isdigit()) and (int(num) % 2 != 0)
			]

#print(flatten_odds([['13'],['casa']]))