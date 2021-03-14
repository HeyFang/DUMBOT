import discord
from discord.ext import commands, tasks




class handle_help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 
    
    @commands.command(aliases=['help'])
    async def help_client(self , ctx):
        """helps client to see commands help"""
        embed=discord.Embed(title="**Palice Plugins Help.**", 
            url="http://cyclones.ml/", 
            description="Heya Dumbos, am Palice: A modified version", 
            color=0x11aaf5)
        
        embed.set_author(name="Cyclones Official", url="https://discord.gg/FCcKuWB8x6", 
            icon_url="https://cdn.discordapp.com/avatars/817402985859514399/1233c748fb8bf08ea67cb42632f02093.webp")
        
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/810697727469682711/820320167342637096/1f300.png")
        
        embed.add_field(name="Info Commands", value="`botinfo` `serverinfo` `whois` `avatar`", inline=False)
        embed.add_field(name="Mod Commands", value="`addrole` `removerole` `purge` `mute` `unmute`", inline=False)
        embed.add_field(name="Admin Commands", value="`ban` `unban`", inline=False)
        embed.add_field(name= "More", value="***use help <command>*** for more info about command.", inline=False)
        embed.add_field(name="Help Server", value="https://discord.gg/FCcKuWB8x6", inline=False)
        embed.add_field(name="Features", value="*Added `activity` command for Bot-Owners*, *Advance Chat filter which auto deletes the blaclisted words*, *More coming soon ;)*", inline=False)
        embed.add_field(name="Coming soon...", value="*Meme command*, *repeatmessage command which would repeat triggered msg after given time interval*, *Welcome messages*...", inline=False)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(handle_help(bot))