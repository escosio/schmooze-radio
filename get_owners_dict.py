import json

f = open("teams.json")
data = json.load(f)

owners_dict = {}

for x in range(0, 14):
    owner_id = data["fantasy_content"]["league"]["teams"][x]["team"]["team_id"]
    owner_name = data["fantasy_content"]["league"]["teams"][x]["team"]["name"]
    owners_dict[owner_id] = owner_name

# print(owners_dict)