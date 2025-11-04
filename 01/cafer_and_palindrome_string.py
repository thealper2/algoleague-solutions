n = int(input())
word = input().strip()

freq = {}
odd_count = 0
for c in word:
    freq[c] = freq.get(c, 0) + 1
    
for k, v in freq.items():
    if v % 2 == 1:
        odd_count += 1
        
    if odd_count > 1:
        break
    
if odd_count > 1:
    print('NO')
else:
    print('YES')
