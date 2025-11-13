def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
                
    return is_prime
    
n = int(input())
queries = [tuple(map(int, input().split())) for _ in range(n)]
max_b = max(b for a, b in queries)
is_prime = sieve(max_b)
prefix = [0] * (max_b + 2)
for i in range(1, max_b + 1):
    prefix[i] = prefix[i - 1] + (1 if is_prime[i] else 0)
    
for a, b in queries:
    print(prefix[b] - prefix[a - 1])
