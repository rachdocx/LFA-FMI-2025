import json
def epsilon_closure(nfa, states):
    closure = set(states)
    changed = True
    while changed:
        changed = False
        for state in list(closure):
            for route in nfa["routes"]:
                if route["inc"] == state and route["state"] == "ε":
                    for next_state in route["fin"]:
                        if next_state not in closure:
                            closure.add(next_state)
                            changed = True
    return closure
def simulate_nfa(nfa, input_string):
    stari_curente = epsilon_closure(nfa, set(nfa["start"]))
    for simbol in input_string:
        stari_noi = set()
        for state in stari_curente:
            for route in nfa["routes"]:
                if route["inc"] == state and route["state"] == simbol:
                    stari_noi.update(route["fin"])
        stari_curente = epsilon_closure(nfa, stari_noi)
    return any(state in nfa["final"] for state in stari_curente)
with open('NFA.json') as f:
    nfa = json.load(f)
inp = input("Input: ")
result = simulate_nfa(nfa, inp)
print("ACCEPTAT" if result else "RESPINS")
