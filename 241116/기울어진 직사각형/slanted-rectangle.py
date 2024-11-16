def in_range(x, y):
    global n

    return 0 <= x < n and 0 <= y < n


def get_part_sum(y, x, y_limit, x_limit):
    global grid

    dys = [-1, -1, 1, 1]
    dxs = [1, -1, -1, 1]
    shifts = [y_limit, x_limit, y_limit, x_limit]

    part_sum = 0
    ny, nx = y, x

    for dy, dx, shift in zip(dys, dxs, shifts):
        for _ in range(shift):
            ny += dy
            nx += dx
            if not in_range(nx, ny):
                return 0

            part_sum += grid[ny][nx]

    return part_sum


n = int(input())
grid = [[int(num) for num in input().split()] for _ in range(n)]
max_sum = 0

for y in range(n):
    for x in range(n):
        for y_limit in range(1, n):
            for x_limit in range(1, n):
                max_sum = max(max_sum, get_part_sum(y, x, y_limit, x_limit))

print(max_sum)
