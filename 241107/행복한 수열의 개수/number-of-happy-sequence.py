n, m = map(int, input().split())
grid = [[int(num) for num in input().split()] for _ in range(n)]
result = 0

for i, row in enumerate(grid):
    count = 1
    for j in range(1, n):
        if row[j] != row[j-1]:
            count = 1
            continue
        
        count += 1
    
        if count >= m:
            result += 1
            break
        
          
        
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    
    count = 1
    for i in range(1, n):
        if col[i] != col[i-1]:
            count = 1
            continue

        count += 1
        
        if count >= m:
            result += 1
            break
         
print(result)