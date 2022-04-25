import nextcord

from typing import Optional

from nextcord import TextChannel
from nextcord.ext import commands

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
    async def pin(self, ctx:commands.Context, channel: Channel, messageID: int, footer: Optional[str] = None):
        ''' (needs Mod role)\nPins a selected message given by ID to a selected channel, you may add an optional footer (must be enclosed with quotation marks) as an extra argument.\nCommand must be invoked in the same channel as the original message.'''
        if ctx.guild is None:
            return
        
        if not isinstance(channel, TextChannel):
            await ctx.send("Invalid pin channel")
            return

        msg = await ctx.fetch_message(messageID)

        formatString = "***Pinned By** {pinner}*,    ***Shared By** {author}*".format(pinner = ctx.author.mention, author = msg.author.mention)

        content = msg.content

        if content:
            formatString += "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n{content}\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬".format(content = content)

        if footer is not None and footer.strip() != "":
            formatString += "\n`{}`".format(footer)

        if len(msg.attachments) == 1:
            await channel.send(formatString, file = await msg.attachments[0].to_file())
        elif len(msg.attachments) > 1:
            attachlist = [await attachment.to_file() for attachment in msg.attachments]
            await channel.send(formatString, files = attachlist)
        else:
            await channel.send(formatString)

        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Pins(bot))
