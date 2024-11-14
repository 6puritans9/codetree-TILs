def in_range(i, j, n):
    return 0 <= i < n and 0 <= j < n


def dig(visited, i, j, move_count):
    global grid, n, k

    if not in_range(i,j,n) or visited[i][j] or move_count > k:
        return 0
    
    gold_count = grid[i][j]
    visited[i][j] = 1

    gold_count += dig(visited, i + 1, j, move_count + 1)
    gold_count += dig(visited, i, j + 1, move_count + 1)
    gold_count += dig(visited, i - 1, j, move_count + 1)
    gold_count += dig(visited, i, j - 1, move_count + 1)
        
    return gold_count


n, m = map(int, input().split())
grid = [[int(num) for num in input().split()] for _ in range(n)]
max_gold_count = 0

k = 0
while k < 2*(n-1):
    dig_cost = k**2 + (k+1)**2
    
    for i in range(n):
        for j in range(n):
            visited = [[0 for _ in range(n)] for _ in range(n)]
            gold_count = dig(visited, i, j, 0)

            if m * gold_count >= dig_cost:
                max_gold_count = max(max_gold_count, gold_count)

    k+= 1

print(max_gold_count)