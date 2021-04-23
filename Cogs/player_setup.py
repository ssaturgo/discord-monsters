import discord
from discord.ext import commands
import os
import json
import shutil

def profile_maker(name):
    with open(f"Database/Players/{name}.json", "r") as file :
        profile_json = json.load(file)
    with open(f"Database/Players/{name}.json", "w") as file :
        profile_json["Profile"]["Name"] = name
        json.dump(profile_json, file,indent=2)

def view_profile(path, name, pfp):
    add_shop_items(name)

    with open("Database/monsters.json") as file:
        monsters_json = json.load(file)
    with open(f"Database/emoji.json", "r") as file :
        emojis = json.load(file) 
    player_description = ""
    with open(f"{path}", "r") as file :
        profile_json = json.load(file)
    player_description += (
        f"{emojis['Profile']['Name']} | {profile_json['Profile']['Name']}\n" +
        f"{emojis['Profile']['Money']} | {profile_json['Profile']['Wealth']}\n"
        f"{emojis['Profile']['Collections']} | {profile_json['Profile']['Tamed']} / {len(monsters_json)}\n"
    )
    embed_msg = discord.Embed(
        title=name,
        color=discord.Color.blue()
    )
    if profile_json["Profile"]["Main"] != "":
        main = profile_json["Profile"]["Main"]
        gif = monsters_json[main]["Profile"]["image"]
        main_monster = ""
        if profile_json["Profile"]["Pet Name"] == "":
            pet_name = profile_json["Profile"]["Pet Name"] = "Unnamed"
        else :
            pet_name = profile_json["Profile"]["Pet Name"]

        main_monster = f"{pet_name} \n{gif}\n"
        embed_msg.add_field(name="Battle Monster", value=main_monster)
    else :
        embed_msg.add_field(name="Battle Monster", value="use **!starter** to get a monster")

    embed_msg.description = player_description
    embed_msg.set_thumbnail(url=pfp)
    return embed_msg

def add_shop_items(username):
    with open(f"Database/Players/{username}.json", "r") as file :
        profile_json = json.load(file)
    with open("Database/shop_inventory.json", "r") as file :
        shop_json = json.load(file)
    for item in shop_json :
        profile_json["Inventory"][f"{item}"] = 0
    with open(f"Database/Players/{username}.json", "w") as file :
        json.dump(profile_json, file, indent=2)

class Player_Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Player setup module is ready..")

    @commands.command()
    async def profile(self, ctx):
        username = str(ctx.author)
        pfp = ctx.author.avatar_url
        file_path = f"Database/Players/{username}.json"
        profile_exist = os.path.exists(f"{file_path}")
        if profile_exist == False :
            shutil.copyfile("Database/profile_template.json", f"{file_path}")
            profile_maker(username)
            print(f"Created new directory for {username}")
            profile = view_profile(file_path, username, pfp)
            await ctx.send(embed=profile)
        else :
            print(f"{username} is an existing player.. loading profile")
            profile = view_profile(file_path, username, pfp)
            await ctx.send(embed=profile)

    @commands.command()
    async def rename(self, ctx, arg):
        username = str(ctx.author)
        with open(f"Database/Players/{username}.json", "r") as file :
            profile = json.load(file)
            profile["Profile"]["Pet Name"] = arg
            pet_id = profile["Profile"]["Main"]
        with open(f"Database/Players/{username}.json", "w") as file :
            json.dump(profile, file)
        await ctx.send(f"Renamed {pet_id} to {arg}")
        print(f"{username} renamed {pet_id} to {arg}...")

def setup(client):
    client.add_cog(Player_Setup(client))