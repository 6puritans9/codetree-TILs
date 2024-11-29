def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def gravity(grid, y, x, values):
    pass


def merge(grid, y, x, ny, nx):
    if grid[ny][nx] == grid[y][x]:
        grid[ny][nx] *= 2
        grid[y][x] = 0


def operate(grid, n, direction, d):
    dy, dx = direction

    if d == "R":
        for y in range(n):
            for x in range(n - 1, -1, -1):
                ny = y + dy
                nx = x + dx

                if in_range(ny, nx, n):
                    merge(grid, y, x, ny, nx)

        for y in range(n):
            valid_values = [num for num in grid[y] if num]
            i = len(valid_values) - 1

            for x in range(n-1, -1, -1):
                if i >= 0:
                    grid[y][x] = valid_values[i]
                    i -= 1
                else:
                    grid[y][x] = 0

    elif d == "L":
        for y in range(n):
            for x in range(n):
                ny = y + dy
                nx = x + dx
                if in_range(ny, nx, n):
                    merge(grid, y, x, ny, nx)

        for y in range(n):
            valid_values = [num for num in grid[y] if num]
            i = 0

            for x in range(n):
                if i < len(valid_values):
                    grid[y][x] = valid_values[i]
                    i += 1
                else:
                    grid[y][x] = 0

    elif d == "U":
        for x in range(n):
            for y in range(n):
                ny = y + dy
                nx = x + dx
                if in_range(ny, nx, n):
                    merge(grid, y, x, ny, nx)

        for x in range(n):
            valid_values = [grid[y][x] for y in range(n) if grid[y][x]]
            i = 0

            for y in range(n):
                if i < len(valid_values):
                    grid[y][x] = valid_values[i]
                    i += 1
                else:
                    grid[y][x] = 0

    else:
        for x in range(n):
            for y in range(n - 1, -1, -1):
                ny = y + dy
                nx = x + dx
                if in_range(ny, nx, n):
                    merge(grid, y, x, ny, nx)

        for x in range(n):
            valid_values = [grid[y][x] for y in range(n-1, -1, -1) if grid[y][x]]
            i = len(valid_values) - 1

            for y in range(n - 1, -1, -1):
                if i >= 0:
                    grid[y][x] = valid_values[i]
                    i -= 1
                else:
                    grid[y][x] = 0


if __name__ == "__main__":
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    grid = [[int(num) for num in input().split()] for _ in range(4)]
    n = 4
    d = input()
    direction = directions[d]

    operate(grid, n, direction, d)

    for row in grid:
        print(" ".join(map(str, row)))