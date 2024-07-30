def in_range(x, y, N):
    return 0<= x < N and 0<= y < N

N, M = [int(num) for num in input().split()]
table = [[0 for _ in range(N)] for _ in range(N)]

dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0] 

for _ in range(M):
    _x, _y = [int(num) for num in input().split()]
    x, y = _x - 1, _y  - 1
    table[x][y] = 1
    count = 0

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if in_range(nx, ny, N):
            count += 1 if table[nx][ny] else 0
    
    if count >= 3:
        print(1)
        continue
    print(0)