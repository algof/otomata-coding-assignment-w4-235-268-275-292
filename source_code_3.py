from automata.fa.dfa import DFA
import json

json_string = '''
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

data = json.loads(json_string)

dfa = DFA(
    states=set(data["states"]),
    input_symbols=set(data["alphabet"]),
    transitions=data["transitions"],
    initial_state=data['start_state'],
    final_states=set(data["accept_states"])
)

print(dfa.accepts_input(data['test_string']))  # True
print(dfa.accepts_input('aa'))  # False