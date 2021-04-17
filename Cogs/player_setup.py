import discord
from discord.ext import commands
import os
import json
import shutil


def profile_maker(name):
    with open(f"Database/Players/{name}.json", "r") as file :
        profile_json = json.load(file)
    with open(f"Database/Players/{name}.json", "w") as file :
        profile_json["name"] = name
        json.dump(profile_json, file,indent=2)

def view_profile(path):
    player_description = ""
    with open(f"{path}", "r") as file :
        profile_json = json.load(file)
    player_description += profile_json["Profile"]

class Player_Setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Player setup module is ready..")

    @commands.command()
    async def profile(self, ctx):
        username = str(ctx.author)
        file_path = f"Database/Players/{username}.json"
        profile_exist = os.path.exists(f"{file_path}")
        if profile_exist == False :
            shutil.copyfile("Database/profile_template.json", f"{file_path}")
            profile_maker(username)
            print(f"Created new directory for {username}")
        else :
            print(f"{username} is an existing player.. loading profile")

def setup(client):
    client.add_cog(Player_Setup(client))