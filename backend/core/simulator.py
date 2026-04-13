from collections import deque
from copy import deepcopy

EPSILON = ""


class PDASimulator:
    def __init__(self, pda_definition: dict):
        self.pda = pda_definition
        self.transitions = pda_definition.get("transitions", [])
        self.start_state = pda_definition.get("start_state")
        self.start_stack_symbol = pda_definition.get("start_stack_symbol")
        self.accept_states = set(pda_definition.get("accept_states", []))

    def simulate(self, input_string: str, max_steps: int = 1000) -> dict:
        initial_config = {
            "state": self.start_state,
            "position": 0,
            "stack": [self.start_stack_symbol],
            "trace": []
        }

        queue = deque([initial_config])
        visited = set()
        steps = 0

        while queue and steps < max_steps:
            current = queue.popleft()
            steps += 1

            state = current["state"]
            position = current["position"]
            stack = current["stack"]

            visit_key = (state, position, tuple(stack))
            if visit_key in visited:
                continue
            visited.add(visit_key)

            if self._is_accepting(state, position, input_string):
                return {
                    "accepted": True,
                    "message": "Cadena aceptada por el PDA.",
                    "final_state": state,
                    "steps_explored": steps,
                    "trace": current["trace"]
                }

            applicable = self._get_applicable_transitions(
                state=state,
                position=position,
                input_string=input_string,
                stack=stack
            )

            for transition in applicable:
                next_config = self._apply_transition(
                    config=current,
                    transition=transition,
                    input_string=input_string
                )
                queue.append(next_config)

        return {
            "accepted": False,
            "message": "Cadena rechazada por el PDA.",
            "final_state": None,
            "steps_explored": steps,
            "trace": []
        }

    def _is_accepting(self, state: str, position: int, input_string: str) -> bool:
        return state in self.accept_states and position == len(input_string)

    def _get_applicable_transitions(
        self,
        state: str,
        position: int,
        input_string: str,
        stack: list
    ) -> list:
        applicable = []
        current_symbol = input_string[position] if position < len(input_string) else None
        stack_top = stack[-1] if stack else None

        for transition in self.transitions:
            if transition.get("from_state") != state:
                continue

            required_input = transition.get("input_symbol", EPSILON)
            required_stack_top = transition.get("stack_top")

            input_matches = (
                required_input == EPSILON or
                (current_symbol is not None and required_input == current_symbol)
            )

            stack_matches = stack_top == required_stack_top

            if input_matches and stack_matches:
                applicable.append(transition)

        return applicable

    def _apply_transition(self, config: dict, transition: dict, input_string: str) -> dict:
        state = config["state"]
        position = config["position"]
        stack_before = deepcopy(config["stack"])
        stack_after = deepcopy(config["stack"])
        trace = deepcopy(config["trace"])

        input_symbol = transition.get("input_symbol", EPSILON)
        stack_top = transition.get("stack_top")
        next_state = transition.get("to_state")
        push_symbols = transition.get("push", [])

        popped_symbol = None
        if stack_after and stack_after[-1] == stack_top:
            popped_symbol = stack_after.pop()

        for symbol in reversed(push_symbols):
            stack_after.append(symbol)

        next_position = position
        if input_symbol != EPSILON:
            next_position += 1

        step_record = {
            "from_state": state,
            "to_state": next_state,
            "input_symbol": input_symbol,
            "consumed": input_symbol if input_symbol != EPSILON else "ε",
            "stack_top_expected": stack_top,
            "popped": popped_symbol,
            "push": push_symbols,
            "position_before": position,
            "position_after": next_position,
            "remaining_input_before": input_string[position:],
            "remaining_input_after": input_string[next_position:],
            "stack_before": stack_before,
            "stack_after": stack_after
        }

        trace.append(step_record)

        return {
            "state": next_state,
            "position": next_position,
            "stack": stack_after,
            "trace": trace
        }