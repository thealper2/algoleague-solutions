n = int(input())

while n > 9:
	new_n = 1
	i = 0
	while 10**i <= n:
		d = n // 10**i % 10
		if d != 0:
			new_n *= d

		i += 1

	n = new_n

print(n)
