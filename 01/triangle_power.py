N = int(input())

a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x4, y4 = map(int, input().split())
x5, y5 = map(int, input().split())
x6, y6 = map(int, input().split())

def power(x1, y1, x2, y2, x3, y3):
	return (x2 + y2 + x3 + y3) - 2 * (x1 + y1)

power1 = power(a, b, c, d, e, f)
power2 = power(x4, y4, x5, y5, x6, y6)

if N == 1:
	print(power1)
elif N == 2:
	print(power2)
else:
	base = (c + d + e + f) - 2 * (a + b)
	for _ in range(3, N + 1):
		powerN = base + 2 * power2 + 2 * power1
		power1, power2 = power2, powerN

	print(powerN)
