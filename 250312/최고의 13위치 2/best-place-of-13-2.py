from itertools import combinations


def find_max_coins(n:int, grid=[list[list[int]]]) -> int:
    # A little optimization with early pruning
    # TC = O(N^4 + (N^2 * logN))
    # SC = O(N^2)

    sub_grids = []
    max_coins = 0

    for y in range(n):
        for x in range(n-2):
            sum_coins = grid[y][x] + grid[y][x+1] + grid[y][x+2]

            sub_grids.append((sum_coins, y, x, x+2))
    
    # Sort by sum_coins in descending order
    sub_grids.sort(key=lambda x:x[0], reverse=True)

    for sub_grid_1, sub_grid_2 in combinations(sub_grids, 2):
        coin_1, y1, x1_start, x1_end = sub_grid_1
        coin_2, y2, x2_start, x2_end = sub_grid_2
        if coin_1 + coin_2 <= max_coins:
            break # Early pruning
        
        if y1 == y2 and (x1_end <= x2_start or x2_end <= x1_start):
            continue
        
        max_coins = max(max_coins, coin_1 + coin_2)

    return max_coins


if __name__ =="__main__":
    # In N^2 sized grid, digits are given which indicates if there's coin
    # By selecting 2 sub-grid, which is 1*3 size,
    # find the maximum coins that can be included
    
    # 1. Overlapping check needed
    # As the given conditions are N<=20, time limit 5s,
    # Two pairs of nested loops would fit(O(N^4))

    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    print(find_max_coins(n, grid))