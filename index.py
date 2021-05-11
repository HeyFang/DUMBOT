import discord
import os
import json

from discord.ext import commands
from discord.ext.commands import Bot
from handlers.handlefiles import get_server_prefix
from handlers.handlefiles import loadconfig




bot = Bot(command_prefix = get_server_prefix)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")
    await add_cogs()


async def add_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                bot.load_extension("cogs.{}".format(file[:-3]))
                print(f"loded {file}")
            except Exception as e: print(e)




@bot.command(aliases=['addcog'])
async def loadcog(ctx, cog: str = None):
    try:
        bot.load_extension(f"cogs.{cog}")
        print(f"{cog} loded")
    except Exception as e: print(e)



@bot.command(aliases=["removecog"])
async def unloadcog(ctx, cog: str = None):
    try:
        bot.unload_extension(f"cogs.{cog}")
        print(f"{cog} unloded")
    except Exception as e: print(e)




Token = loadconfig()["Token"]
bot.run(Token)