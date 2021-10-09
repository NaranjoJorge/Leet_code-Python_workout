'''
run_timing(): Ask user for 10km running times and gives the 
average over all runs.
'''
def run_timing():
	count = total_run = 0
	while True:
		try:
			total_run += float(input('Enter 10KM run time: '))
		except ValueError:
			break
		count += 1
	try:
		return f'Average of {total_run/count} over {count} runs'
	except ZeroDivisionError:
		return f'Average of 0 over no runs'

		