class Transition:
    def __init__(self, current_state, input_symbol, stack_top, next_state, stack_push):
        self.current_state = current_state
        self.input_symbol = input_symbol
        self.stack_top = stack_top
        self.next_state = next_state
        self.stack_push = stack_push

    def __repr__(self):
        return f"({self.current_state}, {self.input_symbol}, {self.stack_top}) -> ({self.next_state}, {self.stack_push})"