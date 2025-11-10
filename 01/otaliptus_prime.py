n = int(input())
numbers = list(map(int, input().split()))
seen = {}

def is_prime(num):
    if num < 2:
        return False
        
    if num == 2:
        return True
        
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
            
    return True
    
for number in numbers:
    if number in seen.keys():
        result = seen[number]
    else:
        result = is_prime(number)
        seen[number] = result
        
    if result:
        print('Yes')
    else:
        print('No')
