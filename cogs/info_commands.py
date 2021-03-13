import discord
from discord.ext import commands, tasks




class handle_info(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 
		
	@commands.command(aliases=['botinfo'])
	async def do_botinfo(self , ctx):
		embed=discord.Embed(title="PALICE: **__P__**ranav n **__A__**ryan's **__L__**earned **__I__**ntellectual **__C__**ollaberating **__E__**mulator.", 
	        url="http://cyclones.ml/", 
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

		
		
		
	@commands.command()
	async def serverinfo(self , ctx):
		
		name = str(ctx.guild.name)
		description = str(ctx.guild.description)
		owner = str(ctx.guild.owner)
		
		
		
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
		#embed.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
		await ctx.send(embed=embed)
	    
	@commands.command(aliases=['user'])
	async def whois(self, ctx, member : discord.Member):
		embed = discord.Embed(title = member.name , description = member.mention ,	color=0x11aaf5)
		embed.add_field(name = "ID", value = member.id , inline = True )
		embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M  UTC"))
		embed.set_thumbnail(url = member.avatar_url)
		embed.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author.name}")
		embed.add_field(name="Nickname:", value=member.display_name)
		embed.add_field(name="Joined Server On:", value=(member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")))
		
		roles = [role.mention for role in member.roles[1:]]  
		if len(member.roles[1:]) < 1:
		    embed.add_field(name=f"Roles:",value="None", inline=False)
		    embed.add_field(name="Highest Role:", value="None")
		elif roles != None:
		    embed.add_field(name=f"Roles({len(roles)}):",value=",".join(roles), inline=False)
		    embed.add_field(name="Highest Role:", value=member.top_role.mention)
		await ctx.send(embed=embed)
        
        
        
        
        

def setup(bot):
    bot.add_cog(handle_info(bot))