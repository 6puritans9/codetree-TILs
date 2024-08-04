def get_min_dist(N, peoples):
    min_dist = float("inf")

    for end in range(N):
        total_dist = 0

        for start in range(N):
            dist = (start + N - end) % N
            total_dist += peoples[start] * dist

        if min_dist > total_dist:
            min_dist = total_dist

    return min_dist


N = int(input())
peoples = [int(input()) for _ in range(N)]

min_dist = get_min_dist(N, peoples)
print(min_dist)