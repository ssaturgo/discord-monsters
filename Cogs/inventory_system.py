import discord
from discord.ext import commands
import json

class Inventory_System(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bag(self, ctx):
        username = str(ctx.author)
        pfp = ctx.author.avatar_url
        embed_msg = discord.Embed(
            title=f"{username}'s Inventory",
            color=0xfef3c0
        )
        with open(f"Database/Players/{username}.json", "r") as file :
            profile_json = json.load(file)
        with open("Database/shop_inventory.json", "r") as file :
            shop_items = json.load(file)
        player_inventory = ""
        for item in profile_json["Inventory"] :
            quantity = profile_json["Inventory"][item]
            item_icon = shop_items[item]["emoji"]
            item_name = shop_items[item]["name"]
            if quantity > 0:
                player_inventory += f"{quantity} {item_icon} {item_name}\n"
        if player_inventory == "" :
            player_inventory = "You currently have no items"
        embed_msg.description = player_inventory
        embed_msg.set_thumbnail(url=pfp)
        await ctx.send(embed=embed_msg)
def setup(client):
    client.add_cog(Inventory_System(client))