""" Bots main handler """

import discord
from discord.ext import commands, tasks
from itertools import cycle
import random,	os,	json



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




@bot.event
async def on_ready():
	"""" ready events to test  """
	print('Bot is online')


#cogs...
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




#activity...
@bot.command(
aliases=['activity','status']
)
@commands.has_permissions(administrator=True)
async def do_activity(ctx,*,activity):
    """activity/status handler"""
    await bot.change_presence(activity=discord.Game(name=activity))
    
    em = discord.Embed(
    description = f" *:white_check_mark: Bot's activity is changed to **{activity}***",
    color = discord.Color.green())
    
    await ctx.send(embed=em)




#ping...
@bot.command()
async def ping(ctx):
    """ Bot latency cheack """
    latency = round(bot.latency*1000, 1)
    await ctx.send(f"Pong! `{latency}ms`")
	



#cmd serverinfo
@bot.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    owner = ctx.guild.owner_id
    owner = await bot.fetch_user(owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)
    role_count = len(ctx.guild.roles)
    icon = str(ctx.guild.icon_url)
           
    embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=0x11aaf5
        )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name='Created At', value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=False)
    embed.add_field(name='Number of roles', value=str(role_count), inline=True)
    embed.add_field(name='Highest role', value=ctx.guild.roles[-2], inline=True)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)

    await ctx.send(embed=embed)




















bot.run(token)
#A dumbot made by fang n pranav...