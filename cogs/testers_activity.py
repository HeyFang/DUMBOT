import discord
from discord.ext import commands, tasks


bot_testing_access = ['782922046669193256' , '587188931762716674']




class owner_activity(commands.Cog):
	def __init__(self, bot):
		self.bot = bot 
	
	@commands.command(
aliases=['activity','status'])
	async def do_activity(self , ctx,*,__activity):
		
		acces_id = ctx.author.id
		print(acces_id)
		
		if str(acces_id) in bot_testing_access:
			await self.bot.change_presence(activity=discord.Game(name=__activity))
			
			em = discord.Embed(
			description = f" *:white_check_mark: Bot's activity is changed to **{__activity}***",
			color = discord.Color.green())
			
			await ctx.send(embed=em)
		else:
			print('acces_cheack_faild')
			print(bot_testing_access)



def setup(bot):
	bot.add_cog(owner_activity(bot))