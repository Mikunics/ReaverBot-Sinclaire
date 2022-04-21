import logging

from nextcord import ActivityType, Status, Embed
from nextcord.ext import commands
from nextcord.member import Member

from config import SERVER_LINKS, COMMAND_PREFIX

from bot import ReaverBot


class Info(commands.Cog):
    def  __init__(self, bot:ReaverBot):
        self.bot = bot

    @commands.command()
    async def links(self, ctx:commands.Context):
        """Gives you ALL the REAVER related links"""
        content = ""
        for name, link in SERVER_LINKS:
            content += "[{name}]({link})\n".format(name = name, link = link)
        content.strip()
        finalEmbed = Embed(title = "Reaver Links", description=content)
        await ctx.send(embed = finalEmbed)

    @commands.command()
    async def help(self, ctx:commands.Context, command=None):
        """Shows all the features the bot is able to do."""
        #Taken from https://github.com/lickorice/shalltear
        all_commands = [cmd for cmd in self.bot.commands]
        if command == None:
            embed = Embed(title="Commands for REAVER Bot", color=0xcc0000)
            for cog in self.bot.cogs:

                commands_for_cog = [f'`{c.name}`' for c in all_commands if not c.hidden and c.cog_name == cog]
                s = ' '.join(commands_for_cog)
                if s:
                    embed.add_field(name=cog, inline=False, value=s)
            await ctx.send("Do `{}help <command>` for more information.".format(COMMAND_PREFIX))
        else:
            if command not in [c.name for c in all_commands]:
                await ctx.send("I don't quite know what that command is")
                return
            cmd = [c for c in all_commands if c.name == command][0]
            if cmd.aliases:
                name = f'{cmd.name} [{"/".join(cmd.aliases)}]'
            else:
                name = cmd.name
            if cmd.clean_params:
                name += f' <{", ".join(cmd.clean_params)}>'
            name = '`{}`'.format(name)
            embed = Embed(title=cmd.cog_name, color=0xff1155)
            embed.add_field(name=name, value=cmd.help)
        await ctx.send(embed=embed)
        

def setup(bot):
    bot.add_cog(Info(bot))
