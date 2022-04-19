import logging
from nextcord.ext import commands
from stats import Filters
from config import STATS_CHANNELS

class Events(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    async def updateMembers(self):
        """Update stats channel of total members"""
        channel = STATS_CHANNELS[2]
        guildtarget = self.bot.get_guild(channel[3])
        if(guildtarget is None):
            return
        membersInServer = guildtarget.members
        MembersOnline = list(filter(Filters.filterNonBots,membersInServer))
        numOnline = len(MembersOnline)
        target = guildtarget.get_channel(channel[2])
        if(target is None):
            logging.error("Member stats channel not found")
            return
        await target.edit(name = channel[1].format(numOnline)) #type:ignore

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.updateMembers()

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.updateMembers()
        
def setup(bot):
    bot.add_cog(Events(bot))