def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def dfs(grid, visited, y, x, n):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    stack = [(y, x)]
    population = 0

    while stack:
        cur_y, cur_x = stack.pop()
        if visited[cur_y][cur_x]:
            continue

        visited[cur_y][cur_x] = True
        population += grid[cur_y][cur_x]

        for dy, dx in directions:
            new_y, new_x = cur_y + dy, cur_x + dx
            if in_range(new_y, new_x, n) and not visited[new_y][new_x] and grid[new_y][new_x] > 0:
                stack.append((new_y, new_x))

    return population


def get_villages_and_pops(grid, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    populations = []

    for y in range(n):
        for x in range(n):
            if not visited[y][x] and grid[y][x] > 0:
                populations.append(dfs(grid, visited, y, x, n))

    populations.sort()
    return [len(populations)] + populations


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    result = get_villages_and_pops(grid, n)
    for element in result:
        print(element)
