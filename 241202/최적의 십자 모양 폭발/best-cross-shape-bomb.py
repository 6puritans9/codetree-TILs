def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def explode(grid, y, x):
    grid[y][x] = 0


def fall(grid, start_y, start_x):
    i = start_y
    while i >= 0:
        fall_target = grid[i][start_x]
        if fall_target:
            grid[start_y][start_x] = grid[i][start_x]
            grid[i][start_x] = explode(grid, i, start_x)
            break
        i -= 1


def gravity(grid, n):
    for x in range(n):
        for y in range(n-1, -1, -1):
            if not grid[y][x]:
                fall(grid, y, x)


def detonate(grid_src, start_y, start_x, n):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    grid_copy = [row[:] for row in grid_src]

    radius = grid_copy[start_y][start_x] - 1
    explode(grid_copy, start_y, start_x)
    
    for dy, dx in zip(dys, dxs):
        ny = start_y + dy
        nx = start_x + dx

        for _ in range(radius):
            if in_range(ny, nx, n):
                explode(grid_copy, ny, nx)
                ny += dy
                nx += dx
    gravity(grid_copy, n)
    
    return grid_copy


def check_count(grid, y, x, n):
    dys = [1, 0]
    dxs = [0, 1]
    count = 0

    for y in range(n):
        for x in range(n):
            cur_value = grid[y][x]
            if not cur_value:
                continue

            for dy, dx in zip(dys, dxs):
                ny = y + dy
                nx = x + dx
            
                if in_range(ny, nx, n) and grid[ny][nx] == cur_value:
                    count += 1

    return count


n = int(input())
grid = [[int(num) for num in input().split()] for _ in range(n)]

max_count = 0
for y in range(n):
    for x in range(n):
        detonated = detonate(grid, y, x, n)
        count = check_count(detonated, y, x, n)
        max_count = max(max_count, count)

print(max_count)