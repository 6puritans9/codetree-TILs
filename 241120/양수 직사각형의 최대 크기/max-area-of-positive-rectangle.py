def preprocess(grid, down_max, n, m):
    for j in range(m):
        if grid[n-1][j] > 0:
            down_max[n-1][j] = 1

    for i in range(n-2, -1, -1):
        for j in range(m):
            if grid[i][j] > 0:
                down_max[i][j] = down_max[i+1][j] + 1


def get_max_area(down_max, n, m):
    max_area = float("-inf")

    for y in range(n):
        for x in range(m):
            max_height = float("inf")

            for l in range(x, m):
                max_height = min(max_height, down_max[y][l])

                max_area = max(max_area, max_height * (l - x + 1))
    
    return max_area if max_area > 0 else -1



if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    down_max = [[0 for _ in range(m)] for _ in range(n)]

    preprocess(grid, down_max, n, m)
    print(get_max_area(down_max, n, m))
