def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def is_wall(maze, y, x):
    return maze[y][x] == "#"


def turn(cur_idx, clockwise):
    return (cur_idx - 1) % 4 if clockwise else (cur_idx + 1) % 4


def should_turn(cur_y, cur_x, dir_idx, maze, n):
    dy, dx = None, None

    if dir_idx == 0:
        dy, dx = cur_y + 1, cur_x
    elif dir_idx == 1:
        dy, dx = cur_y, cur_x + 1
    elif dir_idx == 2:
        dy, dx = cur_y - 1, cur_x
    else:
        dy, dx = cur_y, cur_x - 1

    if in_range(dy, dx, n):
        return is_wall(maze, dy, dx)
    return False


def forward(y, x, direction):
    dir_y, dir_x = direction

    return [y + dir_y, x + dir_x]


def escape(maze, n, start_y, start_x):
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    i = 0
    count = 0

    y, x = start_y, start_x
    # visited[y][x] = 1
    while True:
        direction = directions[i]
        ny, nx = forward(y, x, direction)

        if not in_range(ny, nx, n):
            count += 1
            return count

        else:
            # if visited[ny][nx]:
            #     break
            if count > 9999:
                break

            if is_wall(maze, ny, nx):
                i = turn(i, 0)
                continue

            elif should_turn(y, x, i, maze, n):
                i = turn(i, 1)

        # visited[ny][nx] = 1
        y, x = ny, nx
        count += 1

    return -1


n = int(input())
y, x = tuple(map(int, input().split()))
maze = [[char for char in input()] for _ in range(n)]
# visited = [[0 for _ in range(n)] for _ in range(n)]

count = escape(maze, n, y - 1, x - 1)
print(count)
