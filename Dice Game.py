import random

roll_count = 0
while True:
	launcher = input('\nReady to play? (y/n): ').lower()
	if launcher == 'y':
		dice1 = random.randint(1, 6)
		dice2 = random.randint(1, 6)
		print(f'{dice1}, {dice2}')
		roll_count += 1
	elif launcher == 'n':
		print('Thanks for playing')
		print(f'User played {roll_count} times')
		break
	else:
		print('Invalid input.')
