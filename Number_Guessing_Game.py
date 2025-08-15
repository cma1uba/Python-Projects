import random

winning_number = random.randint(1, 10)
count = 0
while True:
	guess = int(input('\nMake a guess (1-10): '))
	if guess > winning_number:
		print("Too high")
		count += 1
	elif guess < winning_number:
		print('Too low')
		count += 1
	else:
		print(f'The winning_number is:  {winning_number}.')
		count += 1
		if count == 1:
			print(f'Gold!!!, First attempt win')
		elif count == 2:
			print('SILVER!!!, You won on second attempt')
		elif count == 3:
			print('Bronze!!!, You won on third attempt')
		else:
			print(f'You won with {count} attempts')
		break