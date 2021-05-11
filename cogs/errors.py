import discord
import asyncio

from discord.ext import commands


class HandleErrors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # TODO: on_command_errors event here


def setup(bot):
    bot.add_cog(HandleErrors(bot))