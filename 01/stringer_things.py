n = int(input())
s = list(input())

result = []
for i in range(n):
	if i == 0 or s[i] != s[i - 1]:
		result.append(s[i])

print(''.join(result))
