def is_crossed(left_dot, right_dot):
    start_left_dot = left_dot[0]
    end_left_dot = left_dot[1]

    start_right_dot = right_dot[0]
    end_right_dot = right_dot[1]

    if start_right_dot < end_left_dot and end_right_dot <= end_left_dot:
        return True

    return False

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

overlapping_lines = set()

for i in range(N):
    for j in range(i + 1, N):
        if is_crossed(lines[i], lines[j]):
            overlapping_lines.add(lines[i])
            overlapping_lines.add(lines[j])

non_overlapping_count = N - len(overlapping_lines)

print(non_overlapping_count)