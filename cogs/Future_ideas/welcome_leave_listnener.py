import discord
from discord.ext import commands, tasks

class listen_join_leave(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_member_join(self, member):
		print('joined')
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send(f'OwO {member}')




def setup(bot):
    bot.add_cog(listen_join_leave(bot))
    
    
    
    