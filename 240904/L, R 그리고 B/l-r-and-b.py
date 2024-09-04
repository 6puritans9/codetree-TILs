from collections import deque

def find_shortest_path(grid):
    def find_position(char):
        for i in range(10):
            for j in range(10):
                if grid[i][j] == char:
                    return i, j
        return -1, -1

    start = find_position('L')
    end = find_position('B')
    block = find_position('R')

    queue = deque([(start[0], start[1], 0)])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        x, y, distance = queue.popleft()
        
        if (x, y) == end:
            return distance - 1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 10 and 0 <= ny < 10 and (nx, ny) not in visited and (nx, ny) != block:
                visited.add((nx, ny))
                queue.append((nx, ny, distance + 1))

    return -1

grid = [input().strip() for _ in range(10)]

result = find_shortest_path(grid)
print(result)