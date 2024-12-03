def drop_block(grid, n, m, k):
    y = 0
    x = k - 1
    
    for _ in range(n):
        contacted = False

        for i in range(m):
            below_space = grid[y][x + 1]
            if below_space:
                contacted = True
                break
            
            x += 1

        x = k - 1
        if contacted:
            for i in range(m):
                grid[y][x] = 1
                x += 1
            break

        y += 1


if __name__ == "__main__":
    n, m, k = tuple(map(int, input().split()))
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    drop_block(grid, n, m, k)
    for row in grid:
        print(" ".join(map(str, row)))
