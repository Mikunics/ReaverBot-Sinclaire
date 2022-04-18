import logging
from msilib.schema import File
import discord
from discord import ActivityType, Status, TextChannel

import nextcord
from nextcord.ext import commands
from nextcord.member import Member

from config import IMPORTANT_CHANNELS

class Pin(commands.Cog):
    def  __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.has_role("Mod")
    @commands.command()
    async def pin(self, channelname: str, messageID: int, ctx:commands.Context):
        if ctx.guild is None:
            return
        msg = await ctx.fetch_message(messageID)
        channel = discord.utils.get(ctx.guild.channels, name = channelname)
        if not isinstance(channel, TextChannel):
            return
        if len(msg.attachments) == 1:
            await channel.send("Original Poster: {}\n".format(msg.author) + msg.content, file = msg.attachments[0].to_file()) #type:ignore
        elif len(msg.attachments) > 1:
            attachlist = [attachment.to_file() for attachment in msg.attachments]
            await channel.send("Original Poster: {}\n".format(msg.author) + msg.content, files = attachlist) #type:ignore
        else:
            await channel.send("Original Poster: {}\n".format(msg.author) + msg.content)


def setup(bot):
    bot.add_cog(Pin(bot))
