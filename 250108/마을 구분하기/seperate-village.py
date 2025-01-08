def in_range(y, x, n):
    return 0<=y<n and 0<=x<n


def backtrack(grid, n, visited, pops, y, x):
    if not in_range(y, x, n) or visited[y][x] or not grid[y][x]:
        return 0
    
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    visited[y][x] = True
    cur_pop = grid[y][x]

    for dy, dx in zip(dys, dxs):
        cur_pop += backtrack(grid, n, visited, pops, y + dy, x + dx)

    return cur_pop


def get_villages_and_pops(grid, n):
    pops = []
    visited = [[False for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if not visited[y][x] and grid[y][x] > 0:
                pops.append(backtrack(grid, n, visited, pops, y, x))

    pops.sort()
    return [len(pops)] + pops


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    result = get_villages_and_pops(grid, n)
    for element in result:
        print(element)
