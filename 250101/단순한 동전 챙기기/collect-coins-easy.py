from itertools import permutations
from collections import deque


def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def bfs(grid, n, start):
    queue = deque([(*start, 0)])
    distances = [[float("inf")] * n for _ in range(n)]
    distances[start[0]][start[1]] = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        y, x, dist = queue.popleft()
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if in_range(ny, nx, n) and grid[ny][nx] != "#" and distances[ny][nx] > dist + 1:
                distances[ny][nx] = dist + 1
                queue.append((ny, nx, dist + 1))

    return distances


def find_points(grid, n):
    start, end = None, None
    coins = []
    for y in range(n):
        for x in range(n):
            if grid[y][x] == "S":
                start = (y, x)
            elif grid[y][x] == "E":
                end = (y, x)
            elif grid[y][x].isdigit():
                coins.append((int(grid[y][x]), y, x))
    coins.sort()
    return start, end, coins


def solve(grid, n):
    start, end, coins = find_points(grid, n)
    if len(coins) < 3:
        return -1

    key_points = [(0, *start)] + coins + [(float("inf"), *end)]
    distances = {}
    for i, (_, y1, x1) in enumerate(key_points):
        dist = bfs(grid, n, (y1, x1))
        distances[i] = {j: dist[y2][x2] for j, (_, y2, x2) in enumerate(key_points)}

    min_moves = float("inf")
    num_coins = len(coins)
    for num in range(3, num_coins + 1):
        for combo in permutations(range(1, num_coins + 1), num):
            if any(coins[combo[i] - 1][0] >= coins[combo[i + 1] - 1][0] for i in range(len(combo) - 1)):
                continue

            path = [0] + list(combo) + [num_coins + 1]
            total_distance = sum(distances[path[i]][path[i + 1]] for i in range(len(path) - 1))

            if all(distances[path[i]][path[i + 1]] < float("inf") for i in range(len(path) - 1)):
                min_moves = min(min_moves, total_distance)

    return min_moves if min_moves < float("inf") else -1


if __name__ == "__main__":
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    print(solve(grid, n))
