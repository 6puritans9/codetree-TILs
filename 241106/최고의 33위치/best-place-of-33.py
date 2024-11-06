def is_range(x, y, n):
    global SUB_GRID

    return x + SUB_GRID <= n and y + SUB_GRID <= n


N= int(input())
grid = [[int(num) for num in input().split()] for _ in range(N)]
SUB_GRID = 3

max_coins = 0
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if not is_range(i, j, N):
            continue

        cur_coins = 0
        for i2 in range(0, SUB_GRID):
            for j2 in range(0, SUB_GRID):
                cur_coins += grid[i + i2][j + j2]
        
        max_coins = max(cur_coins, max_coins)

print(max_coins)