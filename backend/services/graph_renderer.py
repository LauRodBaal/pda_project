def render_pda_graph(pda):
    nodes = []
    edges = []

    for state in pda.states:
        node = {
            "id": state,
            "label": state,
            "start": state == pda.start_state,
            "accept": state in pda.accept_states
        }
        nodes.append(node)

    for transition in pda.transitions:
        input_symbol = transition.input_symbol if transition.input_symbol != "" else "ε"
        stack_push = transition.stack_push if transition.stack_push != "" else "ε"

        edge = {
            "from": transition.current_state,
            "to": transition.next_state,
            "label": f"{input_symbol}, {transition.stack_top} → {stack_push}"
        }
        edges.append(edge)

    return {
        "nodes": nodes,
        "edges": edges
    }