def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def backtrack(grid, n, y, x, count):
    global max_count, directions, arrows

    dy, dx = arrows[directions[y][x]]

    for i in range(n):
        ny, nx = y + dy * i, x + dx * i

        if in_range(ny, nx, n) and grid[ny][nx] > grid[y][x]:
            max_count = max(max_count, count + 1)
            backtrack(grid, n, ny, nx, count + 1)


if __name__ == "__main__":
    arrows = [None, (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    directions = [[int(num) for num in input().split()] for _ in range(n)]
    r, c = tuple(map(int, input().split()))

    max_count = 0
    backtrack(grid, n, r - 1, c - 1, 0)
    print(max_count)
