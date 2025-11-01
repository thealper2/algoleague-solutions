t = int(input())
for _ in range(t):
	n = int(input())
	message = input()
	if any(c.isupper() for c in message):
		print("Have some chamomile tea")
	else:
		print("No problem")
