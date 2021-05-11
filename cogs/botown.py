import discord
import asyncio

from handlers import handlefiles
from discord.ext import commands



class Owners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = handlefiles.loadconfig()
        self.owners = self.config["ownerIds"]
    
    @commands.command(aliases=['activity','status'])
    async def do_activity(self, ctx, *, activity):
        
        ID = ctx.author.id
        
        if str(ID) in self.owners:
            await self.bot.change_presence(activity=discord.Game(name=activity))
            
            em = discord.Embed(
            description = f" *:white_check_mark: Bot's activity is changed to **{activity}***",
            color = discord.Color.green())
            
            await ctx.send(embed=em)
        else:
            return



def setup(bot):
	bot.add_cog(Owners(bot))