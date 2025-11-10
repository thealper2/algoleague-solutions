n = int(input())
exercises = input().strip().split()
result = []

for exercise in exercises:
    if result and exercise == result[-1]:
        result.pop()
    else:
        result.append(exercise)
        
print(' '.join(result))
