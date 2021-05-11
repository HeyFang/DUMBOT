import discord
import asyncio

from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        #TODO: make botinfo, serverinfo


def setup(bot):
    bot.add_cog(Info(bot))