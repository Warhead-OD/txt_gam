from random import randint

# Formatted as (visited, story progression)
# Starting Screen,
world_location_data = ([0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0])
cur_location = 0
#
world_items = []


def help():
	"""
Is used to generate a list of allowed inputs that the user
can give. If the player chooses to, it will also give a more
descriptive bit on what each command does.
	"""
	print("\n The commands are;")
	print("north, east, south, west, grab, use, room, help\n")
	temp = input("Type one of these commands to learn more about it, otherwise, just press ENTER\n")
	if temp == "north":
		print("\nUsed to move the character up by one room.\n")
	elif temp == "east":
		print("\nUsed to move the character to the right by one room.\n")
	elif temp == "south":
		print("\nUsed to move the character down by one room.\n")
	elif temp == "west":
		print("\nUsed to move the character to the left by one room.\n")
	elif temp == "grab":
		print("\nLets the player try to grab an item from the room that they are in\n")
	elif temp == "use":
		print("\nLets the player try to use a specified object.\n")
	elif temp == "room":
		print("\nUsed to re-display the current locations text.\n")
	elif temp == "help":
		print("\nUsed to display a list of available commands as well as the option to give more details")
		print("on a command if the player asks for it.\n")
	else:
		print("\nInvalid Input\n")
	input("Press ENTER to continue")


def control(command, inp_list=(False, False, False, False)):
	"""
Takes the input of the user and then will attempt to let that thing be executed
	:param str command: The thing the player wants to do
	:param tuple inp_list: List of allowed directions
	"""
	
	command = command.lower()
	temp = command.split(" ")
	if temp[0] == "use":
		command = "use"
	
	global cur_location
	sp = world_location_data[cur_location][1]
	
	global world_items
	if command == "north" and inp_list[0]:
		cur_location += 1
	elif command == "east" and inp_list[1]:
		cur_location += 4
	elif command == "south" and inp_list[2]:
		cur_location -= 1
	elif command == "west" and inp_list[3]:
		cur_location -= 4
	elif command == "grab":
		print()
		if cur_location == 1 and world_location_data[1][1] == 0:
			world_items.append("coin")
			print("You yank the coin off of the string and put it into you pocket.")
			world_location_data[1][1] = 1
		else:
			print("There seems to be nothing to grab!")
		control(input("\nWhat would you like to do? (Try using only 1 word)\n"), inp_list)
		return
	elif command == "use" and len(temp) == 2:
		if temp[1] == "coin" and cur_location == 5 and world_items.count("coin"):
			print("You attempt to fit the coin into the thin slot on the box and it fits! There")
			print("is a small ding and then the box seems to fold open, leaving a small microphone")
			print("to be talked into. There is a small button #################################################")
		else:
			control("FAIL")
			return
		control(input("\nWhat would you like to do? (Try using only 1 word)\n"), inp_list)
	elif command == "room":
		pass
	elif command == "help":
		help()
		control(input("What would you like to do? (Try using only 1 word)\n"), inp_list)
		return
	else:
		print("\nInvalid Response")
		control(input("What would you like to do? (Try using only 1 word)\n"), inp_list)
		return
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


def ufmain():
	print()
	# This the variable that will be changed to hold the currently
	# allowed exits to a room.
	allowed_exits = ()
	
	# This set of if statements are going to be used to figure out
	# where the player currently is and then will display some text
	# statement based on what they have already done in the game
	while True:
		# This is the code for the starting room
		v = world_location_data[cur_location][0]
		sp = world_location_data[cur_location][1]
		if cur_location == 0:
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
		# This is the code for the mousetrap room
		if cur_location == 1:
			if not v:
				print("You walk towards the tall, heavy wooden door and attempt to push it open. You hear a")
				print("couple of clicks as it reluctantly slides open.")
				world_location_data[1][0] = 1
			print("You enter a white room, a deep blue tile lining the bottom edges of the room. You can")
			print("feel a slight lean in the floor, as if to guide you to the drain in the room. The room")
			print("seems to be well lit, but there is no obvious light source that you can see, almost as")
			print("if the walls themselves are providing the light for the room. There is a large wooden")
			print("door to the south and a lightly beaten dirt... trail to the east.")
			if sp == 0:
				print("There is some shiny looking coin hanging from a string in the middle of the room.")
			print("\nThere are exits to this room:")
			print("  east, south")
			allowed_exits = (False, True, True, False)
		# This is the code for the RPS room
		if cur_location == 5:
			if not v:
				print("You walk down the dirt trail from the hospital room. How strange a place for a path.")
				world_location_data[5][0] = 1
			print("You are now in a grand field that seems to stretch on forever. Towards the ends of the")
			print("world, the ground seems to lilt into the sky. There is a standing table off to one side")
			print("of the field that has a small slot in it, as if to guide you to put something into it.")
			print("\nThere are exits to this room:")
			print("  west")
			allowed_exits = (False, False, False, True)
		control(input("What would you like to do? (Try using only 1 word)\n"), allowed_exits)


ufmain()
