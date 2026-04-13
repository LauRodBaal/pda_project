class PDA:
    def __init__(self, states, input_alphabet, stack_alphabet, transitions,
                 start_state, start_stack, accept_states):
        
        self.states = states
        self.input_alphabet = input_alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        
        self.start_state = start_state
        self.start_stack = start_stack
        self.accept_states = accept_states