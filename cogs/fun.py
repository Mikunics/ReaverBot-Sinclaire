import logging
import requests
import os
import io
import aiohttp

from nextcord import File
from nextcord.ext import commands
from nextcord.member import Member

from config import SERVER_LINKS, COMMAND_PREFIX

from bot import ReaverBot

from dotenv import load_dotenv

async def fetchCat():
    headers = {'x-api-key': os.getenv('CATAPI_TOKEN')}
    url = 'https://api.thecatapi.com/v1/images/search'
    r = requests.get(url, headers=headers)
    try:
        jsonContent = r.json()[0]
        return str(jsonContent["url"])
    except Exception as e:
        logging.exception(e)
        return None

async def urlToFile(url):
    data = None
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return None
            data = io.BytesIO(await resp.read())
    return data

class Fun(commands.Cog):
    def  __init__(self, bot:ReaverBot):
        self.bot = bot
            
    @commands.command()
    async def cat(self, ctx:commands.Context):
        """Gives you a picture of a cat"""
        imgurl = await fetchCat()
        img = await urlToFile(imgurl)
        if img is not None:
            assert imgurl is not None
            extension = imgurl.rsplit(".")[-1]
            await ctx.channel.send(file = File(img, "cat.{}".format(extension))) #type: ignore
        else:
            await ctx.send("Sorry, I couldn't get a cat for you, try again.")

        
def setup(bot):
    bot.add_cog(Fun(bot))
