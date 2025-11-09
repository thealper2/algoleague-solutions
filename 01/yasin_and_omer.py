N, T, P = map(int, input().split())
can_damage = False
for _ in range(N):
    X, Y = map(int, input().split())
    if X < T and Y > P:
        can_damage = True
        
print('Yes' if can_damage else 'No')
