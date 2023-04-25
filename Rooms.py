from numpy import array

INPUT_HELP = {"north": "\nUsed to move the character up by one room.\n",
		"east": "\nUsed to move the character to the right by one room.\n",
		"south": "\nUsed to move the character down by one room.\n",
		"west": "\nUsed to move the character to the left by one room.\n",
		"grab": "\nLets the player try to grab an item from the room that they are in\n",
		"use": "\nLets the player try to use a specified object.\n",
		"room": "\nUsed to re-display the current locations text.\n",
		"help": "\nUsed to display a list of available commands as well as the option to give more details\
		\non a command if the player asks for it.\n"}
DIRECTIONS = {"north": array([0, 1]),
			"east": array([1, 0]),
			"south": array([0, -1]),
			"west": array([-1, 0])}


class Room:
	"""
	Room class for building new rooms
	"""
	def __init__(self):
		self.item_pickups = []  # items to pick up, description text
		self.usable_items = {}  # item name, usage text
		self.allowed_exits = []  # allowed direction to leave the room
		self.description = ""  # description of this room
	
	def use_item(self, player):
		"""
		Used to attempt to use an item that is prompted from the user.
		Returns a statement depending on validity and usage.
		:param player: The player that is being used.
		:return:
		"""
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
					print(self.usable_items[to_use])
					player.inventory.remove(to_use)
					del self.usable_items[to_use]
				else:
					print("That item cannot be used here.")
			else:
				print("That item is not in your inventory.")
		else:
			print("You have nothing to use.")