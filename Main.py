from Rooms import Room, room_locations, DIRECTIONS

# Formatted as (visited, story progression)
# Starting Screen,
#
# world_location_data = ###
#
#
world_items = []


class Player:
	"""
	Player class for creating a new player
	"""
	def __init__(self):
		self.inventory = []
		self._cur_location = (1, 1)
	
	@property
	def cur_location(self):
		return tuple(self._cur_location)
	
	@cur_location.setter
	def cur_location(self, direction):
		self._cur_location += direction


player = Player()


def main(player_data):
	"""
	The main running function that is used to run the game.
	:param player_data: The current players object variables
	:return:
	"""
	print("\nWelcome to my humble Text Game!\n")
	
	if input("Would you like the list of commands to the game? yes/no\n") == "yes":
		Room.help_description()
	
	Room.room_description(room_locations.get(player.cur_location), player.cur_location)
	
	choice = ""
	while choice != "quit":
		room = room_locations.get(player.cur_location)
		choice = input("What would you like to do (Use only 1 word)\n")
		if choice in DIRECTIONS:
			if room.movement(player_data, choice):
				room = room_locations.get(player.cur_location)
				room.room_description(player.cur_location)
		elif choice == "use":
			room.use_item(player_data)
		elif choice == "grab":
			room.pick_item(player_data)
		elif choice == "room":
			room.room_description(player.cur_location)
		elif choice == "help":
			room.help_description()
		elif choice == "save":
			pass
		elif choice == "load":
			pass
		elif choice == "quit":
			pass


if __name__ == "__main__":
	main(player)
