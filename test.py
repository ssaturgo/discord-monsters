import json

def view_profile(path):
    with open(f"{path}", "r") as file :
        profile_json = json.load(file)
    for i in profile_json["Profile"]:
        print (i)

view_profile("Database/profile_template.json")