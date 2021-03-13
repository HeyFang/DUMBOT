import discord
from discord.ext import commands, tasks


class avatar(commands.Cog):
	def __init__(self, bot):
		self.bot = bot


	@commands.command(name='avatar', aliases=['Avatar', 'av'])
	async def av_cmd(self, ctx, user: discord.Member = None):
		"""avatar function returns profile url """
		if user is None:
			user = ctx.message.author
			em = discord.Embed(color=0x11aaf5,title = f"{user}")
			em.set_image(url=f"{user.avatar_url}")
			await ctx.send(embed=em)
 	       
		else:
			emm = discord.Embed(color=0x11aaf5,title = f"{user}")
			emm.set_image(url=f"{user.avatar_url}")
			await ctx.send(embed=emm)
	
	
	
	@commands.command()
	async def ping(self , ctx):
		""" Bot latency cheack """
		latency = round(self.bot.latency*1000, 1)
		em = discord.Embed(color=0x11aaf5  )
		em.add_field(name = 'latency',  value=f" pong!  , {latency}", inline=False)
		await ctx.send(embed = em)


def setup(bot):
    bot.add_cog(avatar(bot))