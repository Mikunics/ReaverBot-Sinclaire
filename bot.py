import nextcord
import logging

from typing import Dict, Tuple, Type, Any

from nextcord.ext import commands
from nextcord.abc import GuildChannel, Role

from config import STATS_CHANNELS, PRIMARY_SERVER, SERVER_ROLES

class ReaverBot(commands.Bot):

    ReaverGuild = None
    ReaverChannels = {} #type: Dict[str, Tuple[str, GuildChannel]]
    ReaverRoles = {} #type: Dict[str, Role]

    async def on_ready(self):
        self.ReaverGuild = nextcord.utils.get(self.guilds, id = PRIMARY_SERVER)

        assert self.ReaverGuild is not None, "Reaver server cannot be found"

        for name, prefix, id in STATS_CHANNELS:
            targetChannel = nextcord.utils.get(self.ReaverGuild.channels, id = id)
            if targetChannel is None:
                logging.error("Could not find channel: {}".format(name))
                continue
            self.ReaverChannels[name] = (prefix, targetChannel)

        for name, id in SERVER_ROLES:
            targetRole = nextcord.utils.get(self.ReaverGuild.roles, id = id)
            if targetRole is None:
                logging.error("Could not find role: {}".format(name))
                continue
            self.ReaverRoles[name] = targetRole

        logging.info("Bot is ready to reave!")


    

    

