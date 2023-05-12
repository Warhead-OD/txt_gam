from Rooms import Room, room_locations, DIRECTIONS
import pickle
import json

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


class PointEncoderP(json.JSONEncoder):
	def default(self, obj):
		return [obj.inventory, obj.cur_location]


class PointEncoderR(json.JSONEncoder):
	def default(self, obj):
		return [obj.explored, obj.description, obj.item_pickups, obj.usable_items, obj.allowed_exits]


def save_game():
	with open("game_stats.json", "w") as f:
		data_dict = {"p_data": player, "r_data": room_locations}
		print(data_dict)
		data_dict = json.dumps(data_dict["p_data"], cls=PointEncoderP)
		data_dict += json.dumps(data_dict["r_data"], cls=PointEncoderR)
		json.dump(data_dict, f)


def load_game():
	with open("game_stats.json", "r") as f:
		global player
		global room_locations
		# global data_dict
		
		data_dict = json.load(f)
		print(data_dict)
		player = data_dict["p_data"]
		room_locations = data_dict["r_data"]


def main():
	"""
	The main running function that is used to run the game.
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
			print(player.cur_location)
		
		elif choice == "load":
			load_game()
			print(player.cur_location)
		
		elif choice == "quit":
			pass


if __name__ == "__main__":
	main()
