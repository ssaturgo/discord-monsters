import discord
from discord.ext import commands
import os
import json

with open('Database/shop_inventory.json') as file :
    shop_inventory = json.load(file)
with open('config.json', 'r') as file :
    config = json.load(file)
    channel_id = config["channel_id"]

class Shop_Keeper(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Shop keeper is ready..")

    @commands.command()
    async def shop(self, ctx):
        item_list = ""
        with open("Art/Merchant.png", "rb") as file:
            image = discord.File(file)

        for item in shop_inventory :
            # item_entry = "emoji"+"x"+str(shop_inventory[item]["quantity"])+" | "+shop_inventory[item]["name"]+" | "+str(shop_inventory[item]["cost"])+"\n"
            item_entry = "{emoji} | {name} | {cost} <:dm_currency:832443505157603398>\n".format(
                emoji=shop_inventory[item]["emoji"],
                name = shop_inventory[item]["name"],
                cost = str(shop_inventory[item]["cost"])
            )
            item_list += item_entry

        embed = discord.Embed(
            title="Hugs & Wares",
            description=item_list,
            color=0xfef3c0
        )
        embed.set_footer(text="Thank you for your time!")
        embed.set_author(name="Merchant : Fluffy Muffin")
        await ctx.send(embed=embed, file=image)

def setup(client):
    client.add_cog(Shop_Keeper(client))