import json
with open('some_tournaments.json', 'r') as data:
    data = json.load(data)

with open('better.json', 'w') as outf:
    json.dump(data, outf, indent=4)
