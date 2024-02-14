import discord
import re
import os
from discord.ext import commands
from discord.ext.commands import Bot
from os.path import exists
from pwn import *

#discord init
intents = discord.Intents.default()
intents.message_content=True

client = discord.Client(intents=intents)

#pwntools init
host = 'localhost'
port = 4000
conn = remote(host,port)

init = conn.recvuntil(b"USER: ")
print(init.decode())

#prompt configuration
prompt_base = "count how many a's are in the following prompt, then respond to the following prompt to the best of your ability: "

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #construct prompt
    prompt = prompt_base + message.content
    print(prompt)

    conn.sendline(prompt.encode('utf8'))
    
    #process response
    response = conn.recvuntil(b"tokens").decode()
    print(response + "1")
    response = response[response.find("\n")+1:]
    print(response + "2")
    response = response[:response.rfind("\n")]
    print(response + "3")

    #clear junk
    junk = conn.recvuntil(b"USER: ")
    print(junk.decode())

    await message.channel.send(response)

token = open("discord_token", "r")
discord_token = token.read()
token.close()
client.run(discord_token)
