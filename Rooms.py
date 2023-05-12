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
		print(player.cur_location)
		if choice in self.allowed_exits:
			player.cur_location = DIRECTIONS[choice]
			print(player.cur_location)
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
		
		# prints the main bulk of the room description
		print(self.description[1])
		# prints any pick-able items that are in the room
		if self.item_pickups:
			print(self.item_pickups[1])
		
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


room_locations = {}  # stores the location of each room object to be called on

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

temp_room = Room(["west"])
temp_room.description = ["You walk down the dirt trail from the hospital room. How strange a place for a path.", "\
You are now in a grand field that seems to stretch on forever. Towards the ends of the\n\
world, the ground seems to lilt into the sky. There is a standing table off to one side\n\
of the field that has a small slot in it, as if to guide you to put something into it."]
temp_room.usable_items["coin"] = "You attempt to fit the coin into the thin slot on the box and it fits! There is a\n\
small ding and then the box seems to fold open, leaving a small microphone to be\n\
talked into. There are three small buttons that appear. They bear the following images:\n\
a rock, a piece of paper, and a pair of scissors."
room_locations[(2, 2)] = temp_room


def room_code(location):
	"""
	Runs the unique code on a per-room basis.
	Based on the items that have been used on the room.
	:param location: Is the player's current location
	:return:
	"""
	global room_locations
	if location in room_locations:
		if location == (2, 2):
			for room in room_locations:
				print(f"{room}: {room_locations[room]}")
			print("\n\n")
			room_locations[location].description[1] = "WOO HOO"
			print("\n\n")
			for room in room_locations:
				print(f"{room}: {room_locations[room]}")
			
	else:
		print(location)
		exit(404)
