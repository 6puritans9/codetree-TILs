def get_result(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    count = 0
    for x in range(x1 + 1, x2):
        for y in range(y1 + 1, y2):
            count += 1

    return count

R, C = list(map(int, input().split()))
# grid = []
blacks = []

for i in range(R):
    _string = input()
    # sub_grid = []
    j = 0

    for char in _string:
        if char == "B":
            blacks.append((i, j))
        elif char == " ":
            continue

        j += 1
    #     sub_grid.append(char)

    # grid.append(sub_grid)

result = 0
for i in range(len(blacks) - 1):
    for j in range(i +1, len(blacks)):
        result += get_result(blacks[i], blacks[j])

print(result)