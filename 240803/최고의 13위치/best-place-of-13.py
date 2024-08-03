N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

max_value = 0
for row_idx in range(N):
    for col_idx in range(N-2):
        sum = grid[row_idx][col_idx] + grid[row_idx][col_idx + 1] + grid[row_idx][col_idx + 2]

        max_value = max(max_value, sum)

print(max_value)