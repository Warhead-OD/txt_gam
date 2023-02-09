from random import randint

# This RPS code is something that I have been working on for a while.
# It IS copy and pasted from another one of my repos because I didn't
# want to have to retype it or deal with the importing.
# There are some modifications for the purposes of this program
def rps():
	# this determines the computer's choice
	options = ("Rock", "Paper", "Scissors")
	options_short = ("R", "P", "S")
	c_choice_l = options[randint(0, 2)]
	# this will determine the user's choice
	u_choice = input("Rock, Paper, or Scissors?\n")
	
	# this determines and displays the winner
	try:
		c_choice = c_choice_l[0]
		u_choice = u_choice[0].upper()
		options_short.index(u_choice)
		print(f"\nThe computer chose {c_choice_l}!")
		if u_choice == c_choice:
			input("It was a tie!")
		elif u_choice == "R":
			if c_choice == "S":
				input("You won!")
				return 1
			else:
				input("You lost!")
		elif u_choice == "P":
			if c_choice == "R":
				input("You won!")
				return 1
			else:
				input("You lost!")
		elif u_choice == "S":
			if c_choice == "P":
				input("You won!")
				return 1
			else:
				input("You lost!")
		return 0
	# this will run if the user gives an invalid response
	except ValueError:
		print("Invalid choice!")
		return rps()


# This is the code for running the program
def main():
	# Formatted as (visited, story progression)
	# Starting Screen, 
	world_location_data = ((0, 0), (0, 0))
	#
	world_items = ()
	
	# This is a set list of the allowed inputs from the user for
	# each of their turns. It is auto formatted as a .lower()
	allowed_inputs = ("north", "east", "south", "west")
	
	while True:
		print(rps())


if __name__ == "__main__":
	main()
