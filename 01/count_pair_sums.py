n = int(input())
arr = list(map(int, input().split()))
seen = set()
for i in range(n):
    for j in range(i, n):
        s = arr[i] + arr[j]
        if s not in seen:
            seen.add(s)
            
print(len(seen))
