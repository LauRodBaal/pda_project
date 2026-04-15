from backend.services.json_loader import load_pda_from_json
from backend.converters.cfg_converter import convert_pda_to_cfg

samples = ["anbn.json", "palindrome.json", "parentheses.json"]

for sample in samples:
    print(f"\n--- Testing CFG conversion for {sample} ---")
    pda = load_pda_from_json(f"backend/samples/{sample}")
    cfg = convert_pda_to_cfg(pda)
    print(cfg)