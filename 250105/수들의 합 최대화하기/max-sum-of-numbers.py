def get_max_sum(grid, n, row, visited, max_sum, cur_sum, cnt):
    if cnt == n:
        max_sum[0] = max(max_sum[0], cur_sum)
        return
    
    for col in range(n):
        if not visited[col]:
            visited[col] = True
            get_max_sum(grid, n, row + 1, visited, max_sum, cur_sum + grid[row][col], cnt + 1)
            visited[col] = False
        

if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    visited = [False] * n
    max_sum = [0]
            
    get_max_sum(grid, n, 0, visited, max_sum, 0, 0)
    print(max_sum[0])