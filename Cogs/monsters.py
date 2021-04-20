import discord
from discord.ext import commands
import json
import random

class Monsters(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def starter(self, ctx):
        username = str(ctx.author)
        with open(f"Database/Players/{username}.json","r") as file :
            profile_json = json.load(file)

        tamed = profile_json["Profile"]["Tamed"]
        if tamed == 0 :
            with open(f"Database/monsters.json", "r") as file :
                monsters_json = json.load(file)
                dict_entries = dict.keys(monsters_json)
                list_entries = list(dict_entries)
                result = random.choice(list_entries)
                monster_gif = monsters_json[result]["Profile"]["image"]
            with open(f"Database/Players/{username}.json", "w") as file :
                profile_json["Profile"]["Main"] = result
                profile_json["Discovered"] = result
                profile_json["Profile"]["Tamed"] += 1
                json.dump(profile_json, file, indent=2)
            print(f"Given Starter to {username}")
            embed_msg = discord.Embed(
                title=f"Congratulations! you got {result}!",
                description=monster_gif,
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed_msg)
        else :
            await ctx.send("You already have a Starter")
def setup(client):
    client.add_cog(Monsters(client))