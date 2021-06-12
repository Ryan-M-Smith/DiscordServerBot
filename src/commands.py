#
# FILENAME: commands.py | ServerBot
# DESCRIPTION: Custom slash (/) commands
# CREATED: 2021-06-03 @ 10:10 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import os, secrets, sys

from typing import List, NoReturn, Optional
from random import choice, randint, randrange
from datetime import datetime, date
from params import *

import discord

from discord import Member
from discord.ext import commands
from discord.utils import get
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
from dotenv import load_dotenv

load_dotenv("../.env")
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="/", intents=intents)
slash = SlashCommand(client)

@client.command(
	name="ping", description="Ping the server.",
	guild_ids=[850104152679252006], options=PING_OPTIONS
)
async def ping(ctx: SlashCommand, times: int = 1) -> NoReturn:
	"""
		Ping the server.
		Usage: `/ping <times?>`
	"""
	for _ in range(times):
		await ctx.send(content=f"Query recieved ({round(client.latency * 1000)} ms)")

@client.command(
	name="info", description="Get info about the server.",
	guild_ids=[850104152679252006], options=None
)
async def info(ctx: SlashCommand) -> NoReturn:
	"""
		Get info about the server.
		Usage: `/info`
	"""
	time, curr_date = datetime.now(), date.today()
	slice = 0 if int(time.strftime("%I")) >= 10 else 1

	await ctx.send(content=
		f"Welcome to the {SERVER} server!\n" + \
		f"It is currently {curr_date.strftime('%B %d, %Y')} at {time.strftime('%I:%M %p')[slice:]}"
	)

@client.command(
	name="greet", description="Greet a user.",
	guild_ids=[850104152679252006], options=GREET_OPTIONS
)
async def greet(ctx: SlashCommand, member: Member) -> NoReturn:
	"""
		Greet a user.
		Usage: `/greet @<member>`
	"""
	await ctx.send(f"Greetings, {member.name}! How's life?")

@client.command(
	name="8ball", description="Simulate a magic 8-ball.",
	guild_ids=[850104152679252006], options=EIGHTBALL_OPTIONS
)
async def eight_ball(ctx: SlashCommand, _: str) -> NoReturn: # The command input (question) is just for looks, and is ignored here
	"""
		Simulate a magic 8-ball
		Usage: `/8ball <question>`
	"""

	#
	# The typical 8-ball responses, found at https://en.wikipedia.org/wiki/Magic_8-Ball#Possible_answers.
	# There are 20 possible answers, comprised of:
	#	* 10 affirmative
	#	* 5 non-commital
	#	* 5 negative
	#
	RESPONSES = [
		# Affirmative
		"It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.",
		"You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
		"Yes.", "Signs point to yes.",

		# Non-commital
		"Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
		"Cannot predict now.", "Concentrate and ask again.",

		# Negative
		"Don't count on it.", "My reply is no.", "My sources say no.",
		"Outlook not so good.", "Very doubtful."
	]

	await ctx.send(f"Magic 8-ball: {choice(RESPONSES)}")

@client.command(
	name="roll", description="Roll a user-specified amount of dice of a user-specified side count.",
	guild_ids=[850104152679252006], options=DICEROLL_OPTIONS
)
async def diceroll(ctx: SlashCommand, count: int = 1, sides: int = 6) -> NoReturn:
	"""
		Roll a die (or dice). The user can specify the amount of dice to roll as well
		as how many sides each die should have. This command allows the user to roll a
		die with a side count of 4, 6, 8, 10, 12, or 20.
		Usage: `/roll <sides?>
	"""

	def display(_list: List[int]) -> str:
		""" Customize how a list is displayed. """
		return ', '.join(list(map(lambda n: str(n), _list)))

	DIE_SIDE_COUNTS = [4, 6, 8, 10, 12, 20]

	# Rolling 0 dice is useless, and rolling negative dice is impossible 
	if count <= 0:
		await ctx.send(f"Dice roll: not possible to roll {count} dice")
		return
	
	# Only certain side counts are allowed to be rolled
	if sides not in DIE_SIDE_COUNTS:
		await ctx.send(f"Dice roll: rolling a {sides}-sided die is not allowed")
		return
	
	await ctx.send(f"Rolling {count} {sides}-sided {'dice' if count > 1 else 'die'}") # Maintain grammatical correctness :)

	result = list()

	# Calculate the results
	for _ in range(count):
		result.append(randrange(1, sides))

	await ctx.send(f"Result: {display(result)}") # Display the answer

@client.command(
	name="rage", description="Expell rage in the server.",
	guild_ids=[850104152679252006], options=None,
	pass_context=True
)
async def rage(ctx: SlashCommand) -> NoReturn:
	"""
		Rage on the server.
		Usage: `/rage`
	"""

	await ctx.send(f"{ctx.message.author} is raging!")

	for _ in range(randint(10, 15)):
		await ctx.send(secrets.token_hex(nbytes=16)) # Simulate keymashing

@client.command(
	name="calm", description="Be calm in the server.",
	guild_ids=[850104152679252006], options=None,
	pass_context=True
)
async def calm(ctx: SlashCommand) -> NoReturn:
	"""
		Be calm on the server
		Usage: `/calm`
	"""

	member = ctx.message.author # The command sender

	# NOTE: The only works if you have a role with this exact name
	if get(ctx.guild.roles, name="[ZEN]"):
		# Give that user the zen role
		role = discord.utils.get(ctx.message.guild.roles, name="[ZEN]")
		await ctx.message.author.add_roles(role)
	
	await ctx.send(f"{member} is being calm. Do not disturb their zen state.")

@client.command(
	name="random", description="Display a random number.",
	guild_ids=[850104152679252006], options=RANDOM_OPTIONS
)
async def random(ctx: SlashCommand, lower: int = -sys.maxsize, upper: int = sys.maxsize):
	"""
		Print a random number in the range [lower, upper]
		Usage: `/random <lower?> <upper?>
	"""

	await ctx.send(f"Your random number is: {randint(lower, upper)}")

client.run(TOKEN)
