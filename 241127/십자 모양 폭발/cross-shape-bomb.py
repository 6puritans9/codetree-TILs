def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def explode(grid, y, x):
    grid[y][x] = 0


def fall(grid, i, j, n):
    y, ny = i, i - 1
    x = j

    while in_range(ny, x, n):
        grid[y][x] = grid[ny][x]
        grid[ny][x] = 0
        y -= 1
        ny = y - 1
    
    


def detonate(grid, r, c, n):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    blast_radius = grid[r][c]
    explode(grid, r, c)

    for dy, dx in zip(dys, dxs):
        y, x = r, c

        for i in range(1, blast_radius):
            ny = y + dy
            nx = x + dx

            if in_range(ny, nx, n):
                explode(grid, ny, nx)
                y = ny
                x = nx


def aftershock(grid, n):
    for y in range(n):
        for x in range(n):
            if not grid[y][x]:
                fall(grid, y, x, n)


if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    r, c = tuple(map(int, input().split()))

    detonate(grid, r - 1, c - 1, n)
    aftershock(grid, n)
    for row in grid:
        print(" ".join(map(str, row)))