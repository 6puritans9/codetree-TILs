def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def tile1(y, x, ins_dir):
    deflections = {"L": "D", "R": "U", "U": "R", "D": "L"}
    nxt_dir = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}

    deflection = deflections[ins_dir]
    dy, dx = nxt_dir[ins_dir]
    ny, nx = y + dy, x + dx

    return (ny, nx, deflection)


def tile2(y, x, ins_dir):
    deflections = {"L": "U", "R": "D", "U": "L", "D": "R"}
    nxt_dir = {"L": (1, 0), "R": (-1, 0), "U": (0, 1), "D": (-1, 0)}

    deflection = deflections[ins_dir]
    dy, dx = nxt_dir[ins_dir]
    ny, nx = y + dy, x + dx

    return (ny, nx, deflection)


def play(grid, n, start_y, start_x, ins_dir):
    nxt_dir = {"L": (0, 1), "R": (0, -1), "U": (1, 0), "D": (-1, 0)}

    _dir = ins_dir
    dy, dx = nxt_dir[ins_dir]
    y, x = start_y + dy, start_x + dx
    ny, nx = y, x
    count = 1

    while in_range(ny, nx, n):
        cur_tile = grid[y][x]

        if cur_tile:
            if cur_tile == 1:
                ny, nx, _dir = tile1(y, x, _dir)
            else:
                ny, nx, _dir = tile2(y, x, _dir)
        else:
            dy, dx = nxt_dir[_dir]
            ny, nx = y + dy, x + dx

        if not in_range(ny, nx, n):
            break
        count += 1
        y, x = ny, nx

    return count + 1


if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    max_count = 0

    for y in range(n):
        max_count = max(max_count, play(grid, n, y, -1, "L"))

    for y in range(n):
        max_count = max(max_count, play(grid, n, y, n, "R"))

    for x in range(n):
        max_count = max(max_count, play(grid, n, -1, x, "U"))

    for x in range(n):
        max_count = max(max_count, play(grid, n, n, x, "D"))

    print(max_count)
    