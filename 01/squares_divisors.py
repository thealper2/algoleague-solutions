n = int(input())
factors = {}
temp = n
d = 2
while d ** 2 <= temp:
    while temp % d == 0:
        factors[d] = factors.get(d, 0) + 1
        temp //= d
        
    d += 1
    
if temp > 1:
    factors[temp] = factors.get(temp, 0) + 1
    
result = 1
for exp in factors.values():
    result *= (2 * exp + 1)
    
print(result)
