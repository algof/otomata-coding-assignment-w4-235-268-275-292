import json

def run_dfa(dfa_data):
    states = dfa_data["states"]
    alphabet = dfa_data["alphabet"]
    start_state = dfa_data["start_state"]
    accept_states = dfa_data["accept_states"]
    transitions = dfa_data["transitions"]
    test_string = dfa_data["test_string"]

    current_state = start_state
    path = [current_state]

    for symbol in test_string:
        if symbol not in alphabet:
            print(f"Error: Symbol '{symbol}' not in DFA alphabet")
            return
        current_state = transitions[current_state][symbol]
        path.append(current_state)

    status = "ACCEPTED" if current_state in accept_states else "REJECTED"
    print("Path:", " → ".join(path))
    print("Status:", status)

file_path = "dfa_test.json"

try:
    with open(file_path, "r") as file:
        dfa_data = json.load(file)  # Mencoba membaca JSON
        run_dfa(dfa_data)
except FileNotFoundError:
    print(f"Error: File '{file_path}' tidak ditemukan.")
except json.JSONDecodeError as e:
    print("Error: Format JSON tidak valid.")