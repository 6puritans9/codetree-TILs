from collections import deque


def in_range(y, x, n):
    return 0<=y<n and 0<=x<n


def is_valid_to_go(grid, n, visited, y, x):
    return in_range(y,x,n) and not grid[y][x] and not visited[y][x]


def bfs(grid, n, visited, y, x):
    dys = [-1,0,1,0]
    dxs = [0,1,0,-1]
    
    queue = deque([(y,x)])
    count = 0

    while queue:
        cy, cx = queue.popleft()
        if not is_valid_to_go(grid, n, visited, cy, cx):
            continue
        visited[cy][cx] = True
        count += 1

        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            queue.append((ny,nx))

    return count


def count_tiles(grid, n, points):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    
    for r, c in points:
        count += bfs(grid, n, visited, r-1, c-1)

    return count


if __name__ == "__main__":
    n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    points = [tuple(map(int, input().split())) for _ in range(k)]

    print(count_tiles(grid, n, points))
    