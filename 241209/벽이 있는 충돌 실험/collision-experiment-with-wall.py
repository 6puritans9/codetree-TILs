def in_range(y, x, n):
    return 0 <= y < n and 0 <= x < n

def reverse_direction(direction):
    return {"L": "R", "R": "L", "U": "D", "D": "U"}[direction]

def move(beads, n):
    new_positions = {}
    for idx, (y, x, d) in enumerate(beads):
        # Calculate new position
        if d == "L":
            ny, nx = y, x - 1
        elif d == "R":
            ny, nx = y, x + 1
        elif d == "U":
            ny, nx = y - 1, x
        elif d == "D":
            ny, nx = y + 1, x

        # Handle boundary collision
        if not in_range(ny, nx, n):
            ny, nx = y, x
            d = reverse_direction(d)

        # Update position
        if (ny, nx) not in new_positions:
            new_positions[(ny, nx)] = []
        new_positions[(ny, nx)].append((ny, nx, d, idx))

    # Handle collisions
    remaining_beads = []
    for positions in new_positions.values():
        if len(positions) == 1:  # No collision
            remaining_beads.append(positions[0][:3])  # Keep position and direction
    return remaining_beads

def simulate_beads(n, m, beads):
    seen_states = set()
    max_iterations = n * n * 4  # Set a practical upper limit
    iterations = 0

    while beads and iterations < max_iterations:
        # Generate the current state as a sorted frozenset
        current_state = frozenset((y, x, d) for y, x, d in beads)

        # Check if this state was seen before
        if current_state in seen_states:
            break  # Cycle detected
        seen_states.add(current_state)

        # Move beads and handle collisions
        beads = move(beads, n)
        iterations += 1

    return len(beads)

if __name__ == "__main__":
    t = int(input())
    results = []

    for _ in range(t):
        n, m = map(int, input().split())
        beads = []
        for _ in range(m):
            x, y, d = input().split()
            beads.append((int(x) - 1, int(y) - 1, d))

        results.append(simulate_beads(n, m, beads))

    for result in results:
        print(result)
