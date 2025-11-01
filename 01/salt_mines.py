n = int(input())
s = input()
m = int(input())
w = input()
idx = 0
result = 0
while idx < n:
	if s[idx:idx+m] == w:
		result += 1
		idx += m
	else:
		idx += 1

print(result)
