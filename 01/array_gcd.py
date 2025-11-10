n = int(input())
nums = list(map(int, input().split()))

def gcd(a, b):
    if a == 0:
        return b
        
    return gcd(b % a, a)
    
result = nums[0]
for num in nums[1:]:
    result = gcd(num, result)
    
print(result)
