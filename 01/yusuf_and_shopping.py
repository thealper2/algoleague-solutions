t, idx = map(int, input().split())
freq = {}
for _ in range(t):
    a, b = map(int, input().split())
    freq[b] = freq.get(b, 0) + a
    
sorted_arr = sorted(freq.keys())
cnt = 0
for price in sorted_arr:
    cnt += freq[price]
    if cnt >= idx:
        print(price)
        break
