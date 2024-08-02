def in_range(x, y, n):
    return 0 <= x < n and 0<= y < n

def fill(x, y, i):
    table[x][y] = i

def turn(dir):
    return (dir + 1) % 4


def move(x, y, dir):
    nx = x + dxs[dir]
    ny = y + dys[dir]

    return [nx, ny]


n = int(input())
table = [[0 for _ in range(n)] for _ in range(n)]

x, y = n - 1, n - 1
dir = 0

dxs = [0,-1,0,1]
dys = [-1,0,1,0]

for i in range(n ** 2, 0, -1):
    fill(x, y, i)
    nx, ny = move(x, y, dir)

    if not in_range(nx,ny,n) or table[nx][ny]:
        dir = turn(dir)
        nx, ny = move(x, y, dir)
    
    x, y = nx, ny

for row in table:
    for col in row:
        print(col, end=" ")
    print()