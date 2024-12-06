from collections import deque


class Snake():
    def __init__(self):
        self.positions = deque([(0, 0)])
        self.length = 1
        self.head = self.positions[0]

    def extend(self, grid, y, x):
        grid[y][x] = 0
        self.length += 1

    def shrink(self):
        self.positions.pop()

    def move(self, grid, y, x):
        self.positions.appendleft((y, x))

        if grid[y][x]:
            self.extend(grid, y, x)
        else:
            self.shrink()

        self.head = self.positions[0]


def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def is_overlapped(snake):
    return snake.positions.count(snake.head) > 1


def play(grid, n, snake, direction, distance, count):
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    for _ in range(distance):
        dy, dx = directions[direction]
        y, x = snake.head
        ny, nx = y + dy, x + dx

        if not in_range(ny, nx, n):
            count[0] += 1
            return True

        snake.move(grid, ny, nx)
        if is_overlapped(snake):
            count[0] += 1
            return True

        count[0] += 1

    return False


if __name__ == "__main__":
    n, m, k = tuple(map(int, input().split()))
    info_apple = []
    info_snake = []

    for _ in range(m):
        _input = input().split()
        info_apple.append((int(_input[0]), int(_input[1])))

    for _ in range(k):
        _input = input().split()
        info_snake.append((_input[0], int(_input[1])))

    grid = [[0 for _ in range(n)] for _ in range(n)]
    for info in info_apple:
        y, x = info
        grid[y - 1][x - 1] = 1

    snake = Snake()
    count = [0]
    is_game_over = False
    for info in info_snake:
        direction, distance = info
        is_game_over = play(grid, n, snake, direction, distance, count)
        if is_game_over:
            break

    print(count[0])
