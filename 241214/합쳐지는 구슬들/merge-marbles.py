def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def merge(grid, y, x):
    max_i = 0
    new_direction = None
    sum_weight = 0

    for bead in grid[y][x]:
        d, w, i = bead
        if i > max_i:
            max_i = i
            new_direction = d
        sum_weight += w

    new_bead = [new_direction, sum_weight, max_i]
    grid[y][x].clear()
    grid[y][x].append(new_bead)


def check_collisions(grid, positions):
    for y, x in positions:
        if len(grid[y][x]) > 1:
            merge(grid, y, x)


def turn(d):
    nxt_directions = {"L": "R", "R": "L", "U": "D", "D": "U"}
    return nxt_directions[d]


def move(grid, sub_array, y, x, n):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    bead = sub_array[0]
    d, w, i = bead

    dy, dx = directions[d]
    ny, nx = y + dy, x + dx

    if not in_range(ny, nx, n):
        bead[0] = turn(d)
        return (y, x)

    sub_array.pop()
    grid[ny][nx].append([d, w, i])
    return (ny, nx)


def operate(grid, n, positions):
    new_positions = set()
    for y, x in positions:
        sub_array = grid[y][x]
        if sub_array:
            new_position = move(grid, sub_array, y, x, n)
            new_positions.add(new_position)

    check_collisions(grid, new_positions)
    positions.clear()
    positions.extend(new_positions)


if __name__ == "__main__":
    n, m, t = tuple(map(int, input().split()))
    grid = [[[] for _ in range(n)] for _ in range(n)]
    positions = []
    for i in range(m):
        r, c, d, w = input().split()
        y, x = int(r) - 1, int(c) - 1
        bead = [d, int(w), i + 1]

        grid[y][x].append(bead)
        positions.append((y, x))

    for _ in range(t):
        operate(grid, n, positions)

    max_weight = 0
    count = 0
    for y in range(n):
        for x in range(n):
            if grid[y][x]:
                bead = grid[y][x][0]

                count += 1
                max_weight = max(max_weight, bead[1])

    print(count, max_weight, sep=" ")
