def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n


def play(values_grid, beads_pos, n):
    dys = [-1, 1, 0, 0]  
    dxs = [0, 0, -1, 1]

    new_positions = {}

    
    for i, (y, x) in enumerate(beads_pos):
        best_value = -1
        best_pos = (y, x) 

        for dy, dx in zip(dys, dxs):
            ny, nx = y + dy, x + dx
            if in_range(ny, nx, n) and values_grid[ny][nx] > best_value:
                best_value = values_grid[ny][nx]
                best_pos = (ny, nx)

        if best_pos not in new_positions:
            new_positions[best_pos] = []
        new_positions[best_pos].append(i)

    
    updated_positions = []
    for pos, indices in new_positions.items():
        if len(indices) == 1:  
            updated_positions.append(pos)

    return updated_positions


if __name__ == '__main__':
    n, m, t = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    beads_given = [tuple(map(int, input().split())) for _ in range(m)]

    beads_pos = [(r - 1, c - 1) for r, c in beads_given]

    for _ in range(t):
        beads_pos = play(grid, beads_pos, n)

    print(len(beads_pos))
