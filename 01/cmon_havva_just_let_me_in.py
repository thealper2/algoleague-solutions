n = int(input())
s = input().strip()

cnt = 0
for i in range(n):
    for j in range(i + 2, n + 1):
        substr = s[i:j]
        if substr == substr[::-1]:
            cnt += 1
            
print(cnt)
