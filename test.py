from backend.services.json_loader import load_pda_from_json
from backend.core.validator import validate_pda

pda = load_pda_from_json("backend/samples/anbn.json")

print(pda)
print(validate_pda(pda))