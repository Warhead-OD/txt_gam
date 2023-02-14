from random import randint


# This is the function that will be used for calling the help function
# and/or displaying more detailed information on that command
def help():
	print("\n The commands are;")
	print("north, east, south, west")
	temp = input("Type one of these commands to learn more about it, otherwise, just press ENTER\n")
	if temp == "north":
		print("Used to move the character up by one room.")
	elif temp == "east":
		print("Used to move the character to the right by one room.")
	elif temp == "south":
		print("Used to move the character down by one room.")
	elif temp == "west":
		print("Used to move the character to the left by one room.")
	input()
	print()

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
	print()
	# Formatted as (visited, story progression)
	# Starting Screen, 
	world_location_data = ([0, 0], [0, 0])
	cur_location = 0
	#
	world_items = ()
	
	# This is a set list of the allowed inputs from the user for
	# each of their turns. It is auto formatted as a .lower()
	allowed_inputs = ("north", "east", "south", "west")

	# This set of if statements are going to be used to figure out
	# where the player currently is and then will display some text
	# statement based on what they have already done in the game
		# This is the code for the starting room
	if cur_location == 0:
		v = world_location_data[0][0]
		sp = world_location_data[0][1]
		if not v:
			print("Welcome to my humble Text Game!\n")
			if input("Would you like the list of commands to the game? yes/no\n") == "yes":
				help()
			print("\nAs you join into this strange new digital world, you feel as if you are being watched.")
			world_location_data[0][0] = 1
		print("All around you are grand white pillars that seem to stretch high into the sky. The sky")
		###################################################################################################################################################
		print("There are exits to this room to the:\n  north")


if __name__ == "__main__":
	main()
