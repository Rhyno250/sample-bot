import discord

from discord.ext import commands, tasks
from itertools import cycle

import os

client = commands.Bot(command_prefix = "pg")
status = cycle(["Having a party with Popcorn Gang"])

#Events

@client.event
async def on_ready():
    change_status.start()
    print("Logged in as")
    print(client.user.name)
    print("-----------")

@tasks.loop(seconds=3600)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#commands

#---------------------------

for cog in os.listdir(r"./cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            client.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

client.run("Njc1NzczNDMyODU5NzIxNzU4.Xj8ckQ.WuaYAzlWUQEts7TgZslbb75jzjQ")
