def in_range(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def flood(grid, n, m, k):
    grid = [row[:] for row in grid]  # Make a copy
    did_flood = False
    cur_sum = 0

    for y in range(n):
        for x in range(m):
            if grid[y][x] <= k:
                grid[y][x] = 0
                did_flood = True
            cur_sum += grid[y][x]

    return [did_flood, cur_sum, grid]


def count_dfs(grid, n, m, k):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    visited = [[False for _ in range(m)] for _ in range(n)]
    stack = []
    cur_count = 0

    for y in range(n):
        for x in range(m):
            if not visited[y][x] and grid[y][x]:
                stack.append((y, x))
                cur_count += 1

                while stack:
                    cy, cx = stack.pop()
                    if visited[cy][cx]:
                        continue
                    visited[cy][cx] = True

                    for dy, dx in zip(dys, dxs):
                        ny, nx = cy + dy, cx + dx
                        if in_range(ny, nx, n, m):
                            if grid[ny][nx] and not visited[ny][nx]:
                                stack.append((ny, nx))

    return [cur_count, k]


def count_zones(grid, n, m):
    max_k = 1
    max_count = 0

    for k in range(1, 101):
        flooded, sum_grid, curr_grid = flood(grid, n, m, k)
        if not flooded and not sum_grid:
            break

        cur_count, cur_k = count_dfs(curr_grid, n, m, k)
        if cur_count > max_count:
            max_count = cur_count
            max_k = cur_k

    return [max_k, max_count]


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(" ".join(map(str, count_zones(grid, n, m))))