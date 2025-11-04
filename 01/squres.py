n, m = map(int, input().split())
x, y = n, m
while y:
    x, y = y, x % y
gcd = x
print((n // gcd) * (m // gcd))
