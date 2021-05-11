import discord
import asyncio

from discord.ext import commands
from handlers.handlefiles import load_bad_words



class Filter(commands.Cog):
    def __init__(self, bot):
        
        self.bot = bot
        self.custom_bad_words = load_bad_words()
        self.bad_words = ["bitch", "fuck"]
        
        for word in self.custom_bad_words:
            self.bad_words.append(word)

    @commands.Cog.listener()
    async def on_message(self, msg):
        if any(str(bad_word) in str(msg.content.lower()) for bad_word in self.bad_words):
            await msg.delete()


def setup(bot):
    bot.add_cog(Filter(bot))