def in_range(x, n):
    return 0 <= x <= n


def does_s_come_first(pos, line):
    END = 1001
    dx = [1, -1]
    right = pos
    left = pos

    while True:
        if not in_range(right, END) and not in_range(left, END):
            break

        if line[right] == "S" or line[left] == "S":
            return True
        # elif line[left] == "S":
        #     return True
        elif line[right] == "N" or line[left] == "N":
            return False

        right += dx[0]
        left += dx[1]

    return False


T, a, b = map(int, input().split())
line = [None] * (1000 + 1)
for _ in range(T):
    char, pos = input().split()
    pos = int(pos)

    line[pos] = char

count = 0
for k in range(a, b + 1):
    if does_s_come_first(k, line):
        count += 1

print(count)