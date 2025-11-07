n = int(input())
cnt = 0
i = 1

while i ** 2 <= n:
    if n % i == 0:
        if i % 2 == 1:
            cnt += 1
            
        other = n // i
        if other != i and other % 2 == 1:
            cnt += 1
            
    i += 1
    
print(cnt)
