def get_distance(sub_points_group):
    n = len(sub_points_group)
    max_distance = 0

    for i in range(n):
        x1, y1 = sub_points_group[i]

        for j in range(i, n):
            x2, y2 = sub_points_group[j]

            cur_distance = ((x1 - x2)**2 + (y1 - y2)**2)
            max_distance = max(max_distance, cur_distance)
    
    return max_distance


def backtrack(n, m, points, min_dist, idx, sub_points_group):
    if len(sub_points_group) == m:
        farthest_distance = get_distance(sub_points_group)
        min_dist[0] = min(min_dist[0], farthest_distance)
        return
    if idx >= n:
        return

    sub_points_group.append(points[idx])
    backtrack(n, m, points, min_dist, idx + 1, sub_points_group)
    sub_points_group.pop()

    backtrack(n, m, points, min_dist, idx + 1, sub_points_group)


def get_min_dist(n, m, points):
    min_dist = [float("inf")]

    backtrack(n, m, points, min_dist, 0, [])
    
    return min_dist[0]


if __name__ == "__main__":
    n, m = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    min_dist = get_min_dist(n, m, points)
    print(min_dist)