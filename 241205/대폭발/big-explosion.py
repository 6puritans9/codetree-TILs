def in_range(y, x, n):
    return 0<=y<n and 0<=x<n


def plant(grid, y, x, time):
    dys = [-1, 0, 1, 0]
    dxs = [0, -1, 0, 1]

    for dy, dx in zip(dys, dxs):
        ny = y + dy * (2 ** (time - 1))
        nx = x + dx * (2 ** (time - 1))

        if in_range(ny, nx, n):
            grid[ny][nx] = 1



def play(grid_src, n, start_y, start_x, time):
    grid_copy = [row[:] for row in grid_src]

    for y in range(n):
        for x in range(n):
            if grid_src[y][x]:
                plant(grid_copy, y, x, time)

    return grid_copy


if __name__ == "__main__":
    n, m, r, c = tuple(map(int, input().split()))
    grid = [[0 for _ in range(n)] for _ in range(n)]

    y, x, = r-1, c-1
    grid[y][x] = 1

    for t in range(1, m + 1):
        grid = play(grid, n, y, x, t)

    count = sum(sum(row) for row in grid)
    print(count)
