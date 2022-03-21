import discord
import re
import os
from discord.ext import commands
from discord.ext.commands import Bot
from os.path import exists

client = commands.Bot(command_prefix="!")

@client.event
async def on_message(message):
    if re.search('[aA]', message.content):
        total = message.content.count('a') + message.content.count('A')
        await message.channel.send('You used ' + str(total) + ' of the letter a in your message!')

token = open("discord_token", "r")
discord_token = token.read()
token.close()
bot.run(discord_token)
