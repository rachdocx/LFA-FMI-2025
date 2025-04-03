import json

with open('problema1.json', 'r') as f:
    config = json.load(f)

current_state = config["start"]
stack = []
for route in config["routes"]:
    if route["inc"] == current_state and route["read"] == "ε":
        if route["push"] != "ε":
            stack.append(route["push"])
        current_state = route["fin"]
        break
input_string = input("Introduceti sirul: ")
for x in input_string:
    found = False
    for route in config["routes"]:
        if route["inc"] == current_state and route["read"] == x:
            if route["pop"] == "ε" or (stack and stack[-1] == route["pop"]):
                if route["pop"] != "ε":
                    stack.pop()
                if route["push"] != "ε":
                    stack.append(route["push"])
                current_state = route["fin"]
                found = True
                break
    if not found:
        print("Respins")
        exit()
for route in config["routes"]:
    if route["inc"] == current_state and route["read"] == "ε":
        if stack and stack[-1] == route["pop"]:
            stack.pop()
        current_state = route["fin"]
        break
if current_state in config["final"] and not stack:
    print("Acceptat")
else:
    print("Respins")
