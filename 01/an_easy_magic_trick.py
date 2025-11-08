n = int(input())
arr = [int(input()) for _ in range(1024)]

l = 0
r = 1023
order = 0

while l <= r:
    mid = (l + r) // 2
    print(mid + 1, arr[mid])
    order += 1
    if arr[mid] == n:
        break
    
    elif arr[mid] < n:
        l = mid + 1
    
    else:
        r = mid - 1
    
