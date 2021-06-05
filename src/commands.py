#
# FILENAME: commands.py | ServerBot
# DESCRIPTION: Custom slash (/) commands
# CREATED: 2021-06-03 @ 10:10 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import os
from typing import NoReturn
from random import choice

from discord import Member
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext, SlashCommandOptionType
from dotenv import load_dotenv
from datetime import datetime, date

from params import *

load_dotenv("../.env")
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

client = commands.Bot(command_prefix="/")
slash = SlashCommand(client)

@client.command(
	name="ping", description="Ping the server.",
	guild_ids=[850104152679252006], options=PING_OPTIONS
)
async def ping(ctx: SlashCommand, times=1) -> NoReturn:
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
		"It is Certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely."
		"You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good."
		"Yes.", "Signs point to yes."

		# Non-commital
		"Reply hazy, try again.", "Ask again later.", "Better not tell you now."
		"Cannot predict now.", "Concentrate and ask again."

		# Negative
		"Don't count on it.", "My reply is no.", "My sources say no."
		"Outlook not so good.", "Very doubtful."
	]

	await ctx.send(f"Magic 8-ball: {choice(RESPONSES)}")

client.run(TOKEN)
