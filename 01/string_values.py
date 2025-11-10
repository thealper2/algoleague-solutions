N, M = map(int, input().split())

if M < N or M > 26 * N:
    print(-1)
else:
    result = ['a'] * N
    extra = M - N
    
    i = N - 1
    while extra > 0:
        add = min(25, extra)
        result[i] = chr(ord('a') + add)
        extra -= add
        i -= 1
    
    print("".join(result))
