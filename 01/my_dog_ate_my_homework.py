N = int(input())
nums = list(map(int, input().split()))

max_num = max(nums)
required = set(range(1, max_num + 1))

if required.issubset(set(nums)):
    print("YES")
else:
    print("NO")
