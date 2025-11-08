n = int(input())
arr = list(map(int, input().split()))

result = 0
while arr:
    min_val = min(arr)
    result += min_val
    arr = [x - min_val for x in arr if x - min_val > 0]
    
print(result)
