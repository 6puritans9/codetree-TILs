def drop_block(grid, n, m, k):
    for y in range(n):
        contacted = False

        for x in range(k - 1, k + m - 1):
            if y < n - 1:
                below_space = grid[y + 1][x]
                if below_space:
                    contacted = True
                    break
            else:
                for x in range(k - 1, k + m - 1):
                    grid[y][x] = 1

        if contacted:
            for x in range(k - 1, k + m - 1):
                grid[y][x] = 1
            break


if __name__ == "__main__":
    n, m, k = tuple(map(int, input().split()))
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    drop_block(grid, n, m, k)

    for row in grid:
        print(" ".join(map(str, row)))
