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

from params import *

load_dotenv("../.env")
TOKEN = os.getenv("DISCORD_TOKEN")

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

client.run(TOKEN)