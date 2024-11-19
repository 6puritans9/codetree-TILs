def get_max_size(grid, n, m):
    max_size = 0

    # Iterate over all possible top-left corners
    for start_row in range(n):
        for start_col in range(m):
            # Only consider rectangles starting with positive values
            if grid[start_row][start_col] <= 0:
                continue

            # Iterate over all possible bottom-right corners
            for end_row in range(start_row, n):
                for end_col in range(start_col, m):
                    # Check if the rectangle is valid
                    is_valid = True
                    for i in range(start_row, end_row + 1):
                        for j in range(start_col, end_col + 1):
                            if grid[i][j] <= 0:
                                is_valid = False
                                break
                        if not is_valid:
                            break

                    # If valid, calculate the area
                    if is_valid:
                        area = (end_row - start_row + 1) * (end_col - start_col + 1)
                        max_size = max(max_size, area)

    return max_size if max_size > 0 else -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    print(get_max_size(grid, n, m))
