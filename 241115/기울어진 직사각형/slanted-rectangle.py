def in_range(i, j, n):
    return 0<= i < n and 0<= j < n


def get_sum(y, x):
    global grid, n

    new_x = x
    new_y = y - 1
    sum = 0
    while in_range(new_x, new_y, n):
        dxs = [-1, 0]
        dys = [0, 1]

        for dx, dy in zip(dxs, dys):
            sum += grid[new_x + dx][new_y + dy]

        new_x += 1
        new_y -= 1

    return sum


n = int(input())
grid = [[int(num) for num in input().split()] for _ in range(n)]
max_sum = 0

for y in range(n):
    for x in range(n):
        max_sum = max(max_sum, get_sum(y, x))

print(max_sum)