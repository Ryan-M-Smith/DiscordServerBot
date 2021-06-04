#
# FILENAME: bot.py | ServerBot
# DESCRIPTION: Allow the bot to connect and interface with Discord
# CREATED: 2021-06-03 @ 8:08 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import os, discord

from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

from typing import NoReturn
from dotenv import load_dotenv

# Load the tokens from the environment
load_dotenv("../.env")
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER = os.getenv("DISCORD_SERVER")

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready() -> NoReturn:
	""" A "ready" message. """
	print(f"{client.user} hopped online")
	channel = client.get_channel(850104153278644305)
	await channel.send(f"{client.user} hopped online")

@client.event
async def on_member_join(member: discord.Member) -> NoReturn:
	""" Display a message when a new user joins the server """
	channel = client.get_channel(850104153278644305)
	await member.create_dm()
	await channel.send(f"What's poppin\', {member.name}? Welcome to Infinitely Sus!")

@client.event
async def 

client.run(TOKEN)