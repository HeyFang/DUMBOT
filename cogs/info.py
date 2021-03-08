import discord
from discord.ext import commands, tasks




class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
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
        
    @commands.command()
    async def serverinfo(self,	ctx):
    	name = str(ctx.guild.name)
    	description = str(ctx.guild.description)
    	owner = str(ctx.guild.owner)
    	owner = ctx.guild.owner_id
#    	owner = await ctx.author.fetch_user(owner)
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
    	
    	embed.add_field(
    	name="Owner", 	
    	value=owner, inline=True
    	)
    	
    	embed.add_field(
    	name="Server ID", 
    	value=id, inline=True
    	)
    	
    	embed.add_field(
    	name="Region",
    	value=region,
    	inline=True
    	)
    	
    	embed.add_field(
    	name="Member Count",
    	value=memberCount, inline=True
    	)
    	
    	embed.add_field(
    	name='Number of roles',
    	value=str(role_count),
    	inline=True
    	 )
    	 
    	embed.add_field(
    	 name='Highest role',
    	 value=ctx.guild.roles[-2],
    	 inline=True
    	 )
    	 
    	embed.set_author(
    	 name=ctx.author.name,
    	 icon_url=ctx.author.avatar_url
    	 )
    	 
    	embed.set_footer(
     	text=ctx.message.author.name,		 
    	 icon_url=ctx.message.author.avatar_url
    	 )
   	 
    	await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(info(bot))