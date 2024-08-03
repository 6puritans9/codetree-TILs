def count_valid_paths(R, C, grid):
    def is_valid_jump(x1, y1, x2, y2):
        return x2 > x1 and y2 > y1 and grid[x1][y1] != grid[x2][y2]

    def dfs(x, y, jumps):
        if x == R-1 and y == C-1 and jumps == 3:
            return 1
        if jumps >= 3 or x >= R or y >= C:
            return 0
        
        count = 0
        for i in range(x+1, R):
            for j in range(y+1, C):
                if is_valid_jump(x, y, i, j):
                    count += dfs(i, j, jumps+1)
        return count

    return dfs(0, 0, 0)

R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

result = count_valid_paths(R, C, grid)
print(result)