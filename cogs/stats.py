import logging

from nextcord import ActivityType, Status
from nextcord.ext import commands
from nextcord.member import Member

from config import STATS_CHANNELS

from bot import ReaverBot

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
    def  __init__(self, bot:ReaverBot):
        self.bot = bot

    @commands.has_role("Mod")
    @commands.command()
    async def updatePlayingReaver(self, ctx:commands.Context):
        """Update stats channel of people playing Reaver"""
        assert self.bot.ReaverGuild is not None
        numPlayingReaver = len(list(filter(Filters.filterPlayingReaver,self.bot.ReaverGuild.members)))
        target = self.bot.ReaverChannels["Playing Reaver"]
        assert target is not None
        await target[1].edit(name = target[0].format(numPlayingReaver)) #type:ignore
        await ctx.send("Reaving channel has been updated")

    @commands.has_role("Mod")
    @commands.command()
    async def updateOnline(self, ctx:commands.Context):
        """Update stats channel of people online"""
        assert self.bot.ReaverGuild is not None
        numOnline = len(list(filter(Filters.filterOnlineMembers,self.bot.ReaverGuild.members)))
        target = self.bot.ReaverChannels["Online"]
        assert target is not None
        await target[1].edit(name = target[0].format(numOnline)) #type:ignore
        await ctx.send("Resting channel has been updated")

    @commands.has_role("Mod")
    @commands.command()
    async def updateMembers(self, ctx:commands.Context):
        """Update stats channel of members in server"""
        assert self.bot.ReaverGuild is not None
        numMembers = len(list(filter(Filters.filterNonBots,self.bot.ReaverGuild.members)))
        target = self.bot.ReaverChannels["Members"]
        assert target is not None
        await target[1].edit(name = target[0].format(numMembers)) #type:ignore
        await ctx.send("Reavers channel has been updated")


    @commands.command()
    async def ping(self, ctx:commands.Context):
        """Tests responsiveness."""
        latency_in_ms = "{} ms".format(int(self.bot.latency * 1000))
        await ctx.send("Pong! {}".format(latency_in_ms))

    @commands.command()
    async def members(self, ctx:commands.Context):
        """Check amount of users in current server"""
        assert self.bot.ReaverGuild is not None
        membersInServer = self.bot.ReaverGuild.members
        MembersInServer = list(filter(Filters.filterNonBots,membersInServer))
        await ctx.send("There is/are currently {} user/s in the server".format(len(MembersInServer)))

    @commands.command()
    async def online(self, ctx:commands.Context):
        """Check amount of online users in current server"""
        assert self.bot.ReaverGuild is not None
        membersInServer = self.bot.ReaverGuild.members
        onlineMembersInServer = list(filter(Filters.filterOnlineMembers,membersInServer))
        await ctx.send("There is/are currently {} user/s online in the server".format(len(onlineMembersInServer)))

    @commands.command()
    async def playingReaver(self, ctx:commands.Context):
        """Check amount of online users in current server that are playing Reaver"""
        assert self.bot.ReaverGuild is not None
        membersInServer = self.bot.ReaverGuild.members
        MembersPlayingReaver = list(filter(Filters.filterPlayingReaver,membersInServer))
        await ctx.send("There is/are currently {} user/s playing REAVER in the server".format(len(MembersPlayingReaver)))

def setup(bot):
    bot.add_cog(Stats(bot))
