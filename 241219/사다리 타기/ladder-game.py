def simulate(n, lines):
    result = list(range(1, n + 1))
    for a, b in sorted(lines, key=lambda x: x[1]):
        result[a - 1], result[a] = result[a], result[a - 1]
    return result


def backtrack(n, all_lines, target_result, index=0, current_lines=[]):
    global min_lines

    if simulate(n, current_lines) == target_result:
        min_lines = min(min_lines, len(current_lines))
        return

    if index >= len(all_lines) or len(current_lines) >= min_lines:
        return

    backtrack(n, all_lines, target_result, index + 1, current_lines + [all_lines[index]])
    backtrack(n, all_lines, target_result, index + 1, current_lines)


def find_min_lines(n, m, all_lines):
    global min_lines
    min_lines = m 
    target_result = simulate(n, all_lines)

    backtrack(n, all_lines, target_result)
    return min_lines


if __name__ == '__main__':
    n, m = map(int, input().split())
    all_lines = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = find_min_lines(n, m, all_lines)
    print(result)
