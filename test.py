from backend.services.json_loader import load_pda_from_json
from backend.services.graph_renderer import render_pda_graph

pda = load_pda_from_json("backend/samples/anbn.json")
graph = render_pda_graph(pda)

print(graph)