import discord
import os
import json

from discord.ext import commands
from handlers.handlefiles import get_server_prefix


bot = commands.Bot(command_prefix = get_server_prefix)

@bot.event
async def on_ready():
    print("_______________")
    print(f"{bot.user.name} is online")
    print("_______________")
    await add_cogs()

async def add_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try: 
                bot.load_extension("cogs.{}".format(file[:-3]))
                print(f"loded {file}")
            except Exception as e: print(e)









@bot.command(aliases=["removecog"])
async def unloadcog(ctx, cog: str = None):
	
	if cog == None:
		em = discord.Embed(
		description = "Must Specify Cog to unload",
		color = discord.Color.red())
		
		await ctx.send(embed = em)
		return
		
	try:
		
		bot.unload_extension(f"cogs.{cog}")
		
		em = discord.Embed(
		description = f" *:white_check_mark: **{cog}** is now unloaded!*",
		color = discord.Color.green())
		
		await ctx.send(embed = em)
	except Exception as e: print(e)





with open("./config.json") as f:
	configs = json.load(f)
	Token = configs["Token"]

bot.run(Token)