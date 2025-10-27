n, k = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
r = (-total) % k
if r == 0:
	r = k

a_set = set(a)
while r in a_set:
	r += k

print(r)
