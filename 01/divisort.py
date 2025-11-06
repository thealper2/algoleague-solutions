import math

n = int(input())
divisors = []
limit = int(math.sqrt(n))

for i in range(1, limit + 1):
    if n % i == 0:
        divisors.append(i)
        if i != n // i:
            divisors.append(n // i)
            

divisors.sort()
print(' '.join(map(str, divisors)))
