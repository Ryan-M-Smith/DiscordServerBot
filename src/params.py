#
# FILENAME: params.py | ServerBot
# DESCRIPTION: Parameter lists (list of dictionaries) for commands
# CREATED: 2021-06-04 @ 12:23 AM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

PING_OPTIONS = [
	{
		"name": "times",
		"description": "The number of times to ping",
		"required": False,
		"type": 4
	}
]

GREET_OPTIONS = [
	{
		"name": "member",
		"description": "The member to greet",
		"required": True,
		"type": 9
	}
]

EIGHTBALL_OPTIONS = [
	{
		"name": "question",
		"description": "A question to ask the magic 8-ball",
		"required": True,
		"type": 3
	}
]

DICEROLL_OPTIONS = [
	{
		"name": "count",
		"description": "The number of dice to roll",
		"required": False,
		"type": 4
	},
	
	{
		"name": "sides",
		"description": "The number of sides the die will have",
		"required": False,
		"type": 4
	}
]