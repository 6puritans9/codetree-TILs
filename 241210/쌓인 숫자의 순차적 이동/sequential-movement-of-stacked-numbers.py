from collections import deque


def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def get_coordinate(grid, target):
    y, x = None, None

    for i in range(n):
        found_target = False

        for j in range(n):
            if target in grid[(i, j)]:
                y, x = i, j
                found_target = True
                break
        if found_target:
            break

    return [y, x]


def compare(grid, n, y, x):
    dys = [-1, -1, 0, 1, 1, 1, 0, -1]
    dxs = [0, 1, 1, 1, 0, -1, -1, -1]

    biggest_num = 0
    nxt_y, nxt_x = None, None
    for dy, dx in zip(dys, dxs):
        ny = y + dy
        nx = x + dx
        if in_range(ny, nx, n):
            numbers = grid[(ny, nx)]

            for number in numbers:
                if number > biggest_num:
                    biggest_num = number
                    nxt_y, nxt_x = ny, nx

    return [nxt_y, nxt_x]


def shift(grid, target, cur_y, cur_x, nxt_y, nxt_x):
    if not nxt_y and not nxt_x:
        return

    target_idx = None

    for i in range(len(grid[(cur_y, cur_x)])):
        if grid[(cur_y, cur_x)][i] == target:
            target_idx = i
            break

    grid[(cur_y, cur_x)].rotate(-(target_idx + 1))

    for _ in range(target_idx + 1):
        number = grid[(cur_y, cur_x)].pop()
        grid[(nxt_y, nxt_x)].appendleft(number)


def operate(grid, n, target):
    cur_y, cur_x = get_coordinate(grid, target)
    nxt_y, nxt_x = compare(grid, n, cur_y, cur_x)
    shift(grid, target, cur_y, cur_x, nxt_y, nxt_x)


if __name__ == "__main__":
    n, m = tuple(map(int, input().split()))
    data = [[int(num) for num in input().split()] for _ in range(n)]
    grid = {}
    for i in range(n):
        for j in range(n):
            grid[(i, j)] = deque([data[i][j]])

    a, b, c, d = input().split()
    targets = [int(a), int(b), int(c), int(d)]

    for target in targets:
        operate(grid, n, target)

    for i in range(n):
        for j in range(n):
            if grid[(i, j)]:
                for el in grid[(i, j)]:
                    print(el, end=" ")
            else:
                print("None", end="")
            print()

