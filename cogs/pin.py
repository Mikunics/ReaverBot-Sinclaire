import discord
from discord import TextChannel

import nextcord
from nextcord.ext import commands

from config import IMPORTANT_CHANNELS

class Channel(commands.Converter):
    async def convert(self, ctx, arg):
        arg = str(arg)
        if arg.find("#") != -1:
            arg = arg.strip("<>#")
            return discord.utils.get(ctx.guild.channels, id = int(arg))
        else:
            return discord.utils.get(ctx.guild.channels, name = arg)

class Pins(commands.Cog):
    def  __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.has_role("Mod")
    @commands.command()
    async def pin(self, ctx:commands.Context, channel: Channel, messageID: int, footer = None):
        if ctx.guild is None:
            return
        msg = await ctx.fetch_message(messageID)
        if not isinstance(channel, TextChannel):
            return

        if footer is None:
            if len(msg.attachments) == 1:
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" , file = await msg.attachments[0].to_file()) #type:ignore
            elif len(msg.attachments) > 1:
                attachlist = [await attachment.to_file() for attachment in msg.attachments]
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" , files = attachlist) #type:ignore
            else:
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" )
            
        else:
            if len(msg.attachments) == 1:
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" + "\n`{}`".format(footer), file = await msg.attachments[0].to_file()) #type:ignore
            elif len(msg.attachments) > 1:
                attachlist = [await attachment.to_file() for attachment in msg.attachments]
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" + "\n`{}`".format(footer), files = attachlist) #type:ignore
            else:
                await channel.send("***Shared By** {}*\n".format(msg.author.mention) + "▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{}".format(msg.content) + "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬" + "\n`{}`".format(footer))

def setup(bot):
    bot.add_cog(Pins(bot))
