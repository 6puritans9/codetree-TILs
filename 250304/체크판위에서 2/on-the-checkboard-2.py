def find_paths(r:int, c:int, grid:list[list[str]]) -> int:
    paths = 0
    
    for y in range(1, r):
        for x in range(1, c):
            for ny in range(y+1, r-1):
                for nx in range(x+1, c-1):
                    if grid[0][0] != grid[y][x] and grid[y][x] != grid[ny][nx] and grid[r-1][c-1] != grid[ny][nx]:
                        paths += 1

    return paths


if __name__ == "__main__":
    r, c = map(int, input().split())
    grid = [[char for char in input().split()] for _ in range(r)]

    print(find_paths(r, c, grid))