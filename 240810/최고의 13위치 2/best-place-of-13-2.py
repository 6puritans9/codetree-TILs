def count(x, y):
    return sum(grid[x][y:y+3])

def find_max_coins(N, grid):
    # Get the precomputation
    coin_counts = [[0] * (N-2) for _ in range(N)]
    for i in range(N):
        for j in range(N - 2):
            coin_counts[i][j] = count(i, j)

    # Do the actual exhaustive search
    max_coins = 0

    for i1 in range(N):
        for j1 in range(N - 2):
            for i2 in range(N):
                if i1 == i2:
                    for j2 in range(N-2):
                        if not j2+ 3 <= j1 or not j1 + 3 <= j2:
                            continue
                        
                        max_coins = max(max_coins, coin_counts[i1][j1] + count(i2, j2))
                else:
                    for j2 in range(N-2):
                        max_coins = max(max_coins, coin_counts[i1][j1] + count(i2, j2))
    
    return max_coins
    

N= int(input())
grid = [[int(num) for num in input().split()] for _ in range(N)]

print(find_max_coins(N, grid))