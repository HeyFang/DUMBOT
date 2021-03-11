""" Bots main handler """

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


#status
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


@bot.command()
async def ping(ctx):
    """ Bot latency cheack """
    latency = round(bot.latency*1000, 1)
    await ctx.send(f"Pong! `{latency}ms`")
    
   


#Repeatmessage cmd imported from alice...
@bot.command()
@commands.has_permissions(administrator= True)
async def repeatmessage(ctx, enabled="start", interval=15, message=""):
    if enabled.lower() == "stop":
        messageInterval.stop()
    elif enabled.lower() == "start":
        messageInterval.change_interval(seconds=int(interval))
        messageInterval.start(ctx,message)
@tasks.loop(seconds=15)
async def messageInterval(ctx,message):
    await ctx.send(message)



#cmd mute
@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    
    em = discord.Embed(title = None,
     description = f" *:white_check_mark: **{member.mention}** was muted for reason {reason}*",
      color = discord.Color.green())

    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"You were muted in the server {guild.name} for {reason}")
    await ctx.send(embed=em)


#unmute
@bot.command(description="unmutes user")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    em = discord.Embed(title = None,
     description = f" *:white_check_mark: **{member.mention}** was successfully unmuted!*",
      color = discord.Color.green())

    await member.remove_roles(mutedRole)
    await member.send(f"You were unmuted in the server {ctx.guild.name}")
    await ctx.send(embed=em)







#cmd serverinfo imported from alice...
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








@bot.command()
async def info(ctx):
    embed=discord.Embed(title="PALICE: **P**ranav n __**A**__ryan's __**L**__earned __**I**__ntellectual __**C**__ollaberating __**E**__mulator.", 
        url="https://realdrewdata.medium.com/", 
        description="Heya Dumbos, am Palice: A modified version", 
        color=0x11aaf5)

    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="Fang", url="https://discord.gg/FCcKuWB8x6", 
        icon_url="https://cdn.discordapp.com/avatars/587188931762716674/42db4e4562948267dbbd69df9913723b.png")

    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/817402985859514399/1233c748fb8bf08ea67cb42632f02093.webp")

    embed.add_field(name="Version", value="1.0.0", inline=False) 
    embed.add_field(name="Creator", value="Fang", inline=True)
    embed.add_field(name="Co-creator", value="Pranav", inline=True)
    embed.add_field(name="Invite-Link", value="Not a public bot yet ;)", inline=False)
    embed.add_field(name="Help Server", value="https://discord.gg/FCcKuWB8x6", inline=False)
    await ctx.send(embed=embed)


    

########____MODERATIONS____#############

#ban command imported from alice...
@bot.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason= "No reason provided."):
    embed = discord.Embed(title = None,
     description = f" *:white_check_mark: **{member.name}** was banned from {ctx.guild.name}, because of, {reason}*",
      color = discord.Color.green())
    await member.ban(reason=reason)
    await ctx.send(embed=embed)


#unban
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            embed = discord.Embed(title = None,
            description = f" *:white_check_mark: **{user.name}** was unbanned from {ctx.guild.name}.*",
            color = discord.Color.green())

            await ctx.send(embed=embed)
            return

    await ctx.send(member+" was not found")






#cmd kick
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason= "No reason provided."):
            embed = discord.Embed(title = None,
            description = f" *:white_check_mark: **{member.name}** was kicked from {ctx.guild.name} of, {reason}*",
            color = discord.Color.green())

            await ctx.send(embed=embed)

            await member.kick(reason=reason)
















































bot.run(token)
#A dumbot made by fang n pranav...


