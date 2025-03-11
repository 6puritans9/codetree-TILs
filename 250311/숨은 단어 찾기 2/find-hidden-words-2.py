def in_range(y, x, n, m) -> bool:
    return 0<=y<n and 0<=x<m


def find_lee_counts(n:int, m:int, grid:list[list[str]]) -> int:
    # TC = O(N * M)
    # SC = O(1)

    dys = (-1,-1,-1,0,0,0,1,1,1)
    dxs = (-1,0,1,-1,0,1,-1,0,1)

    count = 0
    for cy in range(n):
        for cx in range(m):
            if grid[cy][cx] != "L":
                continue

            for dy, dx in zip(dys, dxs):
                for i in range(1, 3):
                    ny, nx = cy + dy * i, cx + dx * i

                    if not in_range(ny, nx, n, m) or grid[ny][nx] != "E":
                        is_correct = False
                        break
                else:
                    count += 1

    return count


if __name__ =="__main__":
    # For 8 directions which can proceed from a point 'L',
    # if the next tile is 'E', check again
    # if the second tile is also 'E', count += 1
    # To make sure the checks are in n * m boundary, a helper function is needed
    # if (y, x) == (n-1, m-1), return count

    n, m = map(int, input().split())
    grid = [tuple(char for char in input()) for _ in range(n)]
    
    print(find_lee_counts(n, m, grid))
