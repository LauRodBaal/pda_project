from collections import deque
from copy import deepcopy

EPSILON = ""


class PDASimulator:
    def __init__(self, pda):
        self.pda = pda
        self.transitions = pda.transitions
        self.start_state = pda.start_state
        self.start_stack_symbol = pda.start_stack
        self.accept_states = set(pda.accept_states)

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
            if transition.current_state != state:
                continue

            required_input = transition.input_symbol
            required_stack_top = transition.stack_top

            input_matches = (
                required_input == EPSILON or
                (current_symbol is not None and required_input == current_symbol)
            )

            stack_matches = stack_top == required_stack_top

            if input_matches and stack_matches:
                applicable.append(transition)

        return applicable

    def _apply_transition(self, config: dict, transition, input_string: str) -> dict:
        state = config["state"]
        position = config["position"]
        stack_before = deepcopy(config["stack"])
        stack_after = deepcopy(config["stack"])
        trace = deepcopy(config["trace"])

        input_symbol = transition.input_symbol
        stack_top = transition.stack_top
        next_state = transition.next_state
        stack_push = transition.stack_push

        popped_symbol = None
        if stack_after and stack_after[-1] == stack_top:
            popped_symbol = stack_after.pop()

        if stack_push != EPSILON and stack_push != "":
            for symbol in reversed(stack_push):
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
            "push": stack_push if stack_push != "" else "ε",
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