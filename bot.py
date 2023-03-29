import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('MTA5MDY1OTg4NzU2ODE0MjQyNg.GJzEFA.DpA2C-z_fy7yq_hXOKRUFQZ4aDBih6gaOGQX5I')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

     members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client = CustomClient()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    
client.run(TOKEN)
