from collections import deque


def in_range(y, x):
    global n, m

    return 0 <= y < n and 0 <= x < m


def fill(grid, result, start_y, start_x, end_y, end_x):
    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            grid[y][x] = result.popleft()


def rotate(grid, start_y, start_x, end_y, end_x):
    new_order = deque([0])

    for i in range(start_x, end_x):
        new_order.append(grid[start_y][i])
    for j in range(start_y, end_y):
        new_order.append(grid[j][end_x])
    for k in range(end_x, 0, -1):
        new_order.append(grid[end_y][k])
    for l in range(end_y - 1, start_y + 1, -1):
        new_order.append(grid[l][start_x])
    new_order[0] = grid[start_y + 1][start_x]

    for i in range(start_x, end_x):
        grid[start_y][i] = new_order.popleft()
    for j in range(start_y, end_y):
        grid[j][end_x] = new_order.popleft()
    for k in range(end_x, 0, -1):
        grid[end_y][k] = new_order.popleft()
    for l in range(end_y - 1, start_y, -1):
        grid[l][start_x] = new_order.popleft()


def mutate(grid, start_y, start_x, end_y, end_x):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    
    result = deque()

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            _sum = grid[y][x]
            count = 1

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx):
                    _sum += grid[ny][nx]
                    count += 1
            
            avg = _sum // count
            result.append(avg)

    fill(grid, result, start_y, start_x, end_y, end_x)


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    winds = []
    for _ in range(q):
        r1, c1, r2, c2 = input().split()
        winds.append((int(r1), int(c1), int(r2), int(c2)))

    for start_y, start_x, end_y, end_x in winds:
        rotate(grid, start_y - 1, start_x - 1, end_y - 1, end_x - 1)
        mutate(grid, start_y - 1, start_x - 1, end_y, end_x)

    for row in grid:
        for col in row:
            print(col, end=" ")
        print()
