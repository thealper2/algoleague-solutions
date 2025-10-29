n = int(input())

if n == 0:
	print(0)
else:
	n %= 60
	a, b = 0, 1
	for _ in range(n):
		a, b = b, (a + b) % 10

print(a)
