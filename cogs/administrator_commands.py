import discord

from discord.ext import commands
from handlers.handlefiles import load, commit



class administrator_cmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command(aliases=['purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self , ctx , amount = 5):
        await ctx.channel.purge(limit=amount+1)
        
        
        
    @commands.command(aliases=["changeprefix", "changep"])
    @commands.has_permissions(administrator = True)
    async def change_prefix(self, ctx, prefix = "."):
        
        prefixes = load("prefixes.json")
        prefixes[str(ctx.guild.id)] = prefix
        
        commit(prefixes, "prefixes.json")



def setup(bot):
    bot.add_cog(administrator_cmd(bot))