'''
@get_rainfall(): Ask user for cities and rain fallen in those
cities. Prints cities with their corresponding total of fallen
rain.
'''

def get_rainfall():
	d = {}
	city = input('Enter city: ')
	while city != '':
		rain = int(input(f'Mm of rain fallen in {city}: '))
		if city in d:
			d[city] += rain
		else:
			d[city] = rain
		city = input('Enter city: ')
	for x,y in d.items():
		print(f'{x}: {y}')

#get_rainfall()