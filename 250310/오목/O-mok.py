def in_range(n, y, x):
    return 0<=y<n and 0<=x<n


def is_consecutive(n, grid, y, x) -> int:
    start_color = grid[y][x]
    result = 0
    
    # hor
    for dx in range(x, x+5):
        if in_range(n, y, dx) and grid[y][dx] == start_color:
            result = 1
        else:
            result = 0
            break
    if result:
        return result

    # ver
    for dy in range(y, y+5):
        if in_range(n, dy, x) and grid[dy][x] == start_color:
            result = 2
        else:
            result = 0
            break
    if result:
        return result

    # diag_right
    i = 0
    for dy in range(y, y+5):
        dx = x + i
        
        if in_range(n, dy, dx) and grid[dy][dx] == start_color:
            result = 3
        else:
            result = 0
            break
        i += 1

    if result:
        return result

    # diag_left
    i = 0
    for dy in range(y, y+5):
        dx = x - i
        if in_range(n, dy, dx) and grid[dy][dx] == start_color:
            result = 4
        else:
            result = 0
            break
        
        i -= 1
    
    return result


def find_middle(n, y, x, case) -> tuple[int]:
    ny, nx = -1, -1

    if case == 1:
        ny, nx = y, x + 2
    elif case == 2:
        ny, nx = y +2, x
    elif case == 3:
        ny, nx = y + 2, x + 2
    elif case == 4:
        ny, nx = y + 2, x - 2

    return ny + 1, nx + 1


def find_winner(n:int, grid:list[list[int]]) -> list[int]:
    # state, y, x
    answer = [0, -1, -1]

    for y in range(n):
        for x in range(n):
            if not grid[y][x]:
                continue
            
            win_condition = is_consecutive(n, grid, y, x)
            if win_condition:
                # color, y, x
                ny, nx = find_middle(n,y,x,win_condition)
                answer = [grid[y][x], ny, nx]
                return answer

    return answer


if __name__ =="__main__":
    # In the 19 * 19 sized given table
    # 1 represents black and 2 represents white while 0 for empty space.
    
    # Since the boundary is only 19*19, I can make exhaustive search for
    # hor, ver and 2 diagonal directions(left top >> right bottom, right top >> left bottom)
    # Also, boundary check is required for this process.

    # If there's a winner, print the color. if not, print 0
    # If there's a winner, print the coordinate of the stone which is in the middle of the row(y+1, x+1)
    
    BOUNDARY = 19

    grid = []
    for _ in range(BOUNDARY):
        grid.append(tuple(map(int, input().split())))

    result = find_winner(BOUNDARY, grid)
    if not result[0]:
        print(0)
    else:
        print(result[0])
        print(result[1], result[2])

