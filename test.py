import json
import random

# with open("Database/Players/S H E I K H#6969.json", "r") as file :
#     profile_json = json.load(file)
# inventory = profile_json["Inventory"]
# item1 = {"apple" : 1}
# inventory.append(item1)
# profile_json["Inventory"] = inventory
# print(profile_json["Inventory"][0]["items"])

# with open("Database/shop_inventory.json", "r") as file :
#     shop_items = json.load(file)
# with open("Database/Players/S H E I K H#6969.json", "r") as file :
#     profile_json = json.load(file)
# profile_json["Inventory"]["Bong Bong"] = 2
# print(profile_json["Inventory"])

with open(f"Database/Players/S H E I K H#6969.json", "r") as file :
    profile_json = json.load(file)
with open("Database/shop_inventory.json", "r") as file :
    shop_json = json.load(file)
for item in shop_json :
    profile_json["Inventory"][f"{item}"] = 0
print(profile_json)