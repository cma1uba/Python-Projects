import random

choices = ('r', 'p', 's')

while True:		
	user_choice = input("Rock, Paper or Scissors? (r/p/s): ").lower()
	
	if user_choice not in choices:
		print("Invalid choice!")
		continue
	computer_choice = random.choice(choices)
	print(f"Your choice: {user_choice}")
	print(f"computer_choice: {computer_choice}")
	
	if user_choice ==  computer_choice:
		print("Thats a Tie!!")
	elif (
		(user_choice == "r" and computer_choice == "s") or 
		(user_choice == "p") and computer_choice == "r" or 
		(user_choice == "s" and computer_choice == "p")
	):
		print("You win")
	else:
		print("You lose")
	
	should_continue = input("Play again? (y/n): ")
	if should_continue == "n":
		print("Exiting Game")
		break
	else:
		continue