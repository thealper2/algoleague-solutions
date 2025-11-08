t, N = map(int, input().split())
digit_sum = lambda x: sum(int(d) for d in str(x))
seen = {}
step = 0
states = []

while step < N:
    if t in seen:
        cycle_start = seen[t]
        cycle_length = step - cycle_start
        remaining = N - step
        t = states[cycle_start + (remaining % cycle_length)]
        break
    
    seen[t] = step
    states.append(t)
    t = (t + digit_sum(t)) % 24
    t = (t - digit_sum(t)) % 24
    step += 1

if t == 0 or t == 9:
    print("NO")
else:
    print("YES")

