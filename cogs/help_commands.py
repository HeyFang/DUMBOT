import discord
from discord.ext import commands, tasks




class handle_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    # FIXME : sooner add help

def setup(bot):
    bot.add_cog(handle_help(bot))


    