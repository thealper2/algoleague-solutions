n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_A = max(A)
min_B = min(B)

if max_A > min_B:
    print(0)
else:
    print(min_B - max_A + 1)
