def is_crossed(left_line, right_line):
    start_left_line = left_line[0]
    end_left_line = left_line[1]

    start_right_line = right_line[0]
    end_right_line = right_line[1]

    if start_left_line <= start_right_line < end_left_line and end_right_line <= end_left_line:
        return True

    return False

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

overlapping_lines = set()

for i in range(N):
    for j in range(N):
        if i != j and is_crossed(lines[i], lines[j]):
            overlapping_lines.add(lines[i])
            overlapping_lines.add(lines[j])

non_overlapping_count = N - len(overlapping_lines)

print(non_overlapping_count)