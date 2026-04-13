class Transition:
    def __init__(self, current_state, input_symbol, stack_top, next_state, stack_push):
        self.current_state = current_state
        self.input_symbol = input_symbol
        self.stack_top = stack_top
        self.next_state = next_state
        self.stack_push = stack_push

    def __repr__(self):
        input_display = self.input_symbol if self.input_symbol != "" else "ε"
        push_display = self.stack_push if self.stack_push != "" else "ε"

        return (
            f"({self.current_state}, {input_display}, {self.stack_top}) "
            f"-> ({self.next_state}, {push_display})"
        )
    
    