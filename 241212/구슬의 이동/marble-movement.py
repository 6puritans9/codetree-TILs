def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def turn(d):
    nxt_directions = {"L": "R", "R": "L", "U": "D", "D": "U"}

    return nxt_directions[d]


def move(bead, n):
    r, c, d, v, i, s = bead
    directions = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}

    y, x = r, c
    dy, dx = directions[d]

    for _ in range(v):
        ny, nx = y + dy, x + dx

        if not in_range(ny, nx, n):
            d = turn(d)
            dy, dx = directions[d]
            ny, nx = y + dy, x + dx

        y, x = ny, nx

    bead[0], bead[1] = y, x


def collide(array, k):
    array.sort(key=lambda x: (x[3], x[4]))

    for i in range(len(array) - 1, -1 + k, -1):
        element = array[i]
        element[-1] = False


def handle_collision(beads, k, n):
    grid = {}

    for bead in beads:
        y, x, d, v, i, s = bead

        if (y, x) not in grid:
            grid[(y, x)] = []

        grid[(y, x)].append(bead)

    for (y, x), array in grid.items():
        if len(array) > k:
            collide(grid[(y, x)], k)


def operate(beads, k, n):
    for bead in beads:
        is_active = bead[-1]

        if is_active:
            move(bead, n)

    handle_collision(beads, k, n)


if __name__ == "__main__":
    n, m, t, k = tuple(map(int, input().split()))
    # grid = [[[] for _ in range(n)] for _ in range(n)]
    data = []
    for _ in range(m):
        r, c, d, v = input().split()
        data.append((int(r), int(c), d, int(v)))

    beads = []
    for i, element in enumerate(data):
        r, c, d, v = element
        beads.append([r - 1, c - 1, d, v, i + 1, True])  # y, x, d, v, order, status
    # for bead in beads:
    #     y, x, d, v, i, s = bead
    #     grid[y][x].append(bead)

    for _ in range(t):
        operate(beads, k, n)

    count = 0
    # for y in range(n):
    #     for x in range(n):
    #         _sum += len(grid[y][x])
    for bead in beads:
        if bead[-1]:
            count += 1

    print(count)
