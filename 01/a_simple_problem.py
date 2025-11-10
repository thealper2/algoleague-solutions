n = int(input())
numbers = list(map(int, input().split()))
result = 0
for number in numbers:
    result ^= number
    
print(result)
