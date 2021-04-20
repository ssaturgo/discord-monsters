import json
import random

with open(f"Database/Players/S H E I K H#6969.json","r") as file :
    profile_json = json.load(file)

tamed = profile_json["Profile"]["Tamed"]
if tamed == 0 :
    with open("Database/monsters.json", "r") as file :
        monsters_json = json.load(file)
        dict_entries = dict.keys(monsters_json)
        list_entries = list(dict_entries)
        result = random.choice(list_entries)
        profile_json["Profile"]["Main"] = result
        profile_json["Discovered"] = result