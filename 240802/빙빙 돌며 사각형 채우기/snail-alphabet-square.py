def in_range(x, y, row, col):
    return 0 <= x < row and 0 <= y < col

def fill(x, y, letter_code):
    table[x][y] = chr(letter_code)

def turn(dir):
    return (dir + 1) % 4

def move(x, y, dir):
    nx = x + dxs[dir]
    ny = y + dys[dir]

    return [nx, ny]

n, m = [int(num) for num in input().split()]
table = [[0 for _ in range(m)] for _ in range(n)]

x, y, dir = 0, 0, 0
dxs = [0,1,0,-1]
dys = [1,0,-1,0]

for i in range(n * m):
    letter_code = ord("A") + (i % 26)
    
    fill(x, y, letter_code)
    nx, ny = move(x, y, dir)
    ndir = dir

    if not in_range(nx, ny, n, m) or table[nx][ny]:
        ndir = turn(dir)
        nx, ny = move(x, y, ndir)
    
    x, y, dir = nx, ny, ndir

for row in table:
    for col in row:
        print(col, end=" ")
    print()