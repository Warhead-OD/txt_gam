from random import randint


def rps():
	"""
	Takes no parameters. Lets the player play one round of Rock Paper Scissors
	against the computer.

	:returns: 1 if player wins, 0 if player loses or ties
	"""
	# this determines the computer's choice
	options = ("Rock", "Paper", "Scissors")
	options_short = ("R", "P", "S")
	c_choice_l = options[randint(0, 2)]
	# this will determine the user's choice
	u_choice = input("(R)ock, (P)aper, or (S)cissors?\n")
	
	# this determines and displays the winner
	try:
		c_choice = c_choice_l[0]
		u_choice = u_choice[0].upper()
		options_short.index(u_choice)
		print(f"\nThe computer chose {c_choice_l}!")
		if u_choice == c_choice:
			input("\nIt was a tie!")
		elif u_choice == "R":
			if c_choice == "S":
				input("\nYou won!")
				return 1
			else:
				input("\nYou lost!")
		elif u_choice == "P":
			if c_choice == "R":
				input("\nYou won!")
				return 1
			else:
				input("\nYou lost!")
		elif u_choice == "S":
			if c_choice == "P":
				input("\nYou won!")
				return 1
			else:
				input("\nYou lost!")
		return 0
	# this will run if the user gives an invalid response
	except ValueError:
		print("\nInvalid Choice!")
		return rps()
	except IndexError:
		print("\nInvalid Input!")
		return rps()


# This RPS code is something that I have been working on for a while.
# It **IS** copy and pasted from another one of my repos because I didn't
# want to have to retype it or deal with the importing.
# There are some modifications for the purposes of this program
