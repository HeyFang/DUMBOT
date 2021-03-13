import discord
from discord.ext import commands, tasks




class handle_help(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 
		
	@commands.command(aliases=['help'])
	async def help_client(self , ctx):
		"""helps client to see commands help"""
		embed=discord.Embed(title="Help : ", 
	        color=0x11aaf5)
		"""work on it soon"""
		await ctx.send(embed=embed)
	
def setup(bot):
    bot.add_cog(handle_help(bot))