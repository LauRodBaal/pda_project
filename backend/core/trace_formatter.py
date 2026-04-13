def format_trace(trace: list) -> list:
    formatted_steps = []

    for index, step in enumerate(trace, start=1):
        push_symbols = step.get("push", [])
        push_text = "".join(push_symbols) if push_symbols else "ε"

        formatted_steps.append({
            "step": index,
            "from_state": step.get("from_state"),
            "to_state": step.get("to_state"),
            "consumed": step.get("consumed"),
            "stack_before": step.get("stack_before", []),
            "stack_after": step.get("stack_after", []),
            "remaining_input_before": step.get("remaining_input_before", ""),
            "remaining_input_after": step.get("remaining_input_after", ""),
            "position_before": step.get("position_before"),
            "position_after": step.get("position_after"),
            "transition_label": (
                f"({step.get('consumed')}, "
                f"{step.get('stack_top_expected')} -> {push_text})"
            )
        })

    return formatted_steps


def format_simulation_result(result: dict) -> dict:
    return {
        "accepted": result.get("accepted", False),
        "message": result.get("message", ""),
        "final_state": result.get("final_state"),
        "steps_explored": result.get("steps_explored", 0),
        "trace": format_trace(result.get("trace", []))
    }