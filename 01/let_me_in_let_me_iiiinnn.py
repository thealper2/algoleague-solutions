n = int(input())
s = list(input().strip())

l, r = 0, len(s) - 1

while l <= r:
    if s[l] == '#' and s[r] == '#':
        print(-1)
        exit()

    elif s[l] == '#':
        s[l] = s[r]

    elif s[r] == '#':
        s[r] = s[l]

    elif s[l] != s[r]:
        print(-1)
        exit()

    l += 1
    r -= 1

print(''.join(s))
