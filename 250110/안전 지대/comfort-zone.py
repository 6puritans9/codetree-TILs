def in_range(y, x, n, m):
    return 0<=y<n and 0<=x<m


def flood(grid, n, m, k):
    did_flood = False

    for y in range(n):
        for x in range(m):
            if grid[y][x] <= k:
                grid[y][x] = 0
                did_flood = True

    return did_flood


def count_dfs(grid, n, m, k):
    dys = [-1,0,1,0]
    dxs = [0,1,0,-1]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    stack = []
    cur_count = 0

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and grid[y][x]:
                stack.append((y, x))
                cur_count += 1
            while stack:
                y, x = stack.pop()
                visited[y][x] = True

                for dy, dx in zip(dys, dxs):
                    ny, nx = y + dy, x + dx
                    if in_range(ny, nx, n, m):
                        if grid[ny][nx] and not visited[ny][nx]:
                            stack.append((ny, nx))
    
    return [cur_count, k]
                
    
def count_zones(grid, n, m):
    max_count = 0
    max_k = 0

    for k in range(1, 101):
        flooded = flood(grid, n, m, k)
        if not flooded:
            break

        cur_count, cur_k = count_dfs(grid, n, m, k)
        if cur_count > max_count:
            max_count = cur_count
            max_k = cur_k

    return [max_count, max_k]
    

if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(" ".join(map(str, count_zones(grid, n, m))))