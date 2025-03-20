import json
with open('inputjoc.json') as f:
    data = json.load(f)
#0 sus, 1 jos, 2 dreapta, 3 stanga
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
spoon=0
for x in inp:
    for route in data["routes"]:
        if route["inc"]==stare_actuala and route["state"]==x:
            stare_actuala=route["fin"]
            print(stare_actuala)
            break
        if stare_actuala == "Kitchen":
            spoon = 1
if stare_actuala==data["final"][0] and spoon==1:
    print("ACCEPTAT")
else:
    print("NEACCEPTAT")
