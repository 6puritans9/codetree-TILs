from collections import deque


def in_range(y, x, n, m):
    return 0<=y<n and 0<=x<m


def is_valid(grid, visited, y, x, n, m):
    if not in_range(y,x,n,m) or visited[y][x] or not grid[y][x]:
        return False
    return True


def bfs(grid, n, m, y, x):
    dys = [-1,0,1,0]
    dxs = [0,1,0,-1]

    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque([(y, x)])
    
    while queue:
        cy, cx = queue.popleft()
        if visited[cy][cx]:
            continue
        if cy == n-1 and cx == m-1:
            return True
        visited[cy][cx] = True

        for dy, dx in zip(dys, dxs):
            ny, nx = cy+dy, cx+dx
            if is_valid(grid, visited, ny, nx, n, m):
                queue.append((ny, nx))

    return False

def find_exit(grid, n, m):
    return bfs(grid, n, m, 0, 0)


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    exit = find_exit(grid, n, m)
    print(1 if exit else 0)