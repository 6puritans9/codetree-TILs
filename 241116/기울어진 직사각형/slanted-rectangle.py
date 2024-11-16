def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


def get_rectangle_sum(x, y):
    global grid, n

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]
    rectangle_sum = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny, n):
            return 0

        rectangle_sum += grid[ny][nx]

    return rectangle_sum



def get_part_sum(x, y):
    part_sum = get_rectangle_sum(x, y)
    nx, ny = x + 1, y - 1

    while in_range(nx, ny, n):
        rectangle_sum = get_rectangle_sum(nx, ny)
        if not rectangle_sum:
            break
        
        part_sum += rectangle_sum
        part_sum -= grid[ny][nx - 1] + grid[ny + 1][nx]  # remove duplicates

        nx, ny = nx + 1, ny - 1

    return part_sum


n = int(input())
grid = [[int(num) for num in input().split()] for _ in range(n)]
max_sum = 0

for y in range(n):
    for x in range(n):
        max_sum = max(max_sum, get_part_sum(x, y))

print(max_sum)
