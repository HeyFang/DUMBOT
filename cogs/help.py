import discord
from discord.ext import commands, tasks
from discord.utils import get

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    #cmd help
    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        em = discord.Embed(title = "Help",
        description = "use #help <command> for extended information on a command.",
        color = 0x11aaf5)

        em.add_field(name = "Moderation", value = "`kick`,`ban`,`warn`,`purge`,`mute`")
        em.add_field(name = "General", value = "`meme`,`whois/info`,`serverinfo`,`rule`")

        await ctx.send(embed = em)




    #cmd help kick
    @help.command()
    async def kick(self, ctx):

        em = discord.Embed(title = "kick", 
            description = "Kicks a member from the guild",
            color = 0x11aaf5)

        em.add_field(name = "**Syntax**", value = "`>kick <member> <reason>`")

        await ctx.send(embed = em)

    #cmd help ban
    @help.command()
    async def ban(self, ctx):

        em = discord.Embed(title = "kick", 
            description = "Bans a member from the guild",
            color = 0x11aaf5)

        em.add_field(name = "**Syntax**", value = "`>ban <member> <reason>`")

        await ctx.send(embed = em)











def setup(bot):
    bot.add_cog(help(bot))