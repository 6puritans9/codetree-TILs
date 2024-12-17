def max_non_overlapping_intervals(lines):
    lines.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in lines:
        if start >= last_end:
            count += 1
            last_end = end

    return count


if __name__ == "__main__":
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]

    print(max_non_overlapping_intervals(lines))
