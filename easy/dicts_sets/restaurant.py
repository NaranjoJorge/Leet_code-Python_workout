'''
@restaurant(d):Ask user to select plate from menu and prints 
its plate and the total so far. Return grand total.

@d:Dictionary
'''
MENU = {
	'Ice cream':5,
	'Meat':15,
	'Fish':12,
	'Chicken':7,
	'Lentils':12,
	'Soup':6
}

def restaurant(d):
	total = 0
	order = input('Choose a plate: ')
	
	while order != '':
		try:
			total += d[order]
		except KeyError:
			order = input('Please choose a plate from the menu: ')
			continue
		print(f'{order} is {d[order]}, total is {total}')
		order = input('Choose a plate: ')
		
	
	return f'Your total is {total}'

#print(restaurant(MENU))