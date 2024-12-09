def in_range(y, x, n):
    return 0<=y<n and 0<=x<n

def turn(beads, idx):
    direction = beads[idx][2]

    if direction == "L":
        beads[idx][2] = "R"
    elif direction == "R":
        beads[idx][2] = "L"
    elif direction == "U":
        beads[idx][2] = "D"
    else:
        beads[idx][2] = "U"
    

def move(beads, n, idx, y, x, d):
    ny, nx = None, None
    if d == "L":
        ny, nx = y, x - 1
    elif d == "R":
        ny, nx = y, x + 1
    elif d == "U":
        ny, nx = y - 1, x
    else:
        ny, nx = y + 1, x

    if not in_range(ny, nx, n):
        turn(beads, idx)
        return

    beads[idx][0] = ny
    beads[idx][1] = nx


def remove(beads, beads_length):
    beads_positions = {}
    valid_beads = []
    
    for i in range(beads_length):
        cur_y, cur_x, d = beads[i]
        
        if (cur_y, cur_x) not in beads_positions:
            beads_positions[(cur_y, cur_x)] = []
        
        beads_positions[(cur_y, cur_x)].append(i)
    
    for pos, indices in beads_positions.items():
        if len(indices) == 1:
            valid_beads.append(beads[indices[0]])

    return valid_beads


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        beads = []
        n, m = tuple(map(int, input().split()))

        for _ in range(m):
            row, col, direction = input().split()
            beads.append([int(row) - 1, int(col) - 1, direction])

        for _ in range(n * n):
            for i, bead in enumerate(beads):
                y, x, d = bead

                move(beads, n, i, y, x, d)
            beads = remove(beads, len(beads))

        print(len(beads))