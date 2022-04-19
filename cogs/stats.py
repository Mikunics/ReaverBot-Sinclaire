import logging

from nextcord import ActivityType, Status
from nextcord.ext import commands
from nextcord.member import Member

from config import STATS_CHANNELS

class Filters():
    @staticmethod
    def filterOnlineMembers(member:Member):
        if member.bot:
            return False
        return member.status != Status.offline

    @staticmethod
    def filterPlayingReaver(member:Member):
        if(member.status == Status.offline):
            return False
        for activity in member.activities:
            if activity == None or activity.name == None:
                continue
            if activity.name.lower().find("reaver") != -1 and activity.type == ActivityType.playing:
                return True
        else:
            return False

    @staticmethod
    def filterNonBots(member:Member):
        return not member.bot

class Stats(commands.Cog):
    def  __init__(self, bot:commands.Bot):
        self.bot = bot

    @commands.has_role("Mod")
    @commands.command()
    async def updatePlayingReaver(self, ctx:commands.Context):
        """Update stats channel of people playing Reaver"""
        if(ctx.guild is None):
            return
        membersInServer = ctx.guild.members
        MembersPlayingReaver = list(filter(Filters.filterPlayingReaver,membersInServer))
        numPlayingReaver = len(MembersPlayingReaver)
        channel = STATS_CHANNELS[0] # refers to playing reaver channel
        target = ctx.guild.get_channel(channel[2])
        if(target is None):
            logging.error("Playing Reaver channel not found")
            return
        await target.edit(name = channel[1].format(numPlayingReaver)) #type:ignore

    @commands.has_role("Mod")
    @commands.command()
    async def updateOnline(self, ctx:commands.Context):
        """Update stats channel of people online"""
        if(ctx.guild is None):
            return
        membersInServer = ctx.guild.members
        MembersOnline = list(filter(Filters.filterOnlineMembers,membersInServer))
        numOnline = len(MembersOnline)
        channel = STATS_CHANNELS[1] # refers to members
        target = ctx.guild.get_channel(channel[2])
        if(target is None):
            logging.error("Members online channel not found")
            return
        await target.edit(name = channel[1].format(numOnline)) #type:ignore

    @commands.has_role("Mod")
    @commands.command()
    async def updateMembers(self, ctx:commands.Context):
        """Update stats channel of members in server"""
        if(ctx.guild is None):
            return
        membersInServer = ctx.guild.members
        realMembers = list(filter(Filters.filterNonBots,membersInServer))
        numRealMembers = len(realMembers)
        channel = STATS_CHANNELS[2] # refers to members channel
        target = ctx.guild.get_channel(channel[2])
        if(target is None):
            logging.error("Members channel not found")
            return
        await target.edit(name = channel[1].format(numRealMembers)) #type:ignore


    @commands.command()
    async def ping(self, ctx:commands.Context):
        """Tests responsiveness."""
        latency_in_ms = "{} ms".format(int(self.bot.latency * 1000))
        await ctx.send("Pong! {}".format(latency_in_ms))

    @commands.command()
    async def online(self, ctx:commands.Context):
        """Check amount of online users in current server"""
        if(ctx.guild is None):
            return
        membersInServer = ctx.guild.members
        onlineMembersInServer = list(filter(Filters.filterOnlineMembers,membersInServer))
        await ctx.send("There is/are currently {} user/s online in the server".format(len(onlineMembersInServer)))

    @commands.command()
    async def playingReaver(self, ctx:commands.Context):
        """Check amount of online users in current server that are playing Reaver"""
        if(ctx.guild is None):
            return
        membersInServer = ctx.guild.members
        MembersPlayingReaver = list(filter(Filters.filterPlayingReaver,membersInServer))
        await ctx.send("There is/are currently {} user/s playing REAVER in the server".format(len(MembersPlayingReaver)))

def setup(bot):
    bot.add_cog(Stats(bot))
