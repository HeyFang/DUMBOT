import discord
from discord.ext import commands




class handle_cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=['addcog'])
    async def loadcog(self, ctx, cog: str = None):
    
        if cog == None:
            em = discord.Embed(
            description = "Must Specify Cog to load",
            color = discord.Color.red())
        
        await ctx.send(embed = em)
        return
        
        try:
            
            bot.load_extension(f"./{cog}")
            
            em = discord.Embed(
            description = f" *:white_check_mark: **{cog}** is now loaded!*",
            color = discord.Color.green())
            
            await ctx.send(embed = em)
        except Exception as e: print(e)






def setup(bot):
    bot.add_cog(handle_cogs(bot))