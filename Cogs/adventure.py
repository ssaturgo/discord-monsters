import discord
from discord.ext import commands
import json
import random

def get_random_name():
    with open("Database/first-names.txt", "r") as file :
        list_of_names = file.read().splitlines()
    index = int(random.random() * 4945) + 1
    picked_name = list_of_names[index]
    return picked_name

def get_random_item():
    with open("Database/shop_inventory.json", "r") as file :
        items_json = json.load(file)
    items = list(items_json.keys())
    treasure = random.choice(items)
    if treasure == "Fluffy hugs" or treasure == "Memory Gems": # exclude shop exclusive items from treasures
        treasure = get_random_item()
    return treasure

class Adventure_Manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def embark(self, ctx) :
        username = str(ctx.author)
        embed_msg = discord.Embed(color=discord.Color.red())
        d20 = random.randint(0, 20)
        with open(f"Database/Players/{username}.json", "r") as file :
                profile_json = json.load(file)

        # ------------------------------------------------
        # Prevent embarking without monster
        if profile_json["Profile"]["Main"] == "" :
            embed_msg.title = "⚠️ WARNING ⚠️"
            embed_msg.description = "It's too dangerous to embark without a monster. try again next time"
            await ctx.send(embed=embed_msg)
            return
        # ------------------------------------------------
        if d20 >= 15 : # get treasure!
            embed_msg.title = "Found Treasure!"
            treasure = get_random_item()
            quantity = random.randint(1, 5)
            money = random.randint(1, 50)
            if quantity > 1 :
                plural = "s"
            else : plural = ""
            with open("Database/shop_inventory.json", "r") as file :
                items = json.load(file)
                icon = items[treasure]["emoji"]
            embed_msg.description = (
                f"<:dm_treasure:834939719824834570> You found {quantity}x {icon} **{treasure}{plural}** and <:dm_currency:832443505157603398>{money}")
            profile_json["Inventory"][treasure] += quantity
            profile_json["Profile"]["Wealth"] += money
            with open(f"Database/Players/{username}.json", "w") as file :
                json.dump(profile_json, file, indent=2)
            await ctx.send(embed=embed_msg)
        # ------------------------------------------------
        else : # encounter battle!
            player_pet = profile_json["Profile"]["Main"]
            monster_id = profile_json["Profile"]["Main"]
            monster_name = profile_json["Profile"]["Pet Name"]
            with open("Database/enemies.json", "r") as file:
                enemies_json = json.load(file)
                enemies_list = list(enemies_json.keys())
                enemy = random.choice(enemies_list)
                enemy_name = get_random_name()
                enemy_icon = enemies_json[enemy]["icon"]
                enemy_health = enemies_json[enemy]["health"]
                enemy_dmg = enemies_json[enemy]["attack"]
                enemy_accuracy = enemies_json[enemy]["accuracy"]
            with open("Database\monsters.json", "r") as file :
                monsters_json = json.load(file)
                monster_icon = monsters_json[monster_id]["Profile"]["image"]
                monster_health = monsters_json[monster_id]["Stats"]["health"]
                monster_attack = monsters_json[monster_id]["Stats"]["power"]
                monster_speed = monsters_json[monster_id]["Stats"]["speed"]
                monster_magic = monsters_json[monster_id]["Stats"]["magic"]

            embed_msg.title = f"⚠️ Hostile Encounter ⚠️"
            embed_msg.description = f"{monster_icon} ⚔️ {enemy_icon}"

            enemy_hearts = ""
            for i in range(enemy_health) :
                enemy_hearts += "<:dm_heart:834874390872326215>"
            embed_msg.add_field(name=f"🟥 {enemy} {enemy_name}", value=enemy_hearts, inline= False)

            monster_hearts = ""
            for i in range(monster_health) :
                monster_hearts += "<:dm_heart:834874390872326215>"
            embed_msg.add_field(name=f"🟩 {monster_name}", value=monster_hearts, inline= False)
            await ctx.send(embed = embed_msg)

def setup(client):
    client.add_cog(Adventure_Manager(client))