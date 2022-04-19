import logging

import nextcord

from cogs.stats import Filters
from nextcord.ext import commands, tasks
from config import STATS_CHANNELS, SERVER_ROLES

class Tasks(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        self.chron.start()
    

    async def PlayingReaverTask(self):
        """Update stats channel of people playing Reaver chronically"""
        channel = STATS_CHANNELS[0]
        guildtarget = self.bot.get_guild(channel[3])
        if(guildtarget is None):
            return
        membersInServer = guildtarget.members
        MembersPlayingReaver = list(filter(Filters.filterPlayingReaver,membersInServer))
        numPlayingReaver = len(MembersPlayingReaver)
        target = guildtarget.get_channel(channel[2])
        if(target is None):
            logging.error("Playing Reaver Channel not found")
            return
        await target.edit(name = channel[1].format(numPlayingReaver)) #type:ignore

    async def UpdateOnline(self):
        """Update stats channel of people online"""
        channel = STATS_CHANNELS[1]
        guildtarget = self.bot.get_guild(channel[3])
        if(guildtarget is None):
            return
        membersInServer = guildtarget.members
        MembersOnline = list(filter(Filters.filterOnlineMembers,membersInServer))
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

    @commands.Cog.listener()
    async def on_presence_update(self, before:nextcord.Member, after:nextcord.Member):
        # Gives and Takes playing Reaver Role
        if(Filters.filterPlayingReaver(before) == False and Filters.filterPlayingReaver(after) == True):
            target = SERVER_ROLES[0]
            targetGuild = self.bot.get_guild(target[2])

            if targetGuild is None:
                return

            playingReaverRole = nextcord.utils.get(targetGuild.roles, id = target[1])

            if playingReaverRole is None:
                return

            await after.add_roles(playingReaverRole, reason = "He is currently playing Reaver!")
            return

        elif(Filters.filterPlayingReaver(before) == True and Filters.filterPlayingReaver(after) == False):
            target = SERVER_ROLES[0]
            targetGuild = self.bot.get_guild(target[2])

            if targetGuild is None:
                return

            playingReaverRole = nextcord.utils.get(targetGuild.roles, id = target[1])

            if playingReaverRole is None:
                return

            await after.remove_roles(playingReaverRole, reason = "He is no longer playing Reaver")
            return

        else:
            return


def setup(bot):
    bot.add_cog(Tasks(bot))
