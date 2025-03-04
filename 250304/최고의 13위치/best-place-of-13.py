def in_range(start, end, n):
    return 0<=start and end<n


def find_max_coins(n:int, grid:list[int]) -> int:
    max_coins = 0

    for y in range(n):
        for x in range(n):
            start_x = x-1
            end_x = x+1

            if in_range(start_x, end_x, n):
                max_coins = max(max_coins, grid[y][start_x] + grid[y][x] + grid[y][end_x])

    return max_coins


if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    print(find_max_coins(n, grid))