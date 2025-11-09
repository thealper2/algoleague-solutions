n, m = map(int, input().split())
edges = set()
for _ in range(m):
    u, v = map(int, input().split())
    edges.add((u, v))
    
bidirected = True
for (u, v) in edges:
    if (v, u) not in edges:
        bidirected = False
        break
    
print('Yes' if bidirected else 'No')
