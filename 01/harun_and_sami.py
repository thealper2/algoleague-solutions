n, k = map(int, input().split())
games = input()
h_count = games.count('H')
s_count = k - h_count
remaining = n - k
if h_count > s_count + remaining:
	print('Harun')
elif s_count > h_count + remaining:
	print('Sami')
else:
	print('Cilek')
