import discord
from discord.ext import commands
import os
import json

with open('Database/shop_inventory.json') as file :
    shop_inventory = json.load(file)

class Shop_Keeper(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Shop keeper is ready..")

def setup(client):
    client.add_cog(Shop_Keeper(client))