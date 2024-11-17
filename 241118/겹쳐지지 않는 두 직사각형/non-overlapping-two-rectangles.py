def get_rect_sum(grid, y1, x1, y2, x2):
    rect_sum = 0

    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
            rect_sum += grid[i][j]

    return rect_sum


def get_max_sum(grid, n, m):
    rectangles = []
    rectangles_size = 0
    max_sum = float("-inf")

    for y1 in range(n):
        for x1 in range(m):
            for y2 in range(y1, n):
                for x2 in range(x1, n):
                    rect_sum = get_rect_sum(grid,y1,x1,y2,x2)
                    rectangles.append((rect_sum, y1, x1, y2, x2))
                    rectangles_size += 1

    for i in range(rectangles_size):
        for j in range(rectangles_size):
            rect_sum1, y_start1, x_start1, y_end1, x_end1 = rectangles[i]
            rect_sum2, y_start2, x_start2, y_end2, x_end2 = rectangles[j]

            if y_start1 <= y_end2 and y_end1 >= y_start2 and x_start1 <= x_end2 and x_end1 >= x_start2:
                continue
            
            max_sum = max(max_sum, rect_sum1 + rect_sum2) 

    return max_sum


n, m = map(int, input().split())
grid = [[int(num) for num in input().split()] for _ in range(n)]

print(get_max_sum(grid, n, m))
