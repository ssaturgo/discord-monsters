import discord
from discord.ext import commands

class Admin_Commands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Admin commands are loaded...")

def setup(client):
    client.add_cog(Admin_Commands(client))