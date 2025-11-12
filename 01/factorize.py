n = int(input())
i = 2
factors = []
while i ** 2 <= n:
    if n % i:
        i += 1
    else:
        n //= i
        factors.append(i)
        
if n > 1:
    factors.append(n)
    
print(' '.join(map(str, factors)))
