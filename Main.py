from numpy import array

import Rooms

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
