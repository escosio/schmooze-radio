import json
import sys

# get the team value index as param
param = int(sys.argv[1])
team_index = str(param + 1)
file_path="/Users/scottdantuono/yahoo-fantasy-baseball-reader/allMyData.json"
owners = {'1': "Meet me at Stan's", '2': 'Boat Lords', '3': 'Bring back Mookie', '4': "Dan's Fancy Boys", '5': 'Dog Days Denizens', '6': 'Green Monster', '7': 'IfILoseIBlameScott', '8': 'JC Rubber Arms', '9': 'Oppen-Jeimer', '10': 'Melkman', '11': "Normentino's Ninos", '12': 'The 40-Year-Old Verlanders', '13': 'The Asian Sensations', '14': "Wayne's Primo Team"}

f = open(file_path)
data = json.load(f)

team_name = owners[str(param)]

for player in data["my players"]:
    print(team_name, player["name"]["full"], player["editorial_team_abbr"], player["display_position"], sep=",")