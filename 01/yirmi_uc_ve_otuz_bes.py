N, M = map(int, input().split())
image = [list(map(int, input().split())) for _ in range(N)]
result = [row[:] for row in image]

dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for r in range(N):
    for c in range(M):
        val = image[r][c]
        if val not in (23, 35):
            continue
        
        target = 23 if val == 35 else 35
        found = False
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and image[nr][nc] == val:
                found = True
                break
        
        if not found:
            result[r][c] = target

for row in result:
    print(' '.join(map(str, row)))
