n = int(input())
arr = list(map(int, input().split()))

freq = {}
max_freq = 0
for val in arr:
    freq[val] = freq.get(val, 0) + 1
    if freq[val] > max_freq:
        max_freq = freq[val]
        
print(n - max_freq)
