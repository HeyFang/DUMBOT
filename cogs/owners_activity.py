import discord
from discord.ext import commands, tasks




class owner_activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
        
        """
        will work on it soon 
        """
        


def setup(bot):
    bot.add_cog(owner_activity(bot))