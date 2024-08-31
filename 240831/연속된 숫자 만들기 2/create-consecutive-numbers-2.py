def min_movements(positions):
    gaps = [positions[1] - positions[0], positions[2] - positions[1]]

    if gaps[0] == 1 and gaps[1] == 1:
        return 0

    if gaps[0] == 2 or gaps[1] == 2:
        return 1

    return 2


positions = list(map(int, input().split()))
positions.sort()

print(min_movements(positions))