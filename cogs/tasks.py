import logging

import nextcord

from nextcord.ext import commands, tasks

from config import STATS_CHANNELS, SERVER_ROLES
from cogs.stats import Filters
from bot import ReaverBot

class Tasks(commands.Cog):
    def __init__(self, bot:ReaverBot):
        self.bot = bot
        self.chron.start()

    async def PlayingReaverTask(self):
        """Update stats channel of people playing Reaver chronically"""
        assert self.bot.ReaverGuild is not None
        numPlayingReaver = len(list(filter(Filters.filterPlayingReaver,self.bot.ReaverGuild.members)))
        target = self.bot.ReaverChannels["Playing Reaver"]
        assert target is not None
        await target[1].edit(name = target[0].format(numPlayingReaver)) #type:ignore

    async def UpdateOnline(self):
        """Update stats channel of people online"""
        assert self.bot.ReaverGuild is not None
        numOnline = len(list(filter(Filters.filterOnlineMembers,self.bot.ReaverGuild.members)))
        target = self.bot.ReaverChannels["Online"]
        assert target is not None
        await target[1].edit(name = target[0].format(numOnline)) #type:ignore

    @tasks.loop(minutes=5)
    async def chron(self):
        # Run repeating tasks every x minutes
        if self.chron.current_loop == 0:
            return
        logging.info("Running chron")
        await self.PlayingReaverTask()
        await self.UpdateOnline()

    @commands.Cog.listener()
    async def on_presence_update(self, before:nextcord.Member, after:nextcord.Member):
        # Gives and Takes playing Reaver Role
        if(Filters.filterPlayingReaver(before) == False and Filters.filterPlayingReaver(after) == True):
            playingReaverRole = self.bot.ReaverRoles["Playing Reaver"]
            assert playingReaverRole is not None
            await after.add_roles(playingReaverRole, reason = "He is currently playing Reaver!")
            return

        elif(Filters.filterPlayingReaver(before) == True and Filters.filterPlayingReaver(after) == False):
            playingReaverRole = self.bot.ReaverRoles["Playing Reaver"]
            assert playingReaverRole is not None
            await after.remove_roles(playingReaverRole, reason = "He is no longer playing Reaver")
            return
        else:
            return

def setup(bot):
    bot.add_cog(Tasks(bot))
