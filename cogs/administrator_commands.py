import discord
from discord.ext import commands, tasks




class administrator_cmd(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 		
		
		
	@commands.command()
	@commands.has_permissions(administrator = True)
	async def clear(self , ctx , amount = 5):
		"""clears the chat """
		await ctx.channel.purge(limit=amount+1)
		
		
		
	@commands.command()
	@commands.has_permissions(ban_members = True)
	async def ban( self ,ctx,member : discord.Member,*,reason= "No reason provided."):
		"""bans the client"""
		embed = discord.Embed(title = None,
	     description = f" *:white_check_mark: **{member.name}** was banned from {ctx.guild.name}, because of, {reason}*",
	      color = discord.Color.green())
		await member.ban(reason=reason)
		await ctx.send(embed=embed)
		
		
		
	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unban(self , ctx,*,member):
		"""unbans the client """
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
		
		
	@commands.command()
	@commands.has_permissions(kick_members = True)
	async def kick(self , ctx,member : discord.Member,*,reason= "No reason provided."):
		embed = discord.Embed(title = None,
		description = f" *:white_check_mark: **{member.name}** was kicked from {ctx.guild.name} of, {reason}*",
		color = discord.Color.green())
		
		await ctx.send(embed=embed)
		
		await member.kick(reason=reason)
	
	
	@commands.command(description="Mutes the specified user.")
	@commands.has_permissions(manage_messages=True)
	async def mute(self , ctx, member: discord.Member, *, reason=None):
		"""mutes the user """
		
		guild = ctx.guild
		mutedRole = discord.utils.get(guild.roles, name="Muted")
		
		
		if not mutedRole:
			mutedRole = await guild.create_role(name="Mute")
			for channel in guild.channels:
				await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
		
		em = discord.Embed(title = None,
		 description = f" *:white_check_mark: **{member.mention}** was muted for reason {reason}*",
		  color = discord.Color.green())
		
		await member.add_roles(mutedRole, reason=reason)
		#channel = await member.create_dm()
		#await channel.send(f"You were muted in the server {guild.name} for {reason}")
		await ctx.send(embed=em)
		
		

	@commands.command(description="unmutes user")
	@commands.has_permissions(manage_messages=True)
	async def unmute(self , ctx, member: discord.Member):
		"""unmutes the user """
		
		mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
		
		em = discord.Embed(title = None,
		description = f" *:white_check_mark: **{member.mention}** was successfully unmuted!*",
		color = discord.Color.green())
		
		await member.remove_roles(mutedRole)
		#await member.send(f"You were unmuted in the server {ctx.guild.name}")
		await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(administrator_cmd(bot))