#imma fang tn this is Palice
import discord
from discord.ext import commands, tasks
from itertools import cycle
import random
import os
import json
#helosadiwjaosdwa
#sjsjwjsjjssnsnsn
#jsjsksks
if os.path.exists(os.getcwd() + "/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplete = {"Token": "", "Prefix": ":", "noPing": []}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplete, f)

token = configData["Token"]
prefix = configData["Prefix"]

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")


@bot.event
async def on_ready():
	print('Bot is online')


#load cogs
@bot.command()
@commands.has_permissions(administrator=True)
async def loadcog(ctx, cog):
    bot.load_extension(f"cogs.{cog}")
    em = discord.Embed(title = None,
    description = f" *:white_check_mark: **{cog}** is now loaded!*",
    color = discord.Color.green())
    await ctx.send(embed=em) 



@bot.command()
async def unloadcog(ctx, cog):
    bot.unload_extension(f"cogs.{cog}")
    em = discord.Embed(title = None,
    description = f" *:white_check_mark: **{cog}** is now unloaded!*",
    color = discord.Color.green())
    await ctx.send(embed=em) 

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")



#cmd activity
@bot.command()
@commands.has_permissions(administrator=True)
async def activity(ctx,*,activity):

    await bot.change_presence(activity=discord.Game(name=activity))

    em = discord.Embed(title = None,
    description = f" *:white_check_mark: Bot's activity is changed to **{activity}***",
    color = discord.Color.green())

    await ctx.send(embed=em)



bot.run(token)