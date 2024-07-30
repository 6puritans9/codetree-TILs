def in_range(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def turn(dir):
    return (dir + 1) % 4

def move(dir, x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]

    return [nx, ny]

n, m = [int(num) for num in input().split()]
table = [[0 for _ in range(m)] for _ in range(n)]

directions = {
    "R": 0,
    "D": 1,
    "L": 2,
    "U": 3
}

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = directions["R"]
x, y = 0, 0

for i in range(1, n*m + 1):
    table[x][y] = i
    nx, ny = move(dir, x, y)

    if not in_range(nx, ny, n, m) or table[nx][ny] != 0:
        dir = turn(dir)
        nx, ny = move(dir, x, y)
    
    x, y = nx, ny

for row in table:
    for col in row:
        print(col, end=" ")
    print()