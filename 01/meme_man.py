n = int(input())
x, y = map(int, input().split())
if x > y:
	x, y = y, x

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
	if i >= x:
		dp[i] += dp[i - x]
	if i >= y:
		dp[i] += dp[i - y]

print(dp[n])
