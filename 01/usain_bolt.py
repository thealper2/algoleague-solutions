n = int(input())
records = list(map(int, input().split()))
max_record = records[0]
result = 0
for record in records[1:]:
	if record > max_record:
		max_record = record
		result += 1

print(result)
