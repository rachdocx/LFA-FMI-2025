import json
with open('stari.json') as f:
    data = json.load(f)     #am cautat pe net
for x in data.items():
    print(x)
print(data)