# def is_range(row, col):
#     global n, m

#     return 0 <= row < n and 0 <= col < m


def propagate_up(grid, row, direction):
    global n, m
    
    if row < 0:
        return

    for col in range(m):
        if grid[row][col] == grid[row + 1][col]:
            manipulate(grid, row, direction)
            propagate_up(grid, row - 1, not direction)
            break


def propagate_down(grid, row, direction):
    global n, m
    
    if row > n - 1:
        return

    for col in range(m):
        if grid[row][col] == grid[row - 1][col]:
            manipulate(grid, row, direction)
            propagate_down(grid, row + 1, not direction)
            break
   


def manipulate(grid, row, direction):
    if direction == True:
        temp_grid = grid[row][-1]

        for i in range(m-1, 0, -1):
            grid[row][i] = grid[row][i-1]
        grid[row][0] = temp_grid
    
    else:
        temp_grid = grid[row][0]

        for i in range(m-1):
            grid[row][i] = grid[row][i+1]
        grid[row][-1] = temp_grid


if __name__ == "__main__":
    n, m, q = map(int, input().split())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    winds = []
    for _ in range(q):
        row, direction = input().split()
        row = int(row) - 1
        direction = False if direction == "L" else True
        winds.append((row, direction))

    for row, direction in winds:
        manipulate(grid, row, direction)
        propagate_up(grid, row-1, not direction)
        propagate_down(grid, row+1, not direction)

for row in grid:
    for col in row:
        print(col, end=" ")
    print()