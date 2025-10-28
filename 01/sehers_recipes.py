N = int(input())
diffs = list(map(int, input().split()))
diffs.sort()

if N % 2 != 0:
	print(0)
else:
	mid = N // 2
	left = diffs[mid - 1]
	right = diffs[mid]
	print(max(0, right - left))
