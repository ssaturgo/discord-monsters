import json
import random

with open("Database/shop_inventory.json", "r") as file :
    items_json = json.load(file)
    items = list(items_json.keys())
    treasure = random.choice(items)
print(treasure)