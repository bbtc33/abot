import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.search('[aA]', message.content):
        total = message.content.count('a') + message.content.count('A')
        await message.channel.send(total)

client.run('your token here')
