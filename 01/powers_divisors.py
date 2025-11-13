n = int(input())

MOD = 10**9 + 7
factors = {}
temp = n
p = 2
while p * p <= temp:
    while temp % p == 0:
        factors[p] = factors.get(p, 0) + 1
        temp //= p
    p += 1
if temp > 1:
    factors[temp] = factors.get(temp, 0) + 1

result = 1
for exp in factors.values():
    result = (result * (exp * n + 1)) % MOD

print(result)
