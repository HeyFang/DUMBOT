""" Bot's main handler """

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random,	os,	json


""" Bot Token / prefiz confugs"""
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplete = {"Token": "", "Prefix": "?", "noPing": []}
    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplete, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command('help')

@bot.event
async def on_ready():
	"""" ready events to test  """
	print('Bot is online')


@bot.command()
@commands.has_permissions(administrator=True)
async def loadcog(ctx, cog):
    """ load logs handler """
    bot.load_extension(f"cogs.{cog}")
    em = discord.Embed(
    description = f" *:white_check_mark: **{cog}** is now loaded!*",
    color = discord.Color.green())
    await ctx.send(embed=em)


@bot.command()
@commands.has_permissions(administrator=True)
async def unloadcog(ctx, cog):
    """ unload cogs handler """
    bot.unload_extension(f"cogs.{cog}")
    em = discord.Embed(
    description = f" *:white_check_mark: **{cog}** is now unloaded!*",
    color = discord.Color.green())
    await ctx.send(embed=em) 

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")












bot.run(token)

