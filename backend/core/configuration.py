class Configuration:
    def __init__(self, state, remaining_input, stack):
        self.state = state
        self.remaining_input = remaining_input
        self.stack = stack

    def __repr__(self):
        return f"State: {self.state}, Input: {self.remaining_input}, Stack: {self.stack}"