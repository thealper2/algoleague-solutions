n, k = map(int, input().split())
S = list(map(int, input().split()))
Q = int(input())

for _ in range(Q):
    t = int(input())
    low = k - t
    high = k + t
    
    left = 0
    right = n - 1
    first_idx = n
    
    while left <= right:
        mid = (left + right) // 2
        if S[mid] >= low:
            first_idx = mid
            right = mid - 1
        else:
            left = mid + 1
            
    left = 0
    right = n - 1
    last_idx = -1
    
    while left <= right:
        mid = (left + right) // 2
        if S[mid] <= high:
            last_idx = mid
            left = mid + 1
        else:
            right = mid - 1
            
    if first_idx <= last_idx:
        print(last_idx - first_idx + 1)
    else:
        print(0)
