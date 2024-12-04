def in_range(y, x, n):
    return 0<=y<n and 0<=x<n

def is_wall(maze, y, x):
    return maze[y][x] == "#"


def turn(cur_idx):
    return (cur_idx + 1) % 4


def forward(y, x, direction):
    dir_y, dir_x = direction
    
    return [y + dir_y, x + dir_x]


def escape(maze, n, start_y, start_x, visited):
    directions = [(0, 1), (-1, 0), (0,-1), (1, 0)]
    i = 0
    count = 0

    y, x = start_y, start_x    
    visited[y][x] = 1
    while True:
        direction = directions[i]
        ny, nx = forward(y, x, direction)
        

        if not in_range(ny, nx, n):
            count += 1
            return count
        
        elif is_wall(maze, ny, nx):
            i = turn(i)
            continue

        elif visited[ny][nx]:
            break

        visited[ny][nx] = 1
        y, x = ny, nx
        count += 1

    return -1


n = int(input())
x, y = tuple(map(int, input().split()))
maze = [[char for char in input()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

count = escape(maze, n, y-1, x-1, visited)
print(count)
