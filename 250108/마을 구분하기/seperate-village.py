def in_range(y, x, n):
    return 0<=y<n and 0<=x<n


def backtrack(grid, n, visited, pops, cur_pop, is_start, y, x):
    if not cur_pop or visited[y][x]:
        return 0
    
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    visited[y][x] = True

    for dy, dx in zip(dys, dxs):
        ny, nx = y + dy, x + dx

        if in_range(ny, nx, n):
            cur_pop += backtrack(grid, n, visited, pops, grid[ny][nx], False, ny, nx)

    if is_start:
        pops.append(cur_pop)

    return cur_pop


def get_villages_and_pops(grid, n):
    pops = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            backtrack(grid, n, visited, pops, grid[y][x], True, y, x)

    pops.sort()
    return [len(pops)] + pops


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    result = get_villages_and_pops(grid, n)
    for element in result:
        print(element)
