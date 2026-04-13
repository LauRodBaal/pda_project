from backend.core.transition import Transition
from backend.core.pda import PDA

t1 = Transition("q0", "a", "Z", "q0", "AZ")
t2 = Transition("q0", "b", "A", "q1", "")

pda = PDA(
    states=["q0", "q1"],
    input_alphabet=["a", "b"],
    stack_alphabet=["Z", "A"],
    transitions=[t1, t2],
    start_state="q0",
    start_stack="Z",
    accept_states=["q1"]
)

print(pda)