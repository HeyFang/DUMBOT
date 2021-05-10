from discord.ext import commands
from handlers.handlefiles import *

import discord



class handle_events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        
        prefixes = load("prefixes.json")
        prefixes[str(guild.id)] = "."
        
        commit(prefixes, "prefixes.json")


    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        
        prefixes = load("prefixes.json")
        prefixes.pop(str(guild.id))
        
        commit(prefixes, "prefixes.json")




def setup(bot):
    bot.add_cog(handle_events(bot))