def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def get_sum(table, n, m):
    max_sum = 0
    figures = [[(-1, 0), (0, 0), (0, 1)],
               [(0, 1), (0, 0), (1, 0)],
               [(1, 0), (0, 0), (0, -1)],
               [(0, -1), (0, 0), (-1, 0)],
               [(0, -1), (0, 0), (0, 1)],
               [(-1, 0), (0, 0), (1, 0)]]

    for y in range(n):
        for x in range(m):
            for fig in figures:
                cur_sum = 0
                is_valid = True

                for dx, dy in fig:
                    ny, nx = y + dy, x + dx
                    if not in_range(nx, ny, n, m):
                        is_valid = False
                        break

                    cur_sum += table[ny][nx]

                if is_valid:
                    max_sum = max(max_sum, cur_sum)

    return max_sum


n, m = map(int, input().split())
table = [[int(num) for num in input().split()] for _ in range(n)]

result = get_sum(table, n, m)
print(result)