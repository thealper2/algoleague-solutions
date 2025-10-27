Q = int(input())
beaten = set()

for _ in range(Q):
	query = input().split()
	if query[0] == '1':
		x = int(query[1])
		beaten.add(x)

	else:
		a = int(query[1])
		b = int(query[2])
		if (a - b) in beaten and a in beaten and (a + b) in beaten:
			print('GG EZ')
		else:
			print('GLHF')
