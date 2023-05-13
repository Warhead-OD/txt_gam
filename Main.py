from Rooms import Room, room_locations, DIRECTIONS
import pickle


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


data_dict = {}
player = Player()


def save_game():
	"""
	Saves the game to a file
	:return:
	"""
	global player, room_locations
	data_dict["p_data"] = player
	data_dict["r_data"] = room_locations
	with open("game_stats.dat", "wb") as f:
		pickle.dump(data_dict, f)


def load_game():
	"""
	Loads the game from a file
	:return:
	"""
	global player, room_locations, data_dict
	with open("game_stats.dat", "rb") as f:
		data_dict = pickle.load(f)
	player = data_dict["p_data"]
	room_locations.update(data_dict["r_data"])


def main():
	"""
	The main running function that is used to run the game.
	:return:
	"""
	global player, room_locations
	
	print("\nWelcome to my humble Text Game!\n")
	
	if input("Would you like the list of commands to the game? yes/no\n") == "yes":
		Room.help_description()
	
	Room.room_description(room_locations.get(player.cur_location), player.cur_location)
	
	choice = ""
	while choice != "quit":
		room = room_locations.get(player.cur_location)
		choice = input("What would you like to do (Use only 1 word)\n")
		if choice in DIRECTIONS:
			if room.movement(player, choice):
				room = room_locations.get(player.cur_location)
				room.room_description(player.cur_location)
		
		elif choice == "use":
			room.use_item(player)
		
		elif choice == "grab":
			room.pick_item(player)
		
		elif choice == "room":
			room.room_description(player.cur_location)
		
		elif choice == "help":
			room.help_description()
		
		elif choice == "save":
			save_game()
			print("\nGame Saved\n")
		
		elif choice == "load":
			load_game()
			print("\nGame Loaded\n")
		
		elif choice == "quit":
			pass
		
		else:
			print("\nInvalid Input\n")


if __name__ == "__main__":
	main()
