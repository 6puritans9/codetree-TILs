def get_min_dist(N, peoples):
    prefix_sum = [0] * N

    for i in range(N):
        if i == 0:
            prefix_sum[i] = peoples[i]

        prefix_sum[i] = prefix_sum[i - 1] + peoples[i]
    
    min_dist = float("inf")

    for start in range(N):
        total_dist = 0

        for i in range(N):
            dist = (i + start) % N
            total_dist += peoples[i] * dist

        if min_dist > total_dist:
            min_dist = total_dist

    return min_dist


N = int(input())
peoples = [int(input()) for _ in range(N)]

min_dist = get_min_dist(N, peoples)
print(min_dist)