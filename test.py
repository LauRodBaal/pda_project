from backend.services.json_loader import load_pda_from_json
from backend.core.simulator import PDASimulator


def test_sample(sample_file, test_strings):
    print(f"\n--- Testing {sample_file} ---")

    pda = load_pda_from_json(f"backend/samples/{sample_file}")
    simulator = PDASimulator(pda)

    for s in test_strings:
        result = simulator.simulate(s)
        print(f"Input: {s!r} -> Accepted: {result['accepted']}")


# Test anbn
test_sample("anbn.json", ["ab", "aabb", "aaabbb", "aab", "abba"])

# Test palindrome
test_sample("palindrome.json", ["abba", "aba", "aa", "abab", "abb"])

# Test parentheses
test_sample("parentheses.json", ["()", "(())", "()()", "(()", "())", "())()"])