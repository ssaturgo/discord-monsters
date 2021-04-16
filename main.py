# Libraries
import discord
from discord.ext import commands
import json
import os

with open("config.json") as file :
    config = json.load(file)
TOKEN = config["DISCORD_TOKEN"]

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():   # When the bot is in ready state
    print("bot is ready")

@client.command()
async def ping(ctx) :
    await ctx.send(f'bot latency {round(client.latency * 1000)}ms')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def load(ctx, extention):
    client.load_extension(f'Cogs.{extention}')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'Cogs.{extention}')

for filename in os.listdir("Cogs"):
    if filename.endswith('.py'):
        client.load_extension(f'Cogs.{filename[:-3]}')

if __name__ == '__main__' :
    client.run(TOKEN) # Discord API Token