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

        i = 1
        for item in shop_inventory :
            item_list += f"{i}) "
            item_entry = "{emoji} {name} | {cost} <:dm_currency:832443505157603398>\n".format(
                emoji=shop_inventory[item]["emoji"],
                name = shop_inventory[item]["name"],
                cost = str(shop_inventory[item]["cost"])
            )
            item_list += item_entry
            i = i + 1

        embed = discord.Embed(
            title="Shop",
            description=item_list,
            color=0xfef3c0
        )
        username = str(ctx.author)
        with open(f"Database/Players/{username}.json", "r") as file:
            profile_json = json.load(file)
            player_money = profile_json["Profile"]["Wealth"]

        embed.add_field(name=f"{username}'s Gold", value=f"<:dm_currency:832443505157603398> {player_money}")
        embed.set_footer(text="Use !buy\nThank you for your time!")
        embed.set_author(name="Merchant : Fluffy Muffin")
        await ctx.send(embed=embed, file=image)

    @commands.command()
    async def buy(self, ctx, item_id_str, quantity_str):
        item_id = int(item_id_str)
        quantity = int(quantity_str)
        username = str(ctx.author)
        pfp = ctx.author.avatar_url
        with open(f"Database/Players/{username}.json", "r") as file :
            profile_json = json.load(file)
            player_money = profile_json["Profile"]["Wealth"]
        with open(f"Database/shop_inventory.json", "r") as file :
            shop_inventory = json.load(file)
            item_list = list(shop_inventory.keys())
            item_lookup = item_list[item_id - 1]
            item_per_cost = shop_inventory[f"{item_lookup}"]["cost"]
        
        order_cost = item_per_cost * quantity
        embed_msg = discord.Embed(
            title="<:dm_merchant_pfp:834133527108517898> Fluffy Muffin",
            color=0xfef3c0
        )
        if player_money < order_cost :
            embed_msg.description = f"Sorry {username}, You do not have enough gold.. 🙁"
        else :
            profile_json["Profile"]["Wealth"] -= order_cost
            profile_json["Inventory"][item_lookup] = quantity
            with open (f"Database/Players/{username}.json", "w") as file :
                json.dump(profile_json, file, indent=2)
            embed_msg.description = f"Thank you for your purchase! {username}"
        await ctx.send(embed=embed_msg)

def setup(client):
    client.add_cog(Shop_Keeper(client))