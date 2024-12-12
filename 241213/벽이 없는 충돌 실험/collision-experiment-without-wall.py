def in_range(x, y):
    return -1000 <= x <= 1000 and -1000 <= y <= 1000


def is_stuck(bead):
    if not bead[-1]:
        return True

    x, y = bead[0], bead[1]

    return True if not in_range(y, x) else False


def move(bead):
    directions = {"L": (-0.5, 0), "R": (0.5, 0), "U": (0, 0.5), "D": (0, -0.5)}
    x, y, w, d, i, s = bead

    dx, dy = directions[d]
    nx, ny = x + dx, y + dy

    bead[0], bead[1] = nx, ny


def collide(array):
    # x, y, w, d, i, s = bead
    array.sort(key=lambda x: (x[2], x[4]))

    for i in range(len(array) - 1):
        array[i][-1] = False


def handle_collisions(beads):
    positions = {}
    did_collide = False

    for bead in beads:
        x, y, w, d, i, s = bead
        if not s:
            continue

        if (x, y) not in positions:
            positions[(x, y)] = []
        positions[(x, y)].append(bead)

    for array in positions.values():
        if len(array) > 1:
            collide(array)
            did_collide = True

    return did_collide


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        beads = []
        count = 1
        latest_collision = -1
        collided = False

        for i in range(n):
            x, y, w, d = input().split()
            beads.append([float(x), float(y), int(w), d, i, True])

        deadlocked = False
        while not deadlocked:
            stucked_beads_count = 0

            for bead in beads:
                move(bead)
                stucked_beads_count += 1 if is_stuck(bead) else 0

            collided = handle_collisions(beads)
            if collided:
                latest_collision = count

            if stucked_beads_count == n:
                deadlocked = True

            count += 1

        print(latest_collision)
