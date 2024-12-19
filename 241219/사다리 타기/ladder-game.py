
def simulate(lines):
    global n

    result = [i for i in range(n + 1)]

    for start, depth in sorted(lines, key=lambda x: x[1]):
        result[start], result[start + 1] = result[start + 1], result[start]

    return result


def backtrack(all_lines, idx, target, cur_lines):
    global min_cost, m

    if idx == m:
        return

    if simulate(cur_lines) == target:
        min_cost = min(min_cost, len(cur_lines))
        return

    backtrack(all_lines, idx + 1, target, cur_lines + [all_lines[idx]])
    backtrack(all_lines, idx + 1, target, cur_lines)


if __name__ == '__main__':
    n, m = map(int, input().split())
    all_lines = [tuple(map(int, input().split())) for _ in range(m)]

    target = simulate(all_lines)
    min_cost = float("inf")

    backtrack(all_lines, 0, target, [])
    print(min_cost)
