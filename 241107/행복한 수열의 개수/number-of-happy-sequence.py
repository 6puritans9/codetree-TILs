n, m = map(int, input().split())
grid = [[int(num) for num in input().split()] for _ in range(n)]
result = 0

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if j <= n - m:
            sub_grid = row[j:j+m]

            count = 1
            for k in range(1, len(sub_grid)):
                if sub_grid[k] == sub_grid[k - 1]:
                    count += 1
                else:
                    count = 0
                
            if count >= m:
                result += 1

        
        
for j in range(n):
    for i in range(n):
        col = [grid[i][j] for i in range(n)]
        
        if i <= n-m:
            sub_grid = col[j:j+m]

            count = 1
            for k in range(1, len(sub_grid)):
                if sub_grid[k] == sub_grid[k - 1]:
                    count += 1
                else:
                    count = 0
            
            if count >= m:
                result += 1
                break

print(result)