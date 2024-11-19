def get_max_size(grid, n, m):
    max_size = 0

    for start_y in range(n):
        for start_x in range(m):
            for end_y in range(start_y, n):
                for end_x in range(start_x, m):
                    is_valid = True

                    for i in range(start_y, end_y + 1):
                        for j in range(start_x, end_x + 1):
                            if grid[i][j] <= 0:
                                is_valid = False
                                break

                        if not is_valid:
                            break

                    if is_valid:
                        area_size = (end_y + 1 - start_y) * (end_x + 1 - start_x)
                        max_size = max(max_size, area_size)

    return max_size if max_size > 0 else -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    print(get_max_size(grid, n, m))
