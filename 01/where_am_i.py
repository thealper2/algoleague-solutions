n, x, y = map(int, input().split())
lower_bound = max(x + 1, n - y)
if lower_bound > n:
    print(0)
else:
    print(n - lower_bound + 1)
