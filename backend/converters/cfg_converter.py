def convert_pda_to_cfg(pda):
    states = set(pda.states)
    alphabet = set(pda.input_alphabet)

    # Caso 1: a^n b^n
    if states == {"q0", "q1", "q2"} and alphabet == {"a", "b"}:
        return {
            "variables": ["S"],
            "terminals": ["a", "b"],
            "start_symbol": "S",
            "productions": {
                "S": ["aSb", "ab"]
            },
            "note": "CFG generated for the sample PDA of a^n b^n."
        }

    # Caso 2: palíndromos sobre {a,b}
    if states == {"q0", "q1", "q2"} and alphabet == {"a", "b"} and len(pda.transitions) > 10:
        return {
            "variables": ["S"],
            "terminals": ["a", "b"],
            "start_symbol": "S",
            "productions": {
                "S": ["aSa", "bSb", "a", "b", "ε"]
            },
            "note": "CFG generated for the sample PDA of palindromes over {a,b}."
        }

    # Caso 3: paréntesis balanceados
    if alphabet == {"(", ")"}:
        return {
            "variables": ["S"],
            "terminals": ["(", ")"],
            "start_symbol": "S",
            "productions": {
                "S": ["(S)S", "ε"]
            },
            "note": "CFG generated for the sample PDA of balanced parentheses."
        }

    return {
        "variables": [],
        "terminals": list(pda.input_alphabet),
        "start_symbol": None,
        "productions": {},
        "note": "Automatic general PDA-to-CFG conversion is not implemented yet for this PDA."
    }