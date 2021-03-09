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
        

def setup(bot):
    bot.add_cog(info(bot))