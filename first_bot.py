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

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

# This checks to see if a specfic message is sent
@client.event
async def on_message(message):
    discord_username = str(message.author).split("#")[0]
    channel_name = str(message.channel.name)

    if message.author == client.user:
        return

    # If hi or hello are said in the welcome chat return hi along with their username
    # Sends a basic message back to users
    if 'hi' in message.content or 'hello' in message.content:
        await message.channel.send(f'Hi , {discord_username}, hope you are having a great day!')

# This command gives the clients current ping, to use this command just call -msping
@client.command()
async def msping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

# This command gives the user heads or tails, to use this command just call -flipcoin
@client.command()
async def flipcoin(ctx):
    choices = ['Heads', 'Tails']
    await ctx.send(f'It is {random.choice(choices)}')

# This command looks through a csv file with over 20000 jokes and randomly chooses one
@client.command()
async def telljoke(ctx):
    jokes_filename = 'shortjokes.csv'
    filtered_jokes = pandas.read_csv(jokes_filename, usecols=['Joke'])
    jokes_array = numpy.array(filtered_jokes)
    await ctx.send(f'{random.choice(jokes_array)}')

@client.command()
async def message(ctx, user:discord.member, *, message = None):
    message = "welcome"
    embed = discord.Embed(title = message)
    await user.send(embed = embed)

# Each bot has their unique token so I have placed mine in an .env file
client.run(os.getenv('TOKEN'))