def is_overlap(visited, start2, end2):
    for start1, end1 in visited:
        if start1 <= end2 and end1 >= start2:
            return True

    return False


def backtrack(lines, n, idx, visited):
    global max_count

    if idx == n:
        max_count = max(max_count, len(visited))
        return

    start1, end1 = lines[idx]
    if not is_overlap(visited, start1, end1):
        visited.add((start1, end1))
        backtrack(lines, n, idx + 1, visited)
        visited.remove((start1, end1))

    backtrack(lines, n, idx + 1, visited)


if __name__ == "__main__":
    n = int(input())
    lines = [tuple(map(int, input().split())) for _ in range(n)]
    max_count = 0

    backtrack(lines, n, 0, set())
    print(max_count)
