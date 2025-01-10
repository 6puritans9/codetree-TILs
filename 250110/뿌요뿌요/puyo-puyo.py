from typing import List, Tuple

def in_range(y:int, x:int, n:int) -> bool:
    return 0<=y<n and 0<=x<n


def bayoen(grid:List[List[int]], coords:List[Tuple[int, int]]) -> bool:
    for y, x in coords:
        grid[y][x] = 0

    return True


def visit_and_blast(grid:List[List[int]], y:int, x:int, n:int) -> Tuple[bool, int]:
    dys = [-1, 0, 1, 0]
    dxs = [0, 1, 0, -1]
    
    stack = []
    stack.append((y, x))

    did_blast = False
    cur_block_size = 1
    coords = []

    visited = [[False for _ in range(n)] for _ in range(n)]
    
    while stack:
        cy, cx = stack.pop()
        coords.append((cy, cx))
        visited[cy][cx] = True

        for dy, dx in zip(dys, dxs):
            ny, nx = cy + dy, cx + dx

            if in_range(ny, nx, n):
                if not visited[ny][nx] and grid[ny][nx] == grid[cy][cx]:
                    visited[ny][nx] = True
                    cur_block_size += 1
                    stack.append((ny, nx))
                    
    
    if len(coords) >= 4:
        did_blast = bayoen(grid, coords)
    
    return did_blast, cur_block_size
    

def play(grid:List[List[int]], n:int) -> Tuple[int, int]:
    blasted_count = 0
    biggest_block = 0

    for y in range(n):
        for x in range(n):
            if grid[y][x]:
                did_blast, block_size = visit_and_blast(grid, y, x, n)                
                
                blasted_count += 1 if did_blast else 0
                biggest_block = max(biggest_block, block_size)
                    
    return blasted_count, biggest_block


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    print(" ".join(map(str, play(grid, n))))
