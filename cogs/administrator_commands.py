import discord
from discord.ext import commands, tasks




class administrator_cmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 

""" 
	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban( self ,ctx,member : discord.Member,*,reason= "No reason provided."):
		embed = discord.Embed(title = None,
	     description = f" *:white_check_mark: **{member.name}** was banned from {ctx.guild.name}, because of, {reason}*",
	      color = discord.Color.green())
		await member.ban(reason=reason)
		await ctx.send(embed=embed)


#unban
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self , ctx,*,member):
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
"""

def setup(bot):
    bot.add_cog(administrator_cmd(bot))