def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def fill(x, y, i):   
    table[x][y] = i


def turn(dir):
    return (dir + 1) % 4


def move(x, y, dir):
    nx = x + dxs[dir]
    ny = y + dys[dir]

    return [nx, ny]


n, m = [int(num) for num in input().split()]
table = [[0 for _ in range(m)] for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0
dir = 0

for i in range(1, (n * m) + 1):    
    fill(x, y, i)
    nx, ny = move(x, y, dir)
    ndir = dir

    if not in_range(nx, ny) or table[nx][ny]:
        ndir = turn(ndir)
        nx, ny = move(x, y, ndir)
        
    x, y, dir = nx, ny, ndir

for row in table:
    for col in row:
        print(col, end = " ")
    print()