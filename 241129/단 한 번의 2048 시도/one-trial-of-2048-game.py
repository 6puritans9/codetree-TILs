def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def move_and_merge_line(line):
    n = len(line)
    merged = [False] * n
    new_line = [0] * n
    idx = 0

    for i in range(n):
        if line[i] != 0:
            if idx > 0 and new_line[idx - 1] == line[i] and not merged[idx - 1]:
                new_line[idx - 1] *= 2
                merged[idx - 1] = True
            else:
                new_line[idx] = line[i]
                idx += 1

    return new_line


def move(grid, direction):
    n = len(grid)
    if direction == "L":
        for y in range(n):
            grid[y] = move_and_merge_line(grid[y])
    elif direction == "R":
        for y in range(n):
            grid[y] = move_and_merge_line(grid[y][::-1])[::-1]
    elif direction == "U":
        for x in range(n):
            column = [grid[y][x] for y in range(n)]
            new_column = move_and_merge_line(column)
            for y in range(n):
                grid[y][x] = new_column[y]
    elif direction == "D":
        for x in range(n):
            column = [grid[y][x] for y in range(n)][::-1]
            new_column = move_and_merge_line(column)[::-1]
            for y in range(n):
                grid[y][x] = new_column[y]


if __name__ == "__main__":
    grid = [[int(num) for num in input().split()] for _ in range(4)]
    direction = input()

    move(grid, direction)

    for row in grid:
        print(" ".join(map(str, row)))
