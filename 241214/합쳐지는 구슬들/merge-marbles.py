def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def merge(grid, y, x):
    max_number = 0
    new_direction = None
    total_weight = 0

    for bead in grid[y][x]:
        d, w, num = bead
        total_weight += w
        if num > max_number:
            max_number = num
            new_direction = d

    grid[y][x] = [[new_direction, total_weight, max_number]]


def move(grid, n, y, x):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
    bead = grid[y][x][0]
    d, w, num = bead
    dy, dx = directions[d]

    ny, nx = y + dy, x + dx

    if not in_range(ny, nx, n):
        reverse_dir = {"L": "R", "R": "L", "U": "D", "D": "U"}
        bead[0] = reverse_dir[d]
        return y, x 

    grid[y][x].pop()
    grid[ny][nx].append([d, w, num])
    return ny, nx


def operate(grid, n, positions):
    new_positions = set()

    for y, x in positions:
        if grid[y][x]:
            new_position = move(grid, n, y, x)
            new_positions.add(new_position)

    for y, x in new_positions:
        if len(grid[y][x]) > 1:
            merge(grid, y, x)

    positions.clear()
    positions.extend(new_positions)


if __name__ == "__main__":
    n, m, t = map(int, input().split())
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

    print(count, max_weight)
