from RockPaperScissors import rps
from numpy import array

INPUT_HELP = {
	"north": "\nUsed to move the character up by one room.\n",
	"east": "\nUsed to move the character to the right by one room.\n",
	"south": "\nUsed to move the character down by one room.\n",
	"west": "\nUsed to move the character to the left by one room.\n",
	"use": "\nLets the player try to use a specified object.\n",
	"grab": "\nLets the player try to grab an item from the room that they are in\n",
	"room": "\nUsed to re-display the current locations text.\n",
	"help": "\nUsed to display a list of available commands as well as the option to give more details\
		\non a command if the player asks for it.\n",
	"save": "\nUsed to save the current state of the game.\n",
	"load": "\nUsed to load the game from a save file.\n",
	"quit": "\nUsed to stop the game from running.\n"}
DIRECTIONS = {
	"north": array([0, 1]),
	"east": array([1, 0]),
	"south": array([0, -1]),
	"west": array([-1, 0])}


class Room:
	"""
	Room class for building new rooms
	"""
	def __init__(self, allowed_exits=[]):
		"""
		Initiates a Room object's variables to (mostly) empty collections.
		:param allowed_exits: The exits that are allowed for a room. Defaults to no exits.
		"""
		self.explored = False
		self.room_progression = 0  # used to track the progression of the room
		self.description = ["", ""]  # intro room text, description of this room
		self.item_pickups = []  # items to pick up, pickup description, description text
		self.usable_items = {}  # item name, usage text
		self.allowed_exits = allowed_exits  # allowed direction to leave the room
	
	def __str__(self):
		strings = ""
		strings += f"Is Explored: {self.explored}\n"
		strings += f"Allowed Exits: {self.allowed_exits}\n"
		strings += f"Item Pickups: {self.item_pickups}\n"
		strings += f"Usable Items: {self.usable_items}\n"
		strings += f"Description: {self.description}"
		return strings
	
	def movement(self, player, choice):
		"""
		This is the function that allows the player to move around within the game world.
		:param player: The player object to be used in movement.
		:param choice: The direction that the player is trying to go.
		:return:
		"""
		if choice in self.allowed_exits:
			player.cur_location = DIRECTIONS[choice]
			return True
		else:
			print("\nYou can't go that direction.\n")
	
	def use_item(self, player):
		"""
		Used to attempt to use an item that is prompted from the user.
		Returns a statement depending on validity and usage.
		:param player: The player that is being used.
		:return:
		"""
		print()
		# checks if the user's inventory is empty
		if player.inventory:
			# displays the users current items in their inventory
			print(f"You currently have the following items:\n{player.inventory}\n")
			# asks the user for the item that they want to use
			to_use = input("What would you like to use: ")
			# checks if the item is in the player's inventory
			if to_use in player.inventory:
				# checks to see if the item can be used in the current room
				if to_use in self.usable_items:
					# prints the usage text of the used item
					print()
					print(self.usable_items[to_use])
					player.inventory.remove(to_use)
					del self.usable_items[to_use]
					if to_use == "blade":
						input("\nYou have beaten the game! Press enter to quit!")
						exit("Winner Winner Chicken Dinner!")
					self.room_progression += 1
				else:
					print("That item cannot be used here.")
			else:
				print("That item is not in your inventory.")
		else:
			print("You have nothing to use.")
		print()
	
	def pick_item(self, player):
		"""
		Used to attempt to pick up an item from the room.
		Returns a statement depending on validity
		:param player: The player that is being used.
		:return:
		"""
		print()
		# checks to make sure that there is something to pick up
		if self.item_pickups:
			# displays the description text of the item to be picked up
			print(f"{self.item_pickups[2]}")
			# adds the item to the player's inventory
			player.inventory.append(self.item_pickups[0])
			self.item_pickups.clear()
		else:
			print("There is nothing to pick up.")
		print()
	
	def room_description(self, player_location):
		"""
		Prints a description of the room that is pulled from the description var
		:return:
		"""
		print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		# prints a room introduction script if it is the player's first time
		# in the given room
		if not self.explored:
			print(self.description[0])
			self.explored = True
		
		# prints the current room code
		room_code(player_location, True)
		
		# prints the main bulk of the room description
		print(self.description[1])
		# prints any pick-able items that are in the room
		if self.item_pickups:
			print(self.item_pickups[1])
		
		# prints the current room code
		room_code(player_location)
		
		# prints the allowed exits to a given room
		exit_string = str(self.allowed_exits).replace("'", "")
		print(f"\nThere are exits to this room:\n  {exit_string[1:-1]}\n")
	
	@staticmethod
	def help_description():
		"""
		Prints the allowed inputs from the user.
		Will display more details on a command if prompted.
		:return:
		"""
		print("\n The commands are:")
		print("north, east, south, west, use, grab, room, help, save, load, quit\n")
		helped = input("Type one of these commands to learn more about it, otherwise, just press ENTER\n")
		
		if helped in INPUT_HELP:
			print(f"{INPUT_HELP[helped]}")
		elif helped == "":
			pass
		else:
			print("\nInvalid Input\n")


# stores the location of each room object to be called on
room_locations = {}


def room_code(location, first_time=False):
	"""
	Runs the unique code on a per-room basis.
	Based on the items that have been used on the room.
	:param location: Is the player's current location
	:param first_time: Is a boolean that is used to determine if the player has been in the room before
	:return:
	"""
	global room_locations
	if location in room_locations:
		if location == (2, 2):
			if room_locations[location].room_progression == 1:
				room_locations[location].description[1] = "You in a grand field that seems to stretch on forever. Towards the ends of the\n\
world, the ground seems to lilt into the sky. There is a standing table off to one side\n\
of the field that has one standing table with a microphone on it. There are three buttons\n\
on the table resembling a different image on each one: rock, paper, and scissors. There\n\
is a large metalic wall to the south that seems to be blocking your path, however, you seem\n\
to be able to go in all other directions."
				if not first_time:
					if input("\nWould you like to play Rock, Paper, Scissors? (yes/no)\n") == "yes":
						wins = 0
						input("\nYou must win 3 times to pass. Press ENTER to begin.\n")
						while wins < 3:
							wins += rps()
							print(f"You have won {wins} times.\n")
						input("You have won! A key appears on the table.")
						room_locations[location].item_pickups = ["key", "\nThere is a key on the table.", "You pick up the key."]
						room_locations[location].room_progression += 1
			if room_locations[location].room_progression == 3:
				room_locations[location].description[1] = "You in a grand field that seems to stretch on forever. Towards the ends of the\n\
world, the ground seems to lilt into the sky. There is a standing table off to one side\n\
of the field that has one standing table with a microphone on it. There are three buttons\n\
on the table resembling a different image on each one: rock, paper, and scissors. An important\n\
path lies to the south."
				room_locations[location].allowed_exits = ["north", "south", "west"]
		elif location == (2, 3):
			if room_locations[location].room_progression == 1:
				room_locations[location].description[1] = "The walls of this room are adorned with copper pipes and gears. The floor looks to be\n\
made of a dark wood, but it is hard to tell with all of the pipes and gears. There is a\n\
large clock in the center of the room that ticks away, seemingly powered by steam. There\n\
are two doors in this room, one to the south and one to the east."
				room_locations[location].allowed_exits = ["east", "south"]
		elif location == (3, 3):
			if "orb" not in room_locations[location].item_pickups:
				room_locations[location].description[1] = "You enter a spacious chamber that crackles with magic. The walls are lined with shelves\n\
and purple drapes. There is a massive crystal chandelier that hangs from the ceiling,\n\
casting rainbows of light across the room."
	
	else:
		print(location)
		exit(404)


temp_room = Room(["north"])
temp_room.description = ["As you join into this strange new digital world, you feel as if you are being watched.",
"All around you are grand white pillars that seem to stretch high into the sky. The sky\n\
is painted a rich blend of light blues, fading to orange as the sun just barely starts\n\
to bite into the horizon. The grass at your feet is long and soft but still seems to be\n\
well maintained. As you look around, you see one, singular door, seeming to go nowhere,\n\
standing to the north."]
room_locations[(1, 1)] = temp_room

temp_room = Room(["east", "south"])
temp_room.description = ["You walk towards the tall, heavy wooden door and attempt to push it open. You hear a\n\
couple of clicks as it reluctantly slides open.",
"You enter a white room, a deep blue tile lining the bottom edges of the walls. You can\n\
feel a slight lean in the floor, as if to guide you to the drain in the room. The room\n\
seems to be well lit, but there is no obvious light source that you can see, almost as\n\
if the walls themselves are providing the light to illuminate the area. There is a large\n\
wooden door to the south and a lightly beaten dirt... trail to the east."]
temp_room.item_pickups = ["coin",
						"There is some shiny looking coin hanging from a string in the middle of the room.",
						"You yank the coin off of the string and put it into your pocket."]
room_locations[(1, 2)] = temp_room

temp_room = Room(["north"])
temp_room.description = ["You walk past the molten metal of the wall towards what looks to be a massive arena.",
						"You enter a grand coliseum, a large beast resides in the center. He is to be feared,\n\
though the slightest blade would peirce his hide. To win the game, you must eliminate the beast."]
temp_room.usable_items["blade"] = "You approach the beast, blade in hand. He seems to be unphased by your presence.\n\
he takes a step towards you and you swing your blade. It pierces his hide and he falls\n\
to the ground. You have won the game."
room_locations[(2, 1)] = temp_room

temp_room = Room(["north", "west"])
temp_room.description = ["You walk down the dirt trail from the hospital room. How strange a place for a path.", "\
You are now in a grand field that seems to stretch on forever. Towards the ends of the\n\
world, the ground seems to lilt into the sky. There is a standing table off to one side\n\
of the field that has a small slot in it, as if to guide you to put something into it.\n\
There is a large metalic wall to the south that seems to be blocking your path however\n\
you seem to be able to go in all other directions."]
temp_room.usable_items["coin"] = "You attempt to fit the coin into the thin slot on the box and it fits! There is a\n\
small ding and then the box seems to fold open, leaving a small microphone to be\n\
talked into. There are three small buttons that appear. They bear the following images:\n\
a rock, a piece of paper, and a pair of scissors."
temp_room.usable_items["orb"] = "You hold the orb up to the wall and watch as it melts away, revealing a new path."
room_locations[(2, 2)] = temp_room

temp_room = Room(["south"])
temp_room.description = ["As you are walking, you enter some steampunk area. An industrial fantasy you could say.", "\
The walls of this room are adorned with copper pipes and gears. The floor looks to be\n\
made of a dark wood, but it is hard to tell with all of the pipes and gears. There is a\n\
large clock in the center of the room that ticks away, seemingly powered by steam. There\n\
are two doors in this room, one to the south and one to the east. The east door is locked."]
temp_room.item_pickups = ["blade",
						"Upon further inspection, one of the clock hands seems to be made of a very sharp metal.",
						"You pull this makeshift blade off of the clock, sliding it into your pocket."]
temp_room.usable_items["key"] = "You slide the key into the lock of the east door and it clicks open. You suddenly\n\
hear hushed whispers come to an abrupt stop. The door slides itself open."
room_locations[(2, 3)] = temp_room

temp_room = Room(["west"])
temp_room.description = ["As you enter into the room, you feel a magical tingling sensation fall over you.", "\
You enter a spacious chamber that crackles with magic. The walls are lined with shelves\n\
and purple drapes. On a stack of dusty tomes, you see a small, glowing orb. It seems to\n\
invite you to pick it up. There is also a massive crystal chandelier that hangs from the\n\
ceiling, casting rainbows of light across the room. The glowing image of the orb seems to\n\
pulse and hum, giving you a bad feeling deep in your gut. A feeling of dread sets over you."]
temp_room.item_pickups = ["orb",
                          "The orb seems to be pulling you towards it, unrelenting.",
                          "You pick up the orb and it seems to pulse with energy. You feel a surge of power.\n\
You hear a loud, metalic screech, something important you would assume."]
room_locations[(3, 3)] = temp_room
