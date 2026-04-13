import json

from backend.core.pda import PDA
from backend.core.transition import Transition


def load_pda_from_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    transitions = []
    for t in data["transitions"]:
        transition = Transition(
            current_state=t["current_state"],
            input_symbol=t["input_symbol"],
            stack_top=t["stack_top"],
            next_state=t["next_state"],
            stack_push=t["stack_push"]
        )
        transitions.append(transition)

    pda = PDA(
        states=data["states"],
        input_alphabet=data["input_alphabet"],
        stack_alphabet=data["stack_alphabet"],
        transitions=transitions,
        start_state=data["start_state"],
        start_stack=data["start_stack"],
        accept_states=data["accept_states"]
    )

    return pda