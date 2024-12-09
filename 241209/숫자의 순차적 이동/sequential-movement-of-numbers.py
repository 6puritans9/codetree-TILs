def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def shift(grid, n, cur_num):
    y, x = None, None

    for i in range(n):
        is_identical = False

        for j in range(n):
            if grid[i][j] == cur_num:
                y, x = i, j
                is_identical = True
                break

        if is_identical:
            break

    dys = [-1, -1, -1, 0, 1, 1, 1, 0]
    dxs = [-1, 0, 1, 1, 1, 0, -1, -1]

    biggest_num = 0
    i, j = None, None

    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx

        if in_range(ny, nx, n) and grid[ny][nx] > biggest_num:
            i, j = ny, nx
            biggest_num = grid[ny][nx]

    grid[i][j] = cur_num
    grid[y][x] = biggest_num


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    for _ in range(m):
        for i in range(1, n*n + 1):
            shift(grid, n, i)

    for row in grid:
        print(" ".join(map(str, row)))