operator = input().strip()
a = int(input())
b = int(input())

if operator == 'addition':
    result = a + b
elif operator == 'subtraction':
    result = a - b
elif operator == 'multiplication':
    result = a * b
elif operator == 'power':
    result = a ** b
    
print(result)
