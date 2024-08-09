def in_range(x, y, row, col):
    return 0 <= x < row and 0 <= y < col


def is_E(dir, x, y, row, col, count):
    if count == 2:
        return in_range(x, y, row, col) and grid[x][y] == "E"

    mx = x + dx[dir]
    my = y + dy[dir]

    return in_range(x, y, row, col) and grid[x][y] == "E" and is_E(dir, mx, my, row, col, count + 1)

            
def is_L(row, col):
    return grid[row][col] == "L"


N, M = list(map(int, input().split()))
grid = [list(row) for row in [input() for _ in range(N)]]

# Starts from North
dx = [-1, -1, 0, 1, 1, 1, 0, -1] 
dy = [0, 1, 1, 1, 0, -1, -1, -1]

count = 0
for row in range(N):
    for col in range(M):
        if not is_L(row, col):
            continue
        
        for dir in range(8):
            nx = row + dx[dir]
            ny = col + dy[dir]

            if is_E(dir, nx, ny, N, M, 1):
                count += 1

print(count)