def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def dfs(grid, n, visited, y, x):
    dys = [0, 1]
    dxs = [1, 0]

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx
        
        if ny == n - 1 and nx == n - 1:
            return True

        if in_range(ny, nx, n) and grid[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = True
            if dfs(grid, n, visited, ny, nx):
                return True
    
    return False


def find_exit(grid, n, m):
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    is_escapable = dfs(grid, n, visited, 0, 0)
    return 1 if is_escapable else 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(find_exit(grid, n, m))
