class PDA:
    def __init__(
        self,
        states,
        input_alphabet,
        stack_alphabet,
        transitions,
        start_state,
        start_stack,
        accept_states
    ):
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.start_stack = start_stack
        self.accept_states = accept_states

    def __repr__(self):
        return (
            f"PDA(\n"
            f"  States: {self.states}\n"
            f"  Input Alphabet: {self.input_alphabet}\n"
            f"  Stack Alphabet: {self.stack_alphabet}\n"
            f"  Start State: {self.start_state}\n"
            f"  Start Stack: {self.start_stack}\n"
            f"  Accept States: {self.accept_states}\n"
            f"  Transitions: {len(self.transitions)}\n"
            f")"
        )