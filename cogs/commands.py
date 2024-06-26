import discord
import asyncio

from discord.ext import commands


class Comnds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    
    @commands.command(name='avatar', aliases=['Avatar', 'av'])
    async def av_cmd(self, ctx, user: discord.Member = None):
        
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
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! `{latency}`")


def setup(bot):
    bot.add_cog(Comnds(bot))