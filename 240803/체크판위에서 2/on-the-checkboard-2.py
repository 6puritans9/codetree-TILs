R, C = list(map(int, input().split()))
grid = [input().split() for _ in range(R)]

x, y = 0, 0
start_color = grid[0][0]
count = 0
if start_color != grid[-1][-1]:
    for i in range(x+1, R):
        for j in range(y+1, C):
            if grid[i][j] != start_color:
                count += 1

print(count)