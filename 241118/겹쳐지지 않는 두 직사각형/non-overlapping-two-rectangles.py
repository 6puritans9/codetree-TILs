def get_rect_sum(grid, x1, y1, x2, y2):
    total = 0
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            total += grid[i][j]
    return total

def get_max_sum(grid, n, m):
    max_sum = float('-inf')
    
    rectangles = []
    for x1 in range(n):
        for y1 in range(m):
            for x2 in range(x1, n):
                for y2 in range(y1, m):
                    rect_sum = get_rect_sum(grid, x1, y1, x2, y2)
                    rectangles.append((rect_sum, x1, y1, x2, y2))
    
    for i in range(len(rectangles)):
        sum1, x1a, y1a, x2a, y2a = rectangles[i]
        for j in range(i + 1, len(rectangles)):
            sum2, x1b, y1b, x2b, y2b = rectangles[j]
            
            if not (x1a <= x2b and x1b <= x2a and y1a <= y2b and y1b <= y2a):
                max_sum = max(max_sum, sum1 + sum2)
    
    return max_sum

n, m = map(int, input().split())
grid = [[int(num) for num in input().split()] for _ in range(n)]

result = get_max_sum(grid, n, m)
print(result)
