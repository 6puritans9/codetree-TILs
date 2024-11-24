from collections import deque


def in_range(y, x, n, m):
    return 0 <= y < n and 0 <= x < m


def fill(grid, result, start_y, start_x, end_y, end_x):
    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            grid[y][x] = result.popleft()


def rotate(grid, start_y, start_x, end_y, end_x):
    new_order = deque()
    
    for i in range(start_x, end_x + 1):
        new_order.append(grid[start_y][i])
    
    for j in range(start_y + 1, end_y + 1):
        new_order.append(grid[j][end_x])
    
    for i in range(end_x - 1, start_x - 1, -1):
        new_order.append(grid[end_y][i])
    
    for j in range(end_y - 1, start_y, -1):
        new_order.append(grid[j][start_x])
    
    new_order.rotate(1)
    
    idx = 0
    for i in range(start_x, end_x + 1):
        grid[start_y][i] = new_order[idx]
        idx += 1
    for j in range(start_y + 1, end_y + 1):
        grid[j][end_x] = new_order[idx]
        idx += 1
    for i in range(end_x - 1, start_x - 1, -1):
        grid[end_y][i] = new_order[idx]
        idx += 1
    for j in range(end_y - 1, start_y, -1):
        grid[j][start_x] = new_order[idx]
        idx += 1


def mutate(grid, start_y, start_x, end_y, end_x, n, m):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]

    result = deque()

    for y in range(start_y, end_y + 1):
        for x in range(start_x, end_x + 1):
            _sum = grid[y][x]
            count = 1

            for dy, dx in zip(dys, dxs):
                ny, nx = y + dy, x + dx

                if in_range(ny, nx, n, m):
                    _sum += grid[ny][nx]
                    count += 1

            avg = _sum // count
            result.append(avg)

    fill(grid, result, start_y, start_x, end_y, end_x)


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    
    for _ in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        start_y, start_x, end_y, end_x = r1 - 1, c1 - 1, r2 - 1, c2 - 1

        rotate(grid, start_y, start_x, end_y, end_x)
        mutate(grid, start_y, start_x, end_y, end_x, n, m)

    for row in grid:
        print(" ".join(map(str, row)))
