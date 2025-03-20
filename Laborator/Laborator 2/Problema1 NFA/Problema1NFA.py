import json
def epsilon_closure(nfa, states):
    closure = set(states)
    stack = list(states)
    while stack:
        state = stack.pop()
        for route in nfa["routes"]:
            if route["inc"] == state and route["state"] == "ε":
                for next_state in route["fin"]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)
    return closure
def simulate_nfa(nfa, input_string):
    current_states = epsilon_closure(nfa, set(nfa["start"]))
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            for route in nfa["routes"]:
                if route["inc"] == state and route["state"] == symbol:
                    next_states.update(route["fin"])
        current_states = epsilon_closure(nfa, next_states)
    return any(state in nfa["final"] for state in current_states)
with open('NFA.json') as f:
    nfa = json.load(f)
inp = input("Input: ")
result = simulate_nfa(nfa, inp)
print("ACCEPTAT" if result else "RESPINS")
