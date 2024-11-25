from collections import deque

def fill(grid, numbers, start_y, start_x, m1, m2, m3, m4):
    y = start_y
    x = start_x
    grid[y][x] = numbers.popleft()
        
    for i in range(m1):
        y -= 1
        x += 1

        grid[y][x] = numbers.popleft()

    for j in range(m2):
        y -= 1
        x -= 1

        grid[y][x] = numbers.popleft()

    for k in range(m3):
        y += 1
        x -= 1

        grid[y][x] = numbers.popleft()

    for l in range(m4 - 1):
        y += 1
        x += 1

        grid[y][x] = numbers.popleft()


def rotate(grid, start_y, start_x, m1, m2, m3, m4, d, n):
    numbers = deque([grid[start_y][start_x]])
    y, x = start_y, start_x

    for i in range(m1):
        y -= 1
        x += 1

        numbers.append(grid[y][x])

    for j in range(m2):
        y -= 1
        x -= 1

        numbers.append(grid[y][x])

    for k in range(m3):
        y += 1
        x -= 1

        numbers.append(grid[y][x])

    for l in range(m4 - 1):
        y += 1
        x += 1

        numbers.append(grid[y][x])

    if d:
        numbers.rotate(-1)
    else:
        numbers.rotate(1)

    fill(grid, numbers, start_y, start_x, m1, m2, m3, m4)



if __name__ == "__main__":
    n = int(input())
    grid = [[int(num) for num in input().split()] for _ in range(n)]
    r, c, m1, m2, m3, m4, direction = map(int, input().split())

    start_y, start_x = r- 1, c - 1
    rotate(grid, start_y, start_x, m1, m2, m3, m4, direction, n)

    for row in grid:
        print(" ".join(map(str, row)))