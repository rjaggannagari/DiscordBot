# imports for this project
# for this import you have to do python3 -m pip install discord.py on the command line
import discord
import random
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '-')

# Sees if the bot is ready to use
@client.event
async def on_ready():
    print('Basic discord bot is ready to use')

# This command gives the clients current ping, to use this command just call -msping
@client.command()
async def msping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

# This command gives the user heads or tails, to use this command just call -flipcoin
@client.command()
async def flipcoin(ctx):
    choices = ['Heads', 'Tails']
    await ctx.send(f'It is {random.choice(choices)}')

# Each bot has their unique token so I have placed mine in an .env file
client.run(os.getenv('TOKEN'))