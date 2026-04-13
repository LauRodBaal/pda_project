def validate_pda(pda):
    if pda.start_state not in pda.states:
        raise ValueError("Start state is not in the set of states")

    for state in pda.accept_states:
        if state not in pda.states:
            raise ValueError(f"Accept state '{state}' is not in the set of states")

    for t in pda.transitions:
        if t.current_state not in pda.states:
            raise ValueError(f"Invalid current state in transition: {t}")

        if t.next_state not in pda.states:
            raise ValueError(f"Invalid next state in transition: {t}")

        if t.input_symbol != "" and t.input_symbol not in pda.input_alphabet:
            raise ValueError(f"Invalid input symbol in transition: {t}")

        if t.stack_top not in pda.stack_alphabet:
            raise ValueError(f"Invalid stack symbol in transition: {t}")

    return True