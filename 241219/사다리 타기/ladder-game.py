def simulate(lines, n):
    """Simulates the ladder game."""
    result = [i for i in range(n + 1)]  # Initialize result with a placeholder 0 for alignment

    # Process lines sorted by depth
    for start, depth in sorted(lines, key=lambda x: x[1]):
        if start < n:  # Ensure bounds
            result[start], result[start + 1] = result[start + 1], result[start]

    return result


def backtrack(all_lines, idx, target, cur_lines, min_cost, n, m):
    """Recursive function to find the minimum lines."""
    # Base case: all lines processed
    if idx == m:
        if simulate(cur_lines, n) == target:
            return min(min_cost, len(cur_lines))
        return min_cost

    # Pruning: Stop if the current subset exceeds the best solution so far
    if len(cur_lines) >= min_cost:
        return min_cost

    # Recursive case: Try including and excluding the current line
    # Include the current line
    min_cost = backtrack(all_lines, idx + 1, target, cur_lines + [all_lines[idx]], min_cost, n, m)
    # Exclude the current line
    min_cost = backtrack(all_lines, idx + 1, target, cur_lines, min_cost, n, m)

    return min_cost


if __name__ == '__main__':
    # Input: Number of vertical lines (n) and horizontal lines (m)
    n, m = map(int, input().split())
    all_lines = [tuple(map(int, input().split())) for _ in range(m)]

    # Simulate target result with all lines
    target = simulate(all_lines, n)

    # Find the minimum number of lines using backtracking
    min_cost = float('inf')
    min_cost = backtrack(all_lines, 0, target, [], min_cost, n, m)

    print(min_cost)
