import logging
import nextcord
from cogs.stats import Stats
from nextcord.ext import commands, tasks
from config import IMPORTANT_CHANNELS

class Tasks(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.chron.start()
    

    async def PlayingReaverTask(self):
        """Update stats channel of people playing Reaver chronically"""
        channel = IMPORTANT_CHANNELS[0]
        guildtarget = self.bot.get_guild(channel[3])
        if(guildtarget is None):
            return
        membersInServer = guildtarget.members
        MembersPlayingReaver = list(filter(Stats.filterPlayingReaver,membersInServer))
        numPlayingReaver = len(MembersPlayingReaver)
        target = guildtarget.get_channel(channel[2])
        if(target is None):
            logging.error("Playing Reaver Channel not found")
            return
        await target.edit(name = channel[1].format(numPlayingReaver)) #type:ignore

    async def UpdateOnline(self):
        """Update stats channel of people online"""
        channel = IMPORTANT_CHANNELS[1]
        guildtarget = self.bot.get_guild(channel[3])
        if(guildtarget is None):
            return
        membersInServer = guildtarget.members
        MembersOnline = list(filter(Stats.filterOnlineMembers,membersInServer))
        numOnline = len(MembersOnline)
        target = guildtarget.get_channel(channel[2])
        if(target is None):
            logging.error("Online channel not found")
            return
        await target.edit(name = channel[1].format(numOnline)) #type:ignore

    @tasks.loop(minutes=5)
    async def chron(self):
        # Run repeating tasks every x minutes
        logging.info("Running chron")
        await self.PlayingReaverTask()
        await self.UpdateOnline()

def setup(bot):
    bot.add_cog(Tasks(bot))
