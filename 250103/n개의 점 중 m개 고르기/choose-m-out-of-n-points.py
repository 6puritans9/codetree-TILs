from itertools import combinations

def precompute_distances(points):
    n = len(points)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            distances[i][j] = distances[j][i] = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return distances

def get_min_dist(points, m):
    n = len(points)
    distances = precompute_distances(points)
    min_dist = float("inf")

    for combo in combinations(range(n), m):
        max_distance = max(distances[i][j] for i in combo for j in combo if i < j)
        min_dist = min(min_dist, max_distance)

    return min_dist

if __name__ == "__main__":
    n, m = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    result = get_min_dist(points, m)
    print(result)
