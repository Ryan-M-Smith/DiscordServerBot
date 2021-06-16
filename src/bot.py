#
# FILENAME: bot.py | ServerBot
# DESCRIPTION: Allow the bot to connect and interface with Discord
# CREATED: 2021-06-03 @ 8:08 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import os, sys
from pathlib import Path
from typing import NoReturn
from multiprocessing import Process, Event

import discord
from dotenv import load_dotenv

# NOTE: Import differently for Docker builds
#import commands
from . import commands

# Load the tokens from the environment
load_dotenv(Path(".env"))
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready() -> NoReturn:
	""" A "ready" message. """
	print(f"{client.user} is online")
	channel = client.get_channel(850104153278644305)
	await channel.send(f"{client.user} hopped online")

@client.event
async def on_member_join(member: discord.Member) -> NoReturn:
	""" Display a message when a new user joins the server """
	channel = client.get_channel(850104153278644305)
	await member.create_dm()
	await channel.send(f"What's poppin\', {member.name}? Welcome to Infinitely Sus!")

def main(event: Event) -> NoReturn:
	""" Run the server events. """

	event.wait()
	print("Server events active.")
	client.run(TOKEN)

def run() -> NoReturn:
	""" Simultaneously run the server events and the slash commands. """

	py_version = sys.version_info

	# Print some info to the terminal 
	print("DiscordServerBot - Copyright (c) 2021 by Ryan Smith")
	print(f"Running with Python {py_version.major}.{py_version.minor}.{py_version.micro}")
	print("-" * 51) # A divider (creates 51 dashes)

	event = Event()

	# Get both file's main functions
	bot, slash_commands = Process(target=main, args=tuple([event])), Process(target=commands.main, args=tuple([event]))

	# Start the processes
	bot.start()
	slash_commands.start()

	event.set() # Start the event

if __name__ == "__main__":
	sys.exit(run())