n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    diff = abs(a - b)

    if diff >= 2:
        print('Yes')
    else:
        print('No')
