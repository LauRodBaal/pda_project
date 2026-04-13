from backend.services.sample_service import list_samples, load_sample

print(list_samples())

pda = load_sample("palindrome.json")
print(pda)

pda2 = load_sample("parentheses.json")
print(pda2)