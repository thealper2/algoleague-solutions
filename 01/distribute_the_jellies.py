def merge(left, right):
	result = []
	i = j = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1

		else:
			result.append(right[j])
			j += 1

	result.extend(left[i:])
	result.extend(right[j:])
	return result


def merge_sort(arr):
	if len(arr) <= 1:
		return arr

	mid = len(arr) // 2
	left = merge_sort(arr[:mid])
	right = merge_sort(arr[mid:])
	return merge(left, right)

N = int(input())
M = int(input())
g = list(map(int, input().split()))
s = list(map(int, input().split()))

g_sorted = merge_sort(g)
s_sorted = merge_sort(s)

i = j = 0
while i < N and j < M:
	if s_sorted[j] >= g_sorted[i]:
		i += 1

	j += 1

print(i)
