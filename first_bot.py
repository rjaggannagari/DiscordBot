# imports for this project
# for this import you have to do python3 -m pip install discord.py on the command line
import discord
import random
import os
from discord.ext import commands
import pandas
import numpy

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
    choices = ['heads', 'tails']
    await ctx.send(f'It is {random.choice(choices)}')

# This command looks through a csv file with over 20000 jokes and randomly chooses one
@client.command()
async def telljoke(ctx):
    jokes_filename = 'shortjokes.csv'
    filtered_jokes = pandas.read_csv(jokes_filename, usecols=['Joke'])
    jokes_array = numpy.array(filtered_jokes)
    await ctx.send(f'Here is the joke: {random.choice(jokes_array)}')

# This command clears just the last message
@client.command()
async def clear1(ctx, amount = 1):
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)

# This command clears the last 10 messages in a channel
@client.command()
async def clear10(ctx, amount = 10):
	await ctx.message.delete()
	await ctx.channel.purge(limit = amount)

# This command clears the last 10000 messages in a channel
@client.command()
async def clearall(ctx, amount = 100):
    for i in range (0, 100):
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)

# Each bot has their unique token so I have placed mine in an .env file
client.run(os.getenv('TOKEN'))