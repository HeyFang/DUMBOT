import discord

from discord.ext import commands, tasks
from discord.utils import get



class roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, role: discord.Role, user: discord.Member):
    	em = discord.Embed(title = None, description = f" *:white_check_mark: Added {role.mention} for user **{user.mention}***", color = discord.Color.green())
    	await user.add_roles(role)
    	await ctx.send(embed=em)


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, role: discord.Role, user: discord.Member):
    	em = discord.Embed(title = None, description = f" *:white_check_mark: Removed {role.mention} for user **{user.mention}***", color = discord.Color.green())
    	await user.remove_roles(role)
    	await ctx.send(embed=em)



def setup(bot):
    bot.add_cog(roles(bot))