def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

def turn(dir):
    return (3 - dir)

def move(dir, x, y):
    nx = x + dx[dir]
    ny = y + dy[dir]

    return [nx, ny]

n, t = [int(num) for num in input().split()]
r, c, d = input().split()
x, y = int(r) - 1, int(c) - 1

dx = [0, 1, -1, 0]
dy = [-1, 0, 0, 1]

direction = {
    "U": 2,
    "R": 3,
    "L": 0,
    "D": 1
    }
dir = direction[d]

for _ in range(t):
    nx, ny = move(dir, x, y)

    if not in_range(nx, ny, n):
        dir = turn(dir)
    else:
        x, y = nx, ny


print(x + 1, y + 1, end=" ")