#
# FILENAME: commands.py | ServerBot
# DESCRIPTION: Custom slash (/) commands
# CREATED: 2021-06-03 @ 10:10 PM
# COPYRIGHT: Copyright (c) 2021 by Ryan Smith <rysmith2113@gmail.com>
#

import os, discord

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
	guild_ids=[850104153278644305], options=PING_OPTIONS
)
async def ping(ctx: SlashCommand, times=1):
	"""
		Ping the server.
		Usage: `/ping <times?>`
	"""
	for _ in range(times):
		await ctx.send(content=f"Query recieved ({round(client.latency * 1000)} ms)")

@client.command(
	name="info", description="Get info about the server.",
	guild_ids=[
		850104153278644305, 850104153278644307, 850116523381096448,
		850104800188170280, 850145316530683946
	],
	options=None
)
async def info(ctx: SlashCommand):
	"""
		Get info about the server.
		Usage: `/info`
	"""
	time, curr_date = datetime.now(), date.today()
	slice = 1 if int(time.strftime("%I")) >= 10 else 0
	print(type(slice))
	
	await ctx.send(content=
		f"Welcome to the {SERVER} server!\n" + \
		f"It is currently {curr_date.strftime('%B %d, %Y')} at {time.strftime('%I:%M %p')[slice:]}"
	)

client.run(TOKEN)
