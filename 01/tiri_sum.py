n = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()
found = False
for i in range(n - 2):
	if i > 0 and arr[i] == arr[i - 1]:
		continue

	if sum(arr[i:i+3]) > target:
		break

	l, r = i + 1, n - 1
	while l < r:
		sub = arr[i] + arr[l] + arr[r]
		if sub == target:
			found = True
			break

		elif sub < target:
			l += 1

		else:
			r -= 1

if found:
	print('YES')
else:
	print('NO')
