import os, logging
from config import COMMAND_PREFIX, ACTIVE_COGS
from nextcord.ext import commands
from nextcord import Intents

from dotenv import load_dotenv

def main():
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting the bot...")

    logging.info("Loading environment")
    load_dotenv()
    intents = Intents().all()

    logging.info("Instantiating Bot")
    bot = commands.Bot(command_prefix= COMMAND_PREFIX, intents = intents)


    logging.info("Loading cogs...")
    for cog in ACTIVE_COGS:
        logging.info(" -- Loading '{}'".format(cog))
        bot.load_extension(cog)

    logging.info("Running Bot")
    TOKEN = os.getenv('BOT_TOKEN')
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
