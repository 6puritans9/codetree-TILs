def is_crossed(line1, line2):
    x1_start, x1_end = line1
    x2_start, x2_end = line2

    return (x1_start < x2_start and x1_end > x2_end) or (x1_start > x2_start and x1_end < x2_end)

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