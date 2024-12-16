def in_range(y, x):
    return 0 <= y < n and 0 <= x < n


def blast(y, x, _type):
    bomb_shapes = [
        None,
        [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
        [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
        [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
    ]

    bomb_shape = bomb_shapes[_type]
    for dy, dx in bomb_shape:
        ny, nx = y + dy, x + dx
        if in_range(ny, nx):
            bombed[ny][nx] = True


def reset(grid, n):
    for y in range(n):
        for x in range(n):
            grid[y][x] = False


def calc(bomb_type, bombed, n):
    reset(bombed, n)

    for y in range(n):
        for x in range(n):
            if bomb_type[y][x]:
                blast(y, x, bomb_type[y][x])

    cnt = 0
    for i in range(n):
        for j in range(n):
            if bombed[i][j]:
                cnt += 1

    return cnt


def find_max_area(bomb_type, bombed, n, pos_idx):
    global ans

    if pos_idx == len(bomb_pos):
        cur_count = calc(bomb_type, bombed, n)
        ans = max(ans, cur_count)
        return

    for i in range(1, 4):
        y, x = bomb_pos[pos_idx]

        bomb_type[y][x] = i
        find_max_area(bomb_type, bombed, n, pos_idx + 1)
        bomb_type[y][x] = 0


if __name__ == "__main__":
    n = int(input())
    bomb_type = [[0 for _ in range(n)] for _ in range(n)]
    bombed = [[False for _ in range(n)] for _ in range(n)]
    bomb_pos = []
    ans = 0

    for y in range(n):
        _input = input().split()
        for x, char in enumerate(_input):
            if int(char):
                bomb_pos.append((y, x))

    find_max_area(bomb_type, bombed, n, 0)
    print(ans)
