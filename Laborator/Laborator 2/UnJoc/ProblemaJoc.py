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
print("--------------Menu----------------")
print("States are:")
for x in data["states"]:
    print(x)
print("---------------------------------------------")
print("Directions are:")
for x in data["sigma"]:
    print(x)
print("---------------------------------------------")
print("You're spawned at:")
for x in data["start"]:
    print(x)
print("-----------------------------------------------")
print("To win you need to reach:")
for x in data["final"]:
    print(x)
print("--------------------------------------------------")
print("Additional Rules:")
print("You need the spoon to be able to Exit, Good Luck finding it!")
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
    print("Congratulations! You win!")
elif stare_actuala==data["final"][0] and spoon==0:
    print("Unfortunately, you don't have any spoon!")
elif stare_actuala!=data["final"][0] and spoon==1:
    print("Unfortunately, you didn't found the exit!")
else:
    print("You lost!")
