def find_paths(r:int, c:int, grid:list[list[str]]) -> int:
    dp = [[[0 for _ in range(3)]for _ in range(c)] for _ in range(r)]
    dp[0][0][0] = 1
    
    for y in range(r):
        for x in range(c):
            for step in range(3):
                if dp[y][x][step] == 0:
                    continue

                for ny in range(y+1, r):
                    for nx in range(x+1, c):
                        if grid[y][x] != grid[ny][nx]:
                            new_step = step + 1

                            if new_step < 3:
                                dp[ny][nx][new_step] = max(dp[ny][nx][step], dp[y][x][step] + 1)

    return max(dp[r-1][c-1])

if __name__ == "__main__":
    r, c = map(int, input().split())
    grid = [[char for char in input().split()] for _ in range(r)]

    print(find_paths(r, c, grid))