n = int(input())
s = input().strip()
diff1 = 0
diff2 = 0

for i in range(n):
	if i % 2 == 0:
		if s[i] != '0':
			diff1 += 1
		if s[i] != '1':
			diff2 += 1

	else:
		if s[i] != '1':
			diff1 += 1
		if s[i] != '0':
			diff2 += 1

print(min(diff1, diff2))
