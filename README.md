# otomata-coding-assignment-w4-235-268-275-292
otomata-coding-assignment-w4-235-268-275-292
# Tugas Minggu ke-4 Otomata
| Name           | NRP        | Kelas     |
| ---            | ---        | ----------|
| Algof Kristian Zega | 5025231235 | Otomata (E) |
| Gregorius Setiadharma | 5025231268 | Otomata (E) |
| Muhammad Davin Aulia Risky | 5025231275 | Otomata (E) |
| Muhammad Aditya Handrian | 5025231292 | Otomata (E) |

## Program Simulator DFA

> Implement DFA Simulator. Write explanation, how to use, example input and output

- Screenshot

![contoh-input-output](./asset/contoh_input_output_1.jpg)

- Source code
    ```py
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
    
    # Example DFA data (based on the image input format)
    # Sample input 1
    dfa_json = '''
    {
        "states": ["q0", "q1", "q2", "q3"],
        "alphabet": ["a", "b"],
        "start_state": "q0",
        "accept_states": ["q2", "q3"],
        "transitions": {
            "q0": { "a": "q1", "b": "q3" },
            "q1": { "a": "q1", "b": "q2" },
            "q2": { "a": "q1", "b": "q3" },
            "q3": { "a": "q2", "b": "q3" }
        },
        "test_string": "aa"
    }
    '''
    
    # Mencari jawaban sample input 1
    dfa_data = json.loads(dfa_json)
    print(f"Sample input 1: {dfa_data['test_string']}")
    run_dfa(dfa_data)
    print("\n")
    
    # Sample input 2
    dfa_json = '''
    {
        "states": ["q0", "q1", "q2", "q3"],
        "alphabet": ["a", "b"],
        "start_state": "q0",
        "accept_states": ["q2", "q3"],
        "transitions": {
            "q0": { "a": "q1", "b": "q3" },
            "q1": { "a": "q1", "b": "q2" },
            "q2": { "a": "q1", "b": "q3" },
            "q3": { "a": "q2", "b": "q3" }
        },
        "test_string": "ab"
    }
    '''
    
    # Mencari jawaban sample input 2
    dfa_data = json.loads(dfa_json)
    print(f"Sample input 2: {dfa_data['test_string']}")
    run_dfa(dfa_data)
    ```

- Explanation
