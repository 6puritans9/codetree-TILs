def find_min_dist(n:int, points:list[int]) -> int:
    min_dist = float("inf")
    
    for i in range(1, n-1):
        new_points = points[:i] + points[i+1:]

        cur_dist = 0
        for j in range(n-2):
            cx, cy = new_points[j]
            nx, ny = new_points[j+1]

            cur_dist += (abs(cx-nx) + abs(cy-ny))
        
        min_dist = min(min_dist, cur_dist)
        
    return min_dist


if __name__ == "__main__":
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    print(find_min_dist(n, points))