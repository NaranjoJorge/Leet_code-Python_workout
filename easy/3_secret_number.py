#Game that makes the user guess the secret number.

from random import randint

def guessing_game():
	tries = 0
	number = randint(0,100)
	try:
		guess = int(input('Want to find the secret number? Choose a number from 0 to 100. '))
	except ValueError:
		guess = int(input('Please enter a number from 0 to 100. '))
	while guess != number:
		if guess > number:
			guess = int(input('Too high. Choose another number. '))
		else:
			guess = int(input('Too low. Choose another number. '))
		tries += 1
		if tries == 2:
			return 'Too many chances. Game over'
	return 'The power is with you. You have selected the secret number.'
