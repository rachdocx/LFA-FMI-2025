import json
with open('stari.json') as f:
    data = json.load(f)

def sections(a):
    for key in a:
        print(key)
def states(a, state):
    for key in a.items():
        if key[0] == state:
            print(key[1])

inp=input()
print(data)
stare_actuala=data["start"][0]
print(stare_actuala)
for x in inp:
    for route in data["routes"]:
        if route["inc"]==stare_actuala and route["state"]==x:
            stare_actuala=route["fin"]
            print(stare_actuala)
            break
if stare_actuala==data["final"][0]:
    print("acceptat")
else:
    print("neacceptat")
