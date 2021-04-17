import discord
from discord.ext import commands
from os import remove
import os.path


class Admin_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands are loaded...") 
        print()

    @commands.command()
    async def ping(self,ctx) :
        await ctx.send(f'bot latency {round(self.client.latency * 1000)}ms')

    @commands.command()
    async def delprofile(self, ctx) :
        username = str(ctx.author)
        path = f"Database/Players/{username}.json"
        if os.path.exists(path):
            remove(path)
            print(f"Deleted {username}'s profile")
        else:
            ctx.send("You do not have a profile to delete")

def setup(client):
    client.add_cog(Admin_Commands(client))