n = int(input())
arr = list(map(int, input().split()))
arr.sort()
prev = 0
total_increments = 0

for num in arr:
	if num > prev:
		prev = num
	else:
		total_increments += (prev + 1 - num)
		prev += 1

print(total_increments)
