
from discord import CustomActivity
import nextcord
import logging
import asyncio

from typing import Dict, Tuple, Type, Any

from nextcord import Guild, Game
from nextcord.ext import commands
from nextcord.abc import GuildChannel
from nextcord.role import Role

from config import COMMAND_PREFIX, STATS_CHANNELS, PRIMARY_SERVER, SERVER_ROLES

class ReaverBot(commands.Bot):

    ReaverGuild = None
    ReaverChannels = {} #type: Dict[str, Tuple[str, GuildChannel]]
    ReaverRoles = {} #type: Dict[str, Role]

    async def fetchReaverGuild(self):
        guild = nextcord.utils.get(self.guilds, id = PRIMARY_SERVER)
        if guild is None: 
            raise Exception("Reaver server cannot be found!")
        return guild

    async def fetchReaverChannels(self, guild: Guild):
        channelDict = {}
        assert guild is not None
        for name, prefix, id in STATS_CHANNELS:
            targetChannel = nextcord.utils.get(guild.channels, id = id)
            if targetChannel is None:
                logging.error("Could not find channel: {}".format(name))
                continue
            channelDict[name] = (prefix, targetChannel)
        return channelDict

    async def fetchReaverRoles(self, guild: Guild):
        roleDict = {}
        assert guild is not None
        for name, id in SERVER_ROLES:
            targetRole = nextcord.utils.get(guild.roles, id = id)
            if targetRole is None:
                logging.error("Could not find role: {}".format(name))
                continue
            roleDict[name] = targetRole
        return roleDict

    async def on_ready(self):
        self.ReaverGuild = await self.fetchReaverGuild()
        fetched = await asyncio.gather(self.fetchReaverChannels(self.ReaverGuild), self.fetchReaverRoles(self.ReaverGuild))
        self.ReaverChannels, self.ReaverRoles = fetched
        await self.change_presence(activity=Game(name = "{}help".format(COMMAND_PREFIX)))
        logging.info("Bot is ready to reave!")

    async def on_command_error(self, ctx:commands.Context, err):
        logging.error("Command error: {0} [author: {1.author}][cmd: {1.command}]".format(err, ctx))
        await ctx.send("**{0.mention}, I don't recognize what you're trying to say**".format(ctx.author))


    

    

