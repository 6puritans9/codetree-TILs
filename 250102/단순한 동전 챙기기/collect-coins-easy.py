from itertools import permutations


def parse_grid(grid, n):
    start, end, coins = None, None, {}
    for y in range(n):
        for x in range(n):
            cell = grid[y][x]
            if cell == "S":
                start = (y, x)
            elif cell == "E":
                end = (y, x)
            elif cell.isdigit():
                coins[int(cell)] = (y, x)
    return start, end, coins


def manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def path_length(start, end, coins, order):
    path = [start] + [coins[i] for i in order] + [end]
    return sum(manhattan_dist(path[i], path[i + 1]) for i in range(len(path) - 1))


def find_min_moves(grid, n):
    start, end, coins = parse_grid(grid, n)
    if len(coins) < 3:
        return -1

    min_moves = float('inf')
    coin_numbers = sorted(coins.keys())

    for i in range(3, len(coin_numbers) + 1):
        for order in permutations(coin_numbers, i):
            moves = path_length(start, end, coins, order)
            min_moves = min(min_moves, moves)

    return min_moves if min_moves != float('inf') else -1


if __name__ == "__main__":
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    print(find_min_moves(grid, n))
