import math

n = 7
p = 1/4
q = 3/4

def p_k(k):
    return math.comb(n, k) * (p**k) * (q**(n-k))

probs = {k: p_k(k) for k in range(n + 1)}

for k, prob in probs.items():
    print(f"Exactly {k} times: {prob:.5f} ({math.comb(n, k)} * (1/4)^{k} * (3/4)^{n-k})")

p_at_least_1 = 1 - probs[0]
p_at_least_2 = 1 - probs[0] - probs[1]

print(f"At least once: {p_at_least_1:.5f}")
print(f"At least twice: {p_at_least_2:.5f}")
