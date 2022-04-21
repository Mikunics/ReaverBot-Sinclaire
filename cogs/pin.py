import nextcord

from nextcord import TextChannel
from nextcord.ext import commands

from config import STATS_CHANNELS

from bot import ReaverBot

class Channel(commands.Converter):
    async def convert(self, ctx: commands.Context, arg):
        arg = str(arg)
        assert ctx.guild is not None
        if arg.find("#") != -1:
            arg = arg.strip("<>#")
            return nextcord.utils.get(ctx.guild.channels, id = int(arg))
        else:
            return nextcord.utils.get(ctx.guild.channels, name = arg)

class Pins(commands.Cog):
    def  __init__(self, bot:ReaverBot):
        self.bot = bot

    @commands.has_role("Mod")
    @commands.command()
    async def pin(self, ctx:commands.Context, channel: Channel, messageID: int, footer = None):
        '''Pins a selected message given by ID to a selected channel, you may add an optional footer (must be enclosed with quotation marks if it contains a space) as an extra argument (Command must be invoked in the same channel as the original message)'''
        if ctx.guild is None:
            return
        msg = await ctx.fetch_message(messageID)
        if not isinstance(channel, TextChannel):
            return

        formatString = "***Shared By** {author}*\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{content}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬"

        msgContent = formatString.format(author = msg.author.mention, content = msg.content)

        if footer is not None:
            msgContent += "\n`{}`".format(footer)

        if len(msg.attachments) == 1:
            await channel.send(msgContent, file = await msg.attachments[0].to_file())
        elif len(msg.attachments) > 1:
            attachlist = [await attachment.to_file() for attachment in msg.attachments]
            await channel.send(msgContent, files = attachlist)
        else:
            await channel.send(msgContent)

        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Pins(bot))
