import json

with open('Database/shop_inventory.json') as file :
    shop_inventory = json.load(file)

# print(shop_inventory["hugs"]['quantity'])
item_list = "lmao"

for item in shop_inventory :
    item_entry = "emoji" + "|" + shop_inventory[item]["name"] + "|" + str(shop_inventory[item]["cost"])
    item_list += item_entry

print(item_list)