import logging
from nextcord.ext import commands
from cogs.stats import Filters
from config import STATS_CHANNELS
from bot import ReaverBot

class Events(commands.Cog):
    def __init__(self, bot:ReaverBot):
        self.bot = bot

    async def updateMembers(self):
        """Update stats channel of total members"""
        guildtarget = self.bot.ReaverGuild
        assert guildtarget is not None
        numOnline = len(list(filter(Filters.filterNonBots,guildtarget.members)))
        target = self.bot.ReaverChannels["Members"]
        await target[1].edit(name = target[0].format(numOnline)) #type:ignore

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.updateMembers()

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.updateMembers()

def setup(bot):
    bot.add_cog(Events(bot))