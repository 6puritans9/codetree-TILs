def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def gravity(grid, n):
    for col in range(n):
        remains = [row[col] for row in grid[::-1] if row[col]]
        idx = 0

        for row in range(n-1, -1, -1):
            grid[row][col] = remains[idx] if idx < len(remains) else 0
            idx += 1 


def blast(grid, n, start_y, start_x, radius):
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    grid[start_y][start_x] = 0

    for i in range(1, radius):
        y = start_y
        x = start_x
        for dy, dx in zip(dys, dxs):
            ny = y + dy * i
            nx = x + dx * i

            if in_range(ny, nx, n):
                grid[ny][nx] = 0
    

def detonate(grid, target, n):
    for y in range(n):
        if grid[y][target]:
            radius = grid[y][target]

            blast(grid, n, y, target, radius)
            gravity(grid, n)
            break
            

if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    targets = tuple(int(input()) - 1 for _ in range(m))

    for target in targets:
        detonate(grid, target, n)

    for row in grid:
        print(" ".join(map(str, row)))