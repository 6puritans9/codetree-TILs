def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def move(grid, n, start_y, start_x):
    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]
    y = start_y
    x = start_x
    
    trail = []
    trail.append(grid[y][x])

    while True:
        cur_value = grid[y][x]

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx
            next_value = grid[ny][nx]

            if in_range(ny, nx, n) and next_value > cur_value:
                trail.append(next_value)
                y = ny
                x = nx
                break

        if cur_value == grid[y][x]:
            break
    
    return trail

if __name__ == "__main__":
    n, r, c = tuple(map(int, input().split()))
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    trail = move(grid, n, r-1, c-1)
    print(" ".join(map(str, trail)))
