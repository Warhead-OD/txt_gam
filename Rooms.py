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
