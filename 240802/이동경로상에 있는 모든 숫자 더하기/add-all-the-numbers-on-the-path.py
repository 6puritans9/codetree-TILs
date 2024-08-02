def in_range(x, y, n):
    return 0<= x < n and 0<= y < n


def turn(dir, instruction):
    ndir = None
    if instruction == "R":
        ndir = (dir + 1) % 4
    else:
        ndir = (dir - 1) % 4

    return ndir


def move(x, y, dir):
    nx = x + dxs[dir]
    ny = y + dys[dir]

    return [nx, ny]


N, T = [int(num) for num in input().split()]
instructions = input()
grid = []
for _ in range(N):
    grid.append([int(num) for num in input().split()])

x, y = N // 2, N // 2
dir = 1

dxs = [0,-1,0,1]
dys = [-1,0,1,0]

sum = grid[x][y]
for instruction in instructions:
    nx, ny = None, None
    ndir = None

    if instruction == "F":
        nx, ny = move(x, y, dir)

        if in_range(nx, ny, N):
            sum += grid[nx][ny]
            x, y = nx, ny
    else:
        dir = turn(dir, instruction)

print(sum)