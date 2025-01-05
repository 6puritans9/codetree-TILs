def backtrack(grid, n, row, cnt, min_max, min_nums, visited):
    if cnt == n:
        min_max[0] = max(min_max[0], min(min_nums))
        return
    
    for col in range(0, n):
        if not visited[col]:
            visited[col] = True
            min_nums.append(grid[row][col])
            backtrack(grid, n, row + 1, cnt + 1, min_max, min_nums, visited)
            min_nums.pop()
            visited[col] = False


def find_min_max(grid, n):
    min_max = [0]
    visited = [False] * n

    backtrack(grid, n, 0, 0, min_max, [], visited)

    return min_max[0]


if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]

    print(find_min_max(grid, n))
