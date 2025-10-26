M = int(input())
A = list(map(int, input().split()))
N = int(input())

total_initial = sum(A)
if (total_initial + N) % M == 0:
	final_per_child = (total_initial + N) // M
	if final_per_child >= max(A):
		print(1)
	else:
		print(0)
else:
	print(0)
