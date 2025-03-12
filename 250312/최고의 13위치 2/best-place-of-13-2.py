def in_range(y, x, n) -> bool:
    return 0<=y<n and 0<=x<n


def visit(visited:list[list[bool]], y:int, x_start:int, x_end:int) -> None:
    visited[y][x_start] = True
    visited[y][x_start + 1] = True
    visited[y][x_end] = True


def unvisit(visited:list[list[bool]], y:int, x_start:int, x_end:int) -> None:
    visited[y][x_start] = False
    visited[y][x_start + 1] = False
    visited[y][x_end] = False


def find_max_coins(n:int, grid=[list[list[int]]]) -> int:
    # TC = O(N^4)
    # SC = O(N^2)

    visited = [[False for _ in range(n)] for _ in range(n)]
    max_coins = 0
    
    for y in range(n):
        for x in range(n-2):
            x_start, x_end = x, x+2
            
            visit(visited, y, x_start, x_end)
            coin_1 = grid[y][x_start] + grid[y][x_start + 1] + grid[y][x_end]
            
            for ny in range(y, n):
                for nx in range(n-2):
                    nx_start, nx_end = nx, nx + 2
                    if visited[ny][nx_start] or visited[ny][nx_start + 1] or visited[ny][nx_end]:
                        continue
                    
                    coin_2 = grid[ny][nx_start] + grid[ny][nx_start + 1] + grid[ny][nx_end]
                    max_coins = max(max_coins, coin_1 + coin_2)
            
            unvisit(visited, y, x_start, x_end)

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