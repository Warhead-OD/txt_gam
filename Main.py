from random import randint


# Formatted as (visited, story progression)
# Starting Screen,
world_location_data = ([0, 0], [0, 0])
cur_location = 0
#
world_items = ()


def help():
	"""
Is used to generate a list of allowed inputs that the user
can give. If the player chooses to, it will also give a more
descriptive bit on what each command does.
	"""
	print("\n The commands are;")
	print("north, east, south, west, help\n")
	temp = input("Type one of these commands to learn more about it, otherwise, just press ENTER\n")
	if temp == "north":
		print("Used to move the character up by one room.")
	elif temp == "east":
		print("Used to move the character to the right by one room.")
	elif temp == "south":
		print("Used to move the character down by one room.")
	elif temp == "west":
		print("Used to move the character to the left by one room.")
	elif temp == "help":
		print("Used to display a list of available commands as well as the option to give more details on a command")
	input("Press ENTER to continue")


def control(command, inp_list=(False, False, False, False)):
	"""
Takes the input of the user and then will attempt to let that thing be executed
	:param str command: The thing the player wants to do
	:param tuple inp_list: List of allowed directions
	"""
	global cur_location
	if command == "north" and inp_list[0]:
		cur_location += 1
	elif command == "east" and inp_list[1]:
		cur_location += 4
	elif command == "south" and inp_list[2]:
		cur_location -= 1
	elif command == "west" and inp_list[3]:
		cur_location -= 4
	elif command == "help":
		help()
	


def rps():
	"""
Takes no parameters. Lets the player play one round of Rock Paper Scissors
against the computer.
	:returns: 1 if player wins, 0 if player loses
	"""
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
# This RPS code is something that I have been working on for a while.
# It IS copy and pasted from another one of my repos because I didn't
# want to have to retype it or deal with the importing.
# There are some modifications for the purposes of this program


def main():
	print()
	# This is a set list of the allowed inputs from the user for
	# each of their turns. It is auto formatted as a .lower()
	allowed_inputs = ("north", "east", "south", "west")
	allowed_exits = ()

	# This set of if statements are going to be used to figure out
	# where the player currently is and then will display some text
	# statement based on what they have already done in the game
	while True:
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
			print("is painted a rich blend of light blues, fading to orange as the sun just barely starts")
			print("to bite into the horizon. The grass at your feet is long and soft but still seems to be")
			print("well maintained. As you look around, you see one, singular door, seeming to go nowhere,")
			print("standing to the north.\n")
			print("There are exits to this room:\n  north")
			allowed_exits = (True, False, False, False)
		if cur_location == 1:
			v = world_location_data[1][0]
			sp = world_location_data[1][1]
			if not v:
				print("You walk towards the tall, heavy wooden door and attempt to push it open. You hear a couple")
				print("of clicks as it reluctantly slides open and you are greeted by a hospital looking room.")
				world_location_data[1][0] = 1
			print("You enter a white room, a deep blue tile rimming the bottom edges of the room. You can")
			print("feel a slight lean in the floor, as if to guide you to the drain in the room. The room")
			print("seems to be well lit, but there is no obvious light source that you can see, almost as if")
			print("the walls themselves are providing the light for the room.")
			if sp == 0:
				print("There is some form of mouse trap hanging from a thin string in the middle of the room.")
			print("\nThere are exits to this room:")
			print("  east#not implemented, south")
			allowed_exits = (False, False, True, False)
		control(input("What would you like to do? (Try using only 1 word)\n"), allowed_exits)


if __name__ == "__main__":
	main()
