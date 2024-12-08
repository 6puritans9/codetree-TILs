def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def play(values_grid, beads_grid, beads_pos, n):
    dys = [-1, 1, 0, 0]
    dxs = [0, 0, -1, 1]

    for i, pos in enumerate(beads_pos):
        if not pos:
            continue

        y, x = pos
        cur_value = values_grid[y][x]

        for dy, dx in zip(dys, dxs):
            ny = y + dy
            nx = x + dx

            if in_range(ny, nx, n):
                nxt_value = values_grid[ny][nx]

                if nxt_value > cur_value:
                    cur_value = nxt_value
                    beads_grid[ny][nx] = 1
                    beads_grid[y][x] = 0
                    beads_pos[i] = [ny, nx]


    for i, pos in enumerate(beads_pos):
        if beads_pos.count(pos) > 1:
            y, x = pos
            beads_grid[y][x] = 0
            beads_pos[i] = None


n, m, t = tuple(map(int, input().split()))
grid = [[int(num) for num in input().split()] for _ in range(n)]
beads_given = [tuple(int(num) for num in input().split()) for _ in range(m)]

beads = [[0 for _ in range(n)] for _ in range(n)]
beads_pos = []
for r, c in beads_given:
    y, x = r - 1, c - 1

    beads[y][x] = 1
    beads_pos.append([y, x])

for _ in range(t):
    play(grid, beads, beads_pos, n)

print(sum(sum(row) for row in beads))
